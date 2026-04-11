import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.settings import API_BASE_URL

TIMEOUT = 5


def _build_session():
    retry_strategy = Retry(
        total=3,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST", "PUT", "DELETE"],
        backoff_factor=1,
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session


SESSION = _build_session()


def get(endpoint, headers=None):
    url = f"{API_BASE_URL}{endpoint}"
    return SESSION.get(url, headers=headers, timeout=TIMEOUT)


def post(endpoint, json=None, headers=None):
    url = f"{API_BASE_URL}{endpoint}"
    return SESSION.post(url, json=json, headers=headers, timeout=TIMEOUT)


def put(endpoint, json=None, headers=None):
    url = f"{API_BASE_URL}{endpoint}"
    return SESSION.put(url, json=json, headers=headers, timeout=TIMEOUT)


def delete(endpoint, headers=None):
    url = f"{API_BASE_URL}{endpoint}"
    return SESSION.delete(url, headers=headers, timeout=TIMEOUT)
