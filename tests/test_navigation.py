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

@pytest.mark.ui
def test_ui_with_api_backed_expected_data(driver, post_one_data):
    page = ExamplePage(driver).load()

    title = page.get_title()
    header_text = page.heading_text

    print(f"UI title: {title}")
    print(f"UI header: {header_text}")
    print(f"API post id: {post_one_data['id']}")
    print(f"API userId: {post_one_data['userId']}")

    assert title is not None, "Page title is None"
    assert len(title) > 0, "Page title is empty"
    assert header_text == "Example Domain", (
        f"Expected 'Example Domain', got '{header_text}'"
    )

    assert post_one_data["id"] == 1, (
        f"Expected API id 1, got {post_one_data['id']}"
    )

@pytest.mark.ui
@pytest.mark.workflow
def test_example_to_more_info_workflow(driver):
    example_page = ExamplePage(driver).load()

    print(f"Starting URL: {driver.current_url}")
    print(f"Starting header: {example_page.heading_text}")

    assert example_page.heading_text == "Example Domain", (
        f"Expected 'Example Domain', got '{example_page.heading_text}'"
    )

    more_info_page = example_page.click_more_info()

    print(f"Final URL: {driver.current_url}")
    print(f"Final header: {more_info_page.heading_text}")

    assert "iana" in driver.current_url.lower(), (
        f"Expected URL to contain 'iana', got '{driver.current_url}'"
    )
    assert more_info_page.heading_text is not None, "More info page header is None"
    assert len(more_info_page.heading_text) > 0, "More info page header is empty"
