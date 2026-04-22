import os

ENV = os.getenv("TEST_ENV", "dev")

ENVIRONMENTS = {
    "dev": {
        "API_BASE_URL": "https://jsonplaceholder.typicode.com",
        "UI_BASE_URL": "https://example.com",
    },
    "staging": {
        "API_BASE_URL": "https://jsonplaceholder.typicode.com",
        "UI_BASE_URL": "https://example.com",
    },
    "prod": {
        "API_BASE_URL": "https://jsonplaceholder.typicode.com",
        "UI_BASE_URL": "https://example.com",
    },
}

API_BASE_URL = ENVIRONMENTS[ENV]["API_BASE_URL"]
UI_BASE_URL = ENVIRONMENTS[ENV]["UI_BASE_URL"]

BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
