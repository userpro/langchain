# flake8: noqa
from langchain.prompts import PromptTemplate

prompt_template = """Write a concise summary of the following:


"{text}"


CONCISE SUMMARY:"""

prompt_template_a = """Make a point-by-point summary of the following:


"{text}"


CONCISE SUMMARY IN CHINESE:"""
PROMPT = PromptTemplate(template=prompt_template_a, input_variables=["text"])
