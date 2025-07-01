import re

from langchain_openai.chat_models import ChatOpenAI
import gspread


def generate_response(model: ChatOpenAI, input_text: str):
    response = model.invoke(input_text)
    return response.content


def get_prompt(prompt_file: str = "prompt.txt"):
    with open(prompt_file, "r") as file:
        return file.read()


def encode_to_sheet(
    icp_json: dict,
    field: str,
    gc: gspread.Client,
    sheet_name: str,
    letter: str,
):
    icp_overview: dict = icp_json.get(field)  # type: ignore
    sh = gc.open("My VAs")
    sheet = sh.worksheet(sheet_name)

    counter = 1
    for key, value in icp_overview.items():
        print(f"{letter}{counter}: \t {value}")

        # format for ad_concepts (we need to loop through it and add the values to the text)
        # Concept: “Why Your ESB Bill Is So High—and What’s Really Draining Your Power”
        # Hook: “What if one plug could stop hidden energy waste?”
        # Headline: “How a Tiny Device in My Flat Cut My Bill by 70%”
        try:
            if field == "ad_concepts":
                text = f"Ad Concept: {value}\n"
                for ad_key, ad_value in value.items():
                    text += f"{ad_key}: {ad_value}\n"
            else:
                text = f"{key}: {value}"
        except Exception as e:
            text = f"{key}: {value}"

        sheet.update_acell(f"{letter}{counter}", text)
        counter += 1
