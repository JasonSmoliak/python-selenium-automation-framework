import pytest
from pages.checkbox_page import CheckboxPage


@pytest.mark.ui
def test_check_checkbox(driver):
    page = CheckboxPage(driver).load()

    page.check_checkbox(0)

    assert page.is_checked(0) is True


@pytest.mark.ui
def test_uncheck_checkbox(driver):
    page = CheckboxPage(driver).load()

    page.uncheck_checkbox(1)

    assert page.is_checked(1) is False

@pytest.mark.ui
def test_toggle_checkbox(driver):
    page = CheckboxPage(driver).load()

    initial_state = page.is_checked(0)

    # Toggle it
    page.get_checkboxes()[0].click()

    new_state = page.is_checked(0)

    print(f"Initial: {initial_state}, New: {new_state}")

    assert initial_state != new_state
