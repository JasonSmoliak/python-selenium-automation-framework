import pytest

from api_client import get
from utils.api_helpers import assert_status

@pytest.mark.ui
def test_api_and_ui_validate_existing_post(driver, post_one):
    expected_title = post_one["title"]
    expected_body = post_one["body"]

    print("Expected title:", expected_title)
    print("Expected body:", expected_body)

    driver.get("https://jsonplaceholder.typicode.com/posts/1")

    page_source = driver.page_source.lower()
    escaped_body = expected_body.replace("\n", "\\n")

    assert expected_title.lower() in page_source, (
        f"Expected title '{expected_title}' not found in UI"
    )
    assert escaped_body.lower() in page_source, (
        "Expected body text not found in UI"
    )
