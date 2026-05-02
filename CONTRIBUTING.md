# Contributing Guide

This project demonstrates a production-style QA automation framework using Python, pytest, Selenium, and API testing.

---

## Getting Started

Clone the repository and install dependencies:

git clone <repo-url>
cd python-selenium-automation-framework
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Running Tests

make smoke        # Fast critical tests
make api          # API tests only
make ui           # UI tests only
make regression   # Full test suite (non-smoke)

Project Structure

pages/            # Page Object Model (UI)
tests/            # Test files
utils/            # Helpers, assertions, data builders
schemas/          # API schemas
config/           # Environment configuration

Adding a New API Test

1. Create or update a test in tests/
2. Use the API client:

from utils.api_client import APIClient

api = APIClient()
response = api.get_post(1)

3. Add assertions:

assert response.status_code == 200

4. Optional: validate schema

from utils.schema_validator import validate_schema

Adding a New UI Test

1. Add or update a page in pages/
2. Follow the Page Object Model pattern
3. Write a test in tests/:

@pytest.mark.ui
def test_example(driver):
    page = ExamplePage(driver).load()

Test Tagging

Use markers to control execution:

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.ui

Test Data

Use the data builder pattern:

from utils.data_builders import PostDataBuilder

data = PostDataBuilder().with_title("Custom Title").build()

CI Behavior

* Pull Requests → Smoke tests only
* Push to main → Full API + UI test suite

⸻

Guidelines

* Keep tests small and focused
* Reuse helpers and builders
* Avoid hardcoding test data
* Prefer clear assertions over complex logic

