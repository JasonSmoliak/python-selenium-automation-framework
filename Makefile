.PHONY: test smoke workflow performance regression report smoke-report api ui parallel \
        ui-headed ui-edge ui-edge-headed ui-staging api-staging ui-prod

PYTHON := ./venv/bin/python

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
