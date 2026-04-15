from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RadioPage(BasePage):
    URL = "https://demoqa.com/radio-button"

    YES_LABEL = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_LABEL = (By.XPATH, "//label[@for='impressiveRadio']")
    NO_INPUT = (By.ID, "noRadio")

    RESULT_TEXT = (By.CSS_SELECTOR, ".text-success")

    def load(self):
        super().load(self.URL)
        return self

    def select_yes(self):
        self.click(self.YES_LABEL)

    def select_impressive(self):
        self.click(self.IMPRESSIVE_LABEL)

    def is_no_enabled(self):
        no_radio = self.driver.find_element(*self.NO_INPUT)
        return no_radio.is_enabled()

    @property
    def selected_result(self):
        return self.get_text(self.RESULT_TEXT)
