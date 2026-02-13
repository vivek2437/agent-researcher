from core.openrouter_client import chat_openrouter


def generate_response(system_prompt: str, user_prompt: str):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = chat_openrouter(messages)

    return response["choices"][0]["message"]["content"]
