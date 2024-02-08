from dotenv import load_dotenv

load_dotenv()
import os

from langchain.llms.base import BaseLLM
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

api_key: str = os.environ['OPENAI_API_KEY']

llm: BaseLLM = OpenAI(temperature=0, api_key=api_key)

function_prompt_template: str = """
Generate python docstring for the given python function using the provided documentation style:
Function code: {function_code}
Documentation style: {documentation_style}
"""

function_code: str = """
def add(a: int | float, b: int | float) -> int | float:
    return operator.add(a, b)
"""
documentation_style: str = 'Numpy-Style'

prompt = PromptTemplate.from_template(template=function_prompt_template)
prompt_formatted_str: str = prompt.format(
    function_code=function_code, documentation_style=documentation_style
)

function_and_docstring: str = llm.invoke(prompt_formatted_str)
print(function_and_docstring)
