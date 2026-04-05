import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get(endpoint, headers=None):
    url = f"{BASE_URL}{endpoint}"
    return requests.get(url, headers=headers)


def post(endpoint, json=None, headers=None):
    url = f"{BASE_URL}{endpoint}"
    return requests.post(url, json=json, headers=headers)
