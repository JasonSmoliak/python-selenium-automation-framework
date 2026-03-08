import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()

import os
import re
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only capture artifacts when the test body fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if not driver:
            return

        try:
            os.makedirs("screenshots", exist_ok=True)

            # sanitize test name for filesystem
            safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)

            screenshot_path = os.path.join("screenshots", f"{safe_name}.png")
            html_path = os.path.join("screenshots", f"{safe_name}.html")

            # save screenshot
            driver.save_screenshot(screenshot_path)

            # save page HTML
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(driver.page_source)

        except Exception:
            # never let artifact capture break CI
            pass
