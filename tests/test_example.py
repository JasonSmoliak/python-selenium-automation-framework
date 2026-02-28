import pytest
from pages.example_page import ExamplePage


@pytest.mark.smoke
@pytest.mark.parametrize(
    "expected_heading, expected_url_fragment",
    [
        ("Example Domain", "example"),
        ("Example Domain", "example"),
    ],
)
def test_open_example_page(driver, expected_heading, expected_url_fragment):
    page = ExamplePage(driver).load()

    assert page.heading_text() == expected_heading
    assert expected_url_fragment in driver.current_url.lower()
