from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class DropdownPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dropdown"

    DROPDOWN = (By.ID, "dropdown")

    def load(self):
        super().load(self.URL)
        return self

    def select_option_by_text(self, text):
        dropdown = Select(self.wait_for_element(self.DROPDOWN))
        dropdown.select_by_visible_text(text)

    def get_selected_option(self):
        dropdown = Select(self.wait_for_element(self.DROPDOWN))
        return dropdown.first_selected_option.text
