# flake8: noqa
from langchain.prompts import PromptTemplate

prompt_template = """Write a concise summary of the following:


"{text}"


CONCISE SUMMARY IN CHINESE:"""

prompt_template_cn = """对以下内容进行分点总结，并给出用户可能想知道的问题:


"{text}"


总结:"""
PROMPT = PromptTemplate(template=prompt_template_cn, input_variables=["text"])
