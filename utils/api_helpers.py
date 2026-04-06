def assert_status(response, expected_status):
    actual_status = response.status_code
    assert actual_status == expected_status, (
        f"Expected status {expected_status}, but got {actual_status}"
    )
def is_json(response):
    content_type = response.headers.get("Content-Type", "")
    return "application/json" in content_type

def get_auth_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def log_response(response):
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response Time: {response.elapsed.total_seconds():.2f}s")
    print(f"URL: {response.url}")
