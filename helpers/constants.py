import os
import json

from dotenv import load_dotenv
import streamlit as st

from helpers.utils import get_prompt

load_dotenv(override=True)

OPEN_AI_API_KEY = st.secrets["openai_api_key"]
GOOGLE_SHEET_KEY = st.secrets["sheets_key"]
# OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY", "")
# GOOGLE_SHEET_KEY = os.getenv("GOOGLE_SHEET_KEY", "")

# ? not needed anymore
PATTERN = f"""
    {get_prompt()}
    {json.dumps(get_prompt("format.json"), indent=2, ensure_ascii=False)}

    Now that you have the product information, you need to fill ALL fields.
    There shouldn't be any empty fields.

    For the ad concepts, you need to fill in the following for each field:

    tof_advertorial_concept_1:
        concept: <concept>
        hook: <hook>
        headline: <headline>
    
    tof_advertorial_concept_2: 
        concept: <concept>
        hook: <hook>
        headline: <headline>
    
    and so on.
    
    Please ensure all JSON is properly formatted.

    Return the response in valid JSON format only, no additional text.
    """
