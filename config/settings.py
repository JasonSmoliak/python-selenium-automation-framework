import os


ENV = os.getenv("TEST_ENV", "dev").lower()
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"


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


SUPPORTED_BROWSERS = ["chrome", "edge"]


def validate_config():
    if ENV not in ENVIRONMENTS:
        raise ValueError(
            f"Unsupported TEST_ENV '{ENV}'. "
            f"Supported values: {list(ENVIRONMENTS.keys())}"
        )

    if BROWSER not in SUPPORTED_BROWSERS:
        raise ValueError(
            f"Unsupported BROWSER '{BROWSER}'. "
            f"Supported values: {SUPPORTED_BROWSERS}"
        )


validate_config()


API_BASE_URL = ENVIRONMENTS[ENV]["API_BASE_URL"]
UI_BASE_URL = ENVIRONMENTS[ENV]["UI_BASE_URL"]
