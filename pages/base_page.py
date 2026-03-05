from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)
        return self

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def click(self, locator):
    	logger.info(f"Clicking element: {locator}")
    	element = self.driver.find_element(*locator)
    	element.click()

    def get_text(self, locator):
        element = self.find(locator)
        return element.text

    def get_text(self, locator):
    	logger.info(f"Getting text from element: {locator}")
    	element = self.driver.find_element(*locator)
    	return element.text
