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

import os
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots/ui/failures", exist_ok=True)
            file_name = f"screenshots/ui/failures/{item.name}.png"

            driver.save_screenshot(file_name)
            print(f"\nSaved screenshot: {file_name}")

            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extras.append(pytest_html.extras.image(file_name, name="failure screenshot"))

    report.extras = extras
