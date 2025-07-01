import streamlit as st
import json

from langchain_openai.chat_models import ChatOpenAI
import gspread

from helpers.constants import OPEN_AI_API_KEY, PATTERN, GOOGLE_SHEET_KEY
from helpers.utils import generate_response, encode_to_sheet

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

        # Only run the logic if form is submitted and there's input
        if submitted and product_info.strip():
            model = ChatOpenAI(temperature=0.7, api_key=OPEN_AI_API_KEY)  # type: ignore

            # ! this is the prompt for the product information
            product_response = generate_response(model, product_info)
            st.info(product_response)

            # ! this would be the response for getting the ICP
            raw_json_response = generate_response(
                model, f"{product_response} {PATTERN}"
            )  # type: ignore
            icp_json: dict = json.loads(raw_json_response)  # type: ignore

            if isinstance(icp_json, dict):
                st.json(icp_json)

            # ! automating google sheet encoder
            gc = gspread.service_account_from_dict(json.loads(GOOGLE_SHEET_KEY))  # type: ignore

            encode_to_sheet(icp_json, "icp", gc, "sample", "A")
            encode_to_sheet(icp_json, "icp_overview", gc, "sample", "B")
            encode_to_sheet(icp_json, "ad_concepts", gc, "sample", "C")
            encode_to_sheet(icp_json, "icp_angles", gc, "sample", "D")

        elif submitted and not product_info.strip():
            st.warning("Please enter product information before submitting.")
