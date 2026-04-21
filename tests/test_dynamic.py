import pytest
from pages.dynamic_page import DynamicPage
from utils.assertions import assert_true, assert_false

@pytest.mark.ui
def test_remove_and_add_checkbox(driver):
    print("\n[TEST] Starting remove/add checkbox workflow")
    page = DynamicPage(driver).load()

    page.remove_checkbox()
    assert not page.has_checkbox(), (
        f"Expected checkbox to be removed, but actual state was: {page.has_checkbox()}"
    )

    page.add_checkbox()
    assert_true(
    page.has_checkbox(),
    f"Expected checkbox to be present, but actual state was: {page.has_checkbox()}"
    )

@pytest.mark.ui
def test_enable_and_disable_input(driver):
    print("\n[TEST] Starting enable/disable input workflow")
    page = DynamicPage(driver).load()

    page.enable_input()
    assert page.is_input_enabled(), (
        f"Expected input field to be enabled after clicking Enable, "
        f"but actual state was: {page.is_input_enabled()}"
    )

    page.disable_input()
    assert_false(
    page.is_input_enabled(),
    f"Expected input to be disabled, but actual state was: {page.is_input_enabled()}"
    )

@pytest.mark.ui
def test_checkbox_workflow(driver):
    print("\n[TEST] Starting checkbox workflow")
    page = DynamicPage(driver).load()

    page.remove_and_restore_checkbox()

    assert page.has_checkbox(), (
        f"Expected checkbox to be present after remove/restore workflow, "
        f"but actual state was: {page.has_checkbox()}"
    )


@pytest.mark.ui
def test_input_workflow(driver):
    print("\n[TEST] Starting input workflow")
    page = DynamicPage(driver).load()

    page.enable_and_disable_input()

    assert not page.is_input_enabled(), (
        f"Expected input field to be disabled after enable/disable workflow, "
        f"but actual state was: {page.is_input_enabled()}"
    )
