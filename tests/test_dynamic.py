import pytest
from pages.dynamic_page import DynamicPage
from utils.assertions import assert_true, assert_false

def remove_checkbox(self):
    self.log_info("Clicking Remove button")
    self.click(self.REMOVE_BUTTON)

    self.log_info("Waiting for checkbox to disappear")
    self.wait_until_not_visible(self.CHECKBOX)

    self.log_pass("Checkbox removed successfully")

    self.log_info("Waiting for Add button to appear")
    self.wait_until_present(self.ADD_BUTTON)


def add_checkbox(self):
    self.log_info("Clicking Add button")
    self.click(self.ADD_BUTTON)

    self.log_info("Waiting for checkbox to appear")
    self.wait_until_present(self.CHECKBOX)

    self.log_pass("Checkbox added successfully")


def enable_input(self):
    self.log_info("Clicking Enable button")
    self.click(self.ENABLE_BUTTON)

    self.log_info("Waiting for input to become enabled")
    self.wait_until_enabled(self.INPUT_FIELD)

    self.log_pass("Input enabled successfully")


def disable_input(self):
    self.log_info("Clicking Disable button")
    self.click(self.DISABLE_BUTTON)

    self.log_info("Waiting for input to become disabled")
    self.wait_until_disabled(self.INPUT_FIELD)

    self.log_pass("Input disabled successfully")


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
