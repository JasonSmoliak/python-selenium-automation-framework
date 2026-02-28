from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import BASE_URL


class ExamplePage(BasePage):
    H1 = (By.TAG_NAME, "h1")
    MORE_INFO_LINK = (By.CSS_SELECTOR, "a")
    
    def load(self):
        self.open(BASE_URL)
        return self

    def heading_text(self) -> str:
        return self.get_text(self.H1)

    def click_more_info(self):
        self.click(self.MORE_INFO_LINK)
        return self
