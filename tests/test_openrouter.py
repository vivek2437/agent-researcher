from core.openrouter_client import chat_openrouter

messages = [{"role": "user", "content": "Hello AI"}]
print(chat_openrouter(messages))