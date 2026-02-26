def test_open_example_page(driver):
    driver.get("https://example.com")
    assert "Example" in driver.title
