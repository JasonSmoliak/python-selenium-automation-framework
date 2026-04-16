from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
        self.click(self.REMOVE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(self.CHECKBOX))
        self.wait.until(EC.presence_of_element_located(self.ADD_BUTTON))

    def add_checkbox(self):
        self.click(self.ADD_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.CHECKBOX))
        self.wait.until(EC.presence_of_element_located(self.REMOVE_BUTTON))

    def enable_input(self):
        self.click(self.ENABLE_BUTTON)
        self.wait.until(
            lambda d: d.find_element(*self.INPUT_FIELD).is_enabled()
        )
        self.wait.until(EC.presence_of_element_located(self.DISABLE_BUTTON))

    def disable_input(self):
        self.click(self.DISABLE_BUTTON)
        self.wait.until(
            lambda d: not d.find_element(*self.INPUT_FIELD).is_enabled()
        )
        self.wait.until(EC.presence_of_element_located(self.ENABLE_BUTTON))

    def is_input_enabled(self):
        return self.driver.find_element(*self.INPUT_FIELD).is_enabled()

    def has_checkbox(self):
        return len(self.driver.find_elements(*self.CHECKBOX)) > 0
