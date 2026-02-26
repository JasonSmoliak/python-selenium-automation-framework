from pages.example_page import ExamplePage


def test_open_example_page(driver):
    page = ExamplePage(driver).load()
    assert page.heading_text() == "Example Domain"

