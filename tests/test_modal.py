import pytest
from pages.modal_page import ModalPage


@pytest.mark.ui
def test_modal_appears_on_page_load(driver):
    page = ModalPage(driver).load()

    page.wait_for_modal()

    title = page.modal_title_text
    print("Modal title:", title)

    assert title is not None
    assert len(title) > 0


@pytest.mark.ui
def test_modal_can_be_closed(driver):
    page = ModalPage(driver).load()

    page.wait_for_modal()
    page.close_modal()

    heading = page.page_heading_text
    print("Page heading:", heading)

    assert heading == "Entry Ad"
