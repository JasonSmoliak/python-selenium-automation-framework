import pytest
from pages.example_page import ExamplePage
from pages.more_info_page import MoreInfoPage


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_page_loads_successfully(driver):
    page = ExamplePage(driver).load()

    assert page.heading_text is not None
    assert len(page.heading_text) > 0


@pytest.mark.ui
@pytest.mark.regression
def test_navigation_to_more_info(driver):
    example_page = ExamplePage(driver).load()
    more_info_page = example_page.click_more_info()

    assert "iana" in driver.current_url.lower()
    assert more_info_page.heading_text is not None


@pytest.mark.ui
def test_homepage_title_and_header(driver):
    page = ExamplePage(driver).load()

    title = page.get_title()
    header_text = page.heading_text

    print(f"Page title: {title}")
    print(f"Header text: {header_text}")

    assert title is not None, "Page title is None"
    assert len(title) > 0, "Page title is empty"
    assert header_text == "Example Domain", (
        f"Expected 'Example Domain', got '{header_text}'"
    )
