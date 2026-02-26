# Python Selenium Automation Framework

A lightweight Selenium automation framework built using Python and pytest.

## Tech Stack

- Python 3.12
- Selenium WebDriver
- pytest
- webdriver-manager
- Headless Chrome support

## Project Structure

```
python-selenium-automation-framework/
│
├── pages/                 # Page Object classes
├── tests/                 # Test files
├── conftest.py            # Pytest fixtures (WebDriver setup)
├── pyproject.toml         # Pytest configuration
├── requirements.txt       # Dependencies
└── README.md
```

## Features

- Reusable WebDriver fixture
- Headless execution ready for CI
- Page Object Model implementation
- Clean pytest structure

## How to Run

```bash
python -m pytest
```

## Status

Initial framework scaffold complete.
Added Page Object Model scaffold (BasePage + ExamplePage).
Currently expanding framework structure and preparing for API test layer.

