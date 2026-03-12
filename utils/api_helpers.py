def assert_status(response, expected_status):
    actual_status = response.status_code
    assert actual_status == expected_status, (
        f"Expected status {expected_status}, but got {actual_status}"
    )
