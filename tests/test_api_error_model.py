import pytest

from schemas.error_schema import ERROR_SCHEMA
from utils.schema_validator import validate_schema
from utils.assertions import assert_equals, assert_true


@pytest.mark.api
def test_simulated_error_response_matches_schema():
    error_response = {
        "error": "Invalid request",
        "code": 400,
        "details": [
            "title is required",
            "userId must be an integer",
        ],
    }

    validate_schema(error_response, ERROR_SCHEMA)

    assert_equals(error_response["code"], 400)
    assert_true(
        "title is required" in error_response["details"],
        "Expected error details to include missing title validation"
    )
