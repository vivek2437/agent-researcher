import requests


def search_web(query: str):
    url = "https://duckduckgo.com/html/"
    params = {"q": query}

    response = requests.get(url, params=params)
    return response.text
