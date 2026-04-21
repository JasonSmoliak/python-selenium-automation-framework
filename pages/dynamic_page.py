from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DynamicPage(BasePage):
    URL = "https://practice.expandtesting.com/dynamic-controls"

    REMOVE_BUTTON = (By.XPATH, "//button[normalize-space()='Remove']")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    ENABLE_BUTTON = (By.XPATH, "//button[normalize-space()='Enable']")
    DISABLE_BUTTON = (By.XPATH, "//button[normalize-space()='Disable']")
    INPUT_FIELD = (By.CSS_SELECTOR, "input[type='text']")

    def load(self):
        super().load(self.URL)
        return self

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

    def is_input_enabled(self):
        return self.driver.find_element(*self.INPUT_FIELD).is_enabled()

    def has_checkbox(self):
        return len(self.driver.find_elements(*self.CHECKBOX)) > 0

    def remove_and_restore_checkbox(self):
        self.remove_checkbox()
        self.add_checkbox()

    def enable_and_disable_input(self):
        self.enable_input()
        self.disable_input()
