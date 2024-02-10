import os

from langchain.llms.base import BaseLLM
from langchain_openai import OpenAI

api_key: str = os.environ['OPENAI_API_KEY']

chatgpt: BaseLLM = OpenAI(temperature=0, api_key=api_key)
