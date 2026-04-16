from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"

    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILES = (By.ID, "uploaded-files")

    def load(self):
        super().load(self.URL)
        return self

    def upload_file(self, file_path):
        self.wait_for_element(self.FILE_INPUT).send_keys(file_path)

    def submit_upload(self):
        self.click(self.UPLOAD_BUTTON)

    @property
    def uploaded_filename(self):
        return self.get_text(self.UPLOADED_FILES)
