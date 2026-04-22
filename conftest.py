import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api_client import get
from utils.api_client import APIClient
from utils.api_helpers import assert_status, is_json
from utils.data_generator import random_post_data, seed_data
from config.settings import BROWSER, HEADLESS

# -------------------------
# UI DRIVER FIXTURE
# -------------------------
@pytest.fixture
def driver():
    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

# -------------------------
# SEEDED DATA FIXTURE
# -------------------------
@pytest.fixture
def seeded_data():
    seed_data(42)


# -------------------------
# API DATA FIXTURES
# -------------------------
@pytest.fixture
def post_one():
    response = get("/posts/1")

    assert_status(response, 200)
    assert is_json(response)

    return response.json()


@pytest.fixture
def post_by_id():
    def _get_post(post_id):
        response = get(f"/posts/{post_id}")
        assert_status(response, 200)
        assert is_json(response)
        return response.json()

    return _get_post


@pytest.fixture
def created_post():
    api = APIClient()
    data = random_post_data()

    post = api.create_post(
        title=data["title"],
        body=data["body"],
        user_id=data["userId"]
    )

    yield post

    # Cleanup pattern
    api.delete_post(post["id"])


# -------------------------
# SCREENSHOT ON FAILURE
# -------------------------
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
                extras.append(
                    pytest_html.extras.image(
                        file_name,
                        name="failure screenshot"
                    )
                )

    report.extras = extras

# -------------------------
# HTML REPORT METADATA
# -------------------------
def pytest_metadata(metadata):
    metadata.clear()  # removes defaults

    metadata["Project"] = "Selenium Framework"
    metadata["Browser"] = "Chrome"
    metadata["Test Type"] = "UI/API Automation"
