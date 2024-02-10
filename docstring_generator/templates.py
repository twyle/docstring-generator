from langchain.prompts import PromptTemplate

function_prompt_template: str = """
Generate python docstring for the given python function using the provided documentation style.
Make sure to provide atleast two examples of the function usage only in the docstring as well
as the exceptions that may be raised when using the function. Make sure to return the
function and its docstring.
Function code: {function_code}
Documentation style: {documentation_style}
"""
function_prompt = PromptTemplate.from_template(template=function_prompt_template)
