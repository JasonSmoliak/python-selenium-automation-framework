import pytest
from api_client import get
from jsonschema import validate
from schemas.post_schema import POST_SCHEMA


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize("endpoint, expected_status", [
    ("/posts/1", 200),
])
def test_example_api_success(endpoint, expected_status):
    response = get(endpoint)

    assert response.status_code == expected_status
    data = response.json()

    validate(instance=data, schema=POST_SCHEMA)

@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status", [
    ("/posts/999999", 404),
])
def test_example_api_negative(endpoint, expected_status):
    response = get(endpoint)

    assert response.status_code == expected_status
