import streamlit as st
import json

from langchain_openai.chat_models import ChatOpenAI

from helpers.constants import OPEN_AI_API_KEY, PATTERN
from helpers.utils import generate_response, get_prompt

st.title("Irish Ads")


if __name__ == "__main__":
    with st.form("irish_ads"):
        # ! asking for the product information
        product_info = st.text_area(
            "Paste Product Information",
            "",
            placeholder="Paste your product information here",
        )
        submitted = st.form_submit_button("Submit")

        model = ChatOpenAI(temperature=0.7, api_key=OPEN_AI_API_KEY)  # type: ignore

        # ! this is the prompt for the product information
        product_response = generate_response(model, product_info)
        st.info(product_response)

        # ! this would be the response for getting the ICP

        print(json.dumps(get_prompt("format.json"), indent=2))
        icp_json = generate_response(model, f"{product_response}\n{PATTERN}")  # type: ignore
        st.json(icp_json)
