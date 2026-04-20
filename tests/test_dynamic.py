import pytest
from pages.dynamic_page import DynamicPage


@pytest.mark.ui
def test_remove_and_add_checkbox(driver):
    page = DynamicPage(driver).load()

    # Remove checkbox
    page.remove_checkbox()
    assert not page.has_checkbox(), "Expected checkbox to be removed, but it is still present"

    # Add checkbox back
    page.add_checkbox()
    assert page.has_checkbox(), (
    f"Expected checkbox to be present, but actual state was: {page.has_checkbox()}"
    )

@pytest.mark.ui
def test_enable_and_disable_input(driver):
    page = DynamicPage(driver).load()

    # Enable input
    page.enable_input()
    assert page.is_input_enabled(), (
    f"Expected input field to be enabled after clicking Enable, "
    f"but actual state was: {page.is_input_enabled()}"
    )

    # Disable input
    page.disable_input()
    assert not page.is_input_enabled(), "Expected input field to be disabled after clicking Disable"
