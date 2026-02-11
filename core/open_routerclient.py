import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "upstage/solar-pro-3:free"


def chat_openrouter(messages, reasoning=True):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": messages,
    }

    if reasoning:
        payload["reasoning"] = {"enabled": True}

    response = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))
    return response.json()