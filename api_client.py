import requests


BASE_API_URL = "https://jsonplaceholder.typicode.com"


def get(endpoint: str):
    return requests.get(f"{BASE_API_URL}{endpoint}")
