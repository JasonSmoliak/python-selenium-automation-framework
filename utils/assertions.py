# -------------------------
# GENERIC ASSERTIONS
# -------------------------
def assert_true(condition, message):
    assert condition, message


def assert_false(condition, message):
    assert not condition, message


def assert_equals(actual, expected, message=None):
    assert actual == expected, (
        message or f"Expected {expected}, but got {actual}"
    )


# -------------------------
# UI ASSERTIONS
# -------------------------
def assert_text_contains(actual_text, expected_text):
    assert expected_text in actual_text, (
        f"Expected text '{expected_text}' to be in '{actual_text}'"
    )


def assert_element_visible(element):
    assert element.is_displayed(), "Expected element to be visible"


def assert_element_enabled(element):
    assert element.is_enabled(), "Expected element to be enabled"


# -------------------------
# API ASSERTIONS
# -------------------------
def assert_status_code(response, expected_code):
    actual = response.status_code
    assert actual == expected_code, (
        f"Expected status code {expected_code}, but got {actual}"
    )

def assert_header_contains(response, header_name, expected_value):
    actual_value = response.headers.get(header_name)

    assert actual_value is not None, (
        f"Expected header '{header_name}' to exist, but it was missing"
    )

    assert expected_value in actual_value, (
        f"Expected header '{header_name}' to contain '{expected_value}', "
        f"but got '{actual_value}'"
    )


def assert_empty_json_response(response):
    data = response.json()
    assert data == {}, f"Expected empty JSON response, but got {data}"


def assert_json_key(response_json, key):
    assert key in response_json, (
        f"Expected key '{key}' not found in response"
    )


def assert_json_value(response_json, key, expected_value):
    actual = response_json.get(key)
    assert actual == expected_value, (
        f"Expected '{key}' to be '{expected_value}', but got '{actual}'"
    )

# -------------------------
# SOFT ASSERTIONS
# -------------------------
class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_true(self, condition, message):
        if not condition:
            self.errors.append(message)

    def assert_equals(self, actual, expected, message=None):
        if actual != expected:
            self.errors.append(
                message or f"Expected {expected}, but got {actual}"
            )

    def assert_all(self):
        if self.errors:
            raise AssertionError("\n".join(self.errors))
