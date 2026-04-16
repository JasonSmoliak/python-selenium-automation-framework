import os
import pytest

from pages.upload_page import UploadPage


@pytest.mark.ui
def test_file_upload(driver):
    page = UploadPage(driver).load()

    file_path = os.path.abspath("test_data/uploads/sample_upload.txt")

    print("Uploading file:", file_path)

    page.upload_file(file_path)
    page.submit_upload()

    uploaded_name = page.uploaded_filename

    print("Uploaded filename:", uploaded_name)

    assert uploaded_name == "sample_upload.txt", (
        f"Expected 'sample_upload.txt', got '{uploaded_name}'"
    )
