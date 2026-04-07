PYTHON := ./venv/bin/python

test:
	$(PYTHON) -m pytest -q

smoke:
	$(PYTHON) -m pytest -m smoke -q

workflow:
	$(PYTHON) -m pytest -m workflow -q

performance:
	$(PYTHON) -m pytest -m performance -q

regression:
	$(PYTHON) -m pytest -m regression -q

report:
	$(PYTHON) -m pytest --html=reports/report.html --self-contained-html

smoke-report:
	$(PYTHON) -m pytest -m smoke --html=reports/smoke_report.html --self-contained-html

api:
	$(PYTHON) -m pytest -m api -q

ui:
	$(PYTHON) -m pytest -m ui -q

parallel:
	$(PYTHON) -m pytest -n 4
