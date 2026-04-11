import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api_client import get
from utils.api_helpers import assert_status, is_json


# -------------------------
# UI DRIVER FIXTURE
# -------------------------
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


# -------------------------
# API DATA FIXTURE
# -------------------------
@pytest.fixture
def post_one_data():
    response = get("/posts/1")

    assert_status(response, 200)
    assert is_json(response)

    return response.json()
