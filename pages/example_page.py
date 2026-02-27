from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ExamplePage(BasePage):
    URL = "https://example.com"
    H1 = (By.TAG_NAME, "h1")

    def load(self):
        self.open(self.URL)
        return self

    def heading_text(self) -> str:
        return self.get_text(self.H1)	
