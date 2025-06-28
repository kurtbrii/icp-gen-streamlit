import json
import os
from langchain_openai.chat_models import ChatOpenAI


def generate_response(model: ChatOpenAI, input_text: str):
    response = model.invoke(input_text)
    return response.content


def get_prompt(prompt_file: str = "prompt.txt"):
    with open(prompt_file, "r") as file:
        return file.read()
