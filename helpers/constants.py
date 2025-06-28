import os
import json

from dotenv import load_dotenv

from helpers.utils import get_prompt

load_dotenv(override=True)

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY", "")

PATTERN = f"""
    {get_prompt()}
    {json.dumps(get_prompt("format.json"), indent=2)}

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


    and so on. concept, hook, headline are strings separated by a new line, not json objects.

    return the response in json format and formatted on the screen
    """
