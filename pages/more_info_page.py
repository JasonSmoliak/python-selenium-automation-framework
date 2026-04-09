from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MoreInfoPage:
    HEADING = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def heading_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HEADING)
        ).text
