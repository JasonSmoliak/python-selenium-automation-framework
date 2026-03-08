# Python Selenium Automation Framework

[![CI](https://github.com/JasonSmoliak/python-selenium-automation-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/JasonSmoliak/python-selenium-automation-framework/actions/workflows/ci.yml

A Python-based automation framework using Selenium and pytest that demonstrates:

• Page Object Model architecture
• UI and API test separation
• CI pipelines using GitHub Actions
• Screenshot and HTML artifact capture on failures
• Structured logging and explicit waits for stability

## Tech Stack

- Python 3.12
- Selenium WebDriver
- pytest
- webdriver-manager
- Headless Chrome support

## Key Capabilities

• Page Object Model (POM) architecture for maintainable UI tests  
• Pytest markers for running targeted suites (UI, API, smoke)  
• GitHub Actions CI pipeline running automated checks on every push  
• Automatic screenshot and HTML capture on test failures  
• Explicit waits and retry logic to reduce flaky UI tests  
• Structured logging for debugging test execution

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

## Environment Configuration

Create a `.env` file (see `.env.example`) to set environment variables locally:

- `BASE_URL` (UI target)

CI sets environment variables directly in the workflow.

## Running Tests

### Run full test suite
`make test`

### Run smoke tests (UI + API)
`make smoke`

### Run regression tests
`make regression`

### Run UI tests only
`make ui`

### Run API tests only
`make api`

### Generate HTML report
`make report`
Then open:
`open reports/report.html`

## CI (GitHub Actions)

This repository includes a GitHub Actions workflow that runs the full pytest suite automatically on every push and pull request.

## Test Organization

Tests are categorized using pytest markers:

- `smoke`: fast critical checks
- `regression`: broader suite
- `ui`: Selenium browser-based tests
- `api`: API tests using requests + schema validation

Examples:
- Run only UI tests: `make ui`
- Run only API tests: `make api`
- Run smoke suite: `make smoke`

## Reporting

HTML test reports can be generated locally using pytest-html:

- `make report`
- `open reports/report.html`

> Note: `reports/` is gitignored because reports are generated artifacts.

## Flaky Test Mitigation

UI tests may be retried on transient failures using pytest-rerunfailures (limited reruns + small delay). Retries are used as a safety net; root causes are addressed with stable locators, explicit waits, and test isolation.

## Status

Initial framework scaffold complete.
Added Page Object Model scaffold (BasePage + ExamplePage).
Currently expanding framework structure and preparing for API test layer.

