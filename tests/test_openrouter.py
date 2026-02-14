from core.openrouter_client import chat_openrouter


def test_openrouter():
    messages = [
        {"role": "user", "content": "Say hello in one sentence."}
    ]

    response = chat_openrouter(messages)

    print("\nOpenRouter Response:")
    print(response["choices"][0]["message"]["content"])


if __name__ == "__main__":
    test_openrouter()