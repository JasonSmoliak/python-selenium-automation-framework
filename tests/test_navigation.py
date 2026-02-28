import pytest
from pages.example_page import ExamplePage
from pages.more_info_page import MoreInfoPage

@pytest.mark.regression
def test_page_loads_successfully(driver):
    page = ExamplePage(driver).load()

    assert page.heading_text() is not None
    assert len(page.heading_text()) > 0

@pytest.mark.regression
def test_navigation_to_more_info(driver):
    example_page = ExamplePage(driver).load()
    example_page.click_more_info()

    more_info_page = MoreInfoPage(driver)

    assert "iana" in driver.current_url.lower()
    assert more_info_page.heading_text() is not None
