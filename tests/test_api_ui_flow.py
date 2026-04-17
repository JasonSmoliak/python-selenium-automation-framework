import pytest

from api_client import get
from utils.api_helpers import assert_status


@pytest.mark.ui
@pytest.mark.parametrize(
    "post_id",
    [
        pytest.param(1, id="post-1"),
        pytest.param(2, id="post-2"),
        pytest.param(3, id="post-3"),
    ],
)
def test_api_and_ui_validate_existing_post(driver, post_by_id, post_id):
    post = post_by_id(post_id)

    expected_title = post["title"]
    expected_body = post["body"]

    print("Post ID:", post_id)
    print("Expected title:", expected_title)
    print("Expected body:", expected_body)

    driver.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

    page_source = driver.page_source.lower()
    escaped_body = expected_body.replace("\n", "\\n")

    assert expected_title.lower() in page_source, (
        f"Expected title '{expected_title}' not found in UI for post {post_id}"
    )
    assert escaped_body.lower() in page_source, (
        f"Expected body text not found in UI for post {post_id}"
    )
