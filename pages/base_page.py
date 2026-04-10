from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
