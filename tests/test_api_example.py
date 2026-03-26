import pytest
from api_client import get
from jsonschema import validate
from schemas.post_schema import POST_SCHEMA
from test_data.api_data import API_SUCCESS_CASES, API_NEGATIVE_CASES
from utils.api_helpers import assert_status, is_json

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize("endpoint, expected_status", API_SUCCESS_CASES)
def test_example_api_success(endpoint, expected_status):
    response = get(endpoint)

    assert_status(response, expected_status)
    assert is_json(response)
    
    data = response.json()

    validate(instance=data, schema=POST_SCHEMA)

@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status", API_NEGATIVE_CASES)
def test_example_api_negative(endpoint, expected_status):
    response = get(endpoint)

    assert_status(response, expected_status)

@pytest.mark.api
def test_api_response_contains_expected_fields():
    response = get("/posts/1")

    assert_status(response, 200)
    assert is_json(response)

    data = response.json()

    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert data["id"] == 1
