from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from threading import Lock

from .config import Config
from .directory_iterators import get_all_modules
from .docstring_writer import process_file, process_function


def generate_project_docstrings(
    config: Config, source_code_queue: Queue, function_code_queue: Queue
) -> None:
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(get_all_modules, config, source_code_queue)
        executor.submit(process_file, source_code_queue, function_code_queue)
        executor.submit(process_function, config, function_code_queue)
    source_code_queue.join()
    function_code_queue.join()
