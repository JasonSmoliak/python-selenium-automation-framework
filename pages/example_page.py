from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.more_info_page import MoreInfoPage


class ExamplePage:
    URL = "https://example.com"

    HEADING = (By.TAG_NAME, "h1")
    MORE_INFO_LINK = (By.CSS_SELECTOR, "a")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.URL)
        return self

    @property
    def heading_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HEADING)
        ).text

    def get_title(self):
        return self.driver.title

    def get_header_text(self):
        return self.heading_text

    def click_more_info(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MORE_INFO_LINK)
        ).click()
        return MoreInfoPage(self.driver)
