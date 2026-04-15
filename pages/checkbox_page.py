from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckboxPage(BasePage):
    URL = "https://the-internet.herokuapp.com/checkboxes"

    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def load(self):
        super().load(self.URL)
        return self

    def get_checkboxes(self):
        return self.get_elements(self.CHECKBOXES)

    def check_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if not checkboxes[index].is_selected():
            checkboxes[index].click()

    def uncheck_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if checkboxes[index].is_selected():
            checkboxes[index].click()

    def is_checked(self, index):
        return self.get_checkboxes()[index].is_selected()
