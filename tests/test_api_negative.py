import pytest
from utils.data_builders import PostDataBuilder


from utils.api_client import APIClient
from utils.assertions import (
    assert_equals,
    assert_empty_json_response,
    assert_header_contains,
    assert_response_time_under,
)

@pytest.mark.api
def test_get_nonexistent_post_returns_404():
    api = APIClient()

    response = api.get_post(999999)

    assert_equals(response.status_code, 404)
    assert_header_contains(response, "Content-Type", "application/json")
    assert_response_time_under(response, 2.0)
    assert_empty_json_response(response)

@pytest.mark.api
@pytest.mark.parametrize(
    "payload, expected_status",
    [
        (PostDataBuilder().without_title().build(), 201),
        (PostDataBuilder().with_empty_title().build(), 201),
        (PostDataBuilder().with_invalid_user_id().build(), 201),
    ],
)
def test_create_post_with_invalid_payload(payload, expected_status):
    api = APIClient()

    response = api.create_post_raw(payload)

    assert_equals(response.status_code, expected_status)

    data = response.json()
    assert "id" in data
