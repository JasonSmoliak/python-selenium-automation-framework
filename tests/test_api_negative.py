import pytest

from utils.api_client import APIClient
from utils.assertions import assert_equals


@pytest.mark.api
def test_get_nonexistent_post_returns_404():
    api = APIClient()

    response = api.get_post(999999)

    assert_equals(response.status_code, 404)
