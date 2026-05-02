.PHONY: help test smoke api api-smoke ui ui-smoke regression report smoke-report parallel ui-headed ui-edge ui-edge-headed ui-staging api-staging ui-prod

PYTHON := ./venv/bin/python

help:
	@echo "Available commands:"
	@echo "  make smoke        - Run smoke tests"
	@echo "  make api          - Run API tests"
	@echo "  make ui           - Run UI tests"
	@echo "  make regression   - Run non-smoke regression tests"
	@echo "  make report       - Generate HTML test report"
	@echo "  make ui-headed    - Run UI tests in headed Chrome"
	@echo "  make ui-edge      - Run UI tests in Edge"
	@echo "  make parallel     - Run tests in parallel"

test:
	./venv/bin/python -m pytest -q

smoke:
	./venv/bin/python -m pytest -m smoke -q

workflow:
	./venv/bin/python -m pytest -m workflow -q

performance:
	./venv/bin/python -m pytest -m performance -q

regression:
	./venv/bin/python -m pytest -m regression -q

report:
	./venv/bin/python -m pytest --html=reports/report.html --self-contained-html

smoke-report:
	./venv/bin/python -m pytest -m smoke --html=reports/smoke_report.html --self-contained-html

api:
	./venv/bin/python -m pytest -m api -q

ui:
	./venv/bin/python -m pytest -m ui -q

parallel:
	./venv/bin/python -m pytest -n 4


# -------------------------
# BROWSER / ENV SHORTCUTS
# -------------------------
ui-headed:
	HEADLESS=false ./venv/bin/python -m pytest -m ui -q -s

ui-edge:
	BROWSER=edge ./venv/bin/python -m pytest -m ui -q

ui-edge-headed:
	BROWSER=edge HEADLESS=false ./venv/bin/python -m pytest -m ui -q -s

ui-staging:
	TEST_ENV=staging ./venv/bin/python -m pytest -m ui -q

api-staging:
	TEST_ENV=staging ./venv/bin/python -m pytest -m api -q

ui-prod:
	TEST_ENV=prod ./venv/bin/python -m pytest -m ui -q
