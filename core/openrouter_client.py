import requests
import json
from core.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    MODEL_NAME
)


def chat_openrouter(messages, reasoning=True):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
    }

    if reasoning:
        payload["reasoning"] = {"enabled": True}

    response = requests.post(
        OPENROUTER_BASE_URL,
        headers=headers,
        data=json.dumps(payload),
        timeout=60
    )

    response.raise_for_status()
    return response.json()
