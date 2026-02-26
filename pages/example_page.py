from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ExamplePage(BasePage):
    URL = "https://example.com"
    H1 = (By.TAG_NAME, "h1")

    def load(self):
        self.open(self.URL)
        return self

    def heading_text(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located(self.H1)
        )
        return element.text

