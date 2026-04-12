from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderComponent(BasePage):
    HEADER = (By.TAG_NAME, "h1")

    @property
    def text(self):
        return self.get_text(self.HEADER)
