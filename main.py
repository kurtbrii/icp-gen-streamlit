import json

import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
from langchain_openai.chat_models import ChatOpenAI
import gspread

from helpers.constants import OPEN_AI_API_KEY, PATTERN, GOOGLE_SHEET_KEY
from helpers.utils import generate_response, encode_to_sheet

st.title("Irish Ads")

if __name__ == "__main__":
    st.set_page_config(layout="wide")
