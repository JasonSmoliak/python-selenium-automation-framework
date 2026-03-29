test:
	python -m pytest -q

smoke:
	python -m pytest -m smoke -q

regression:
	python -m pytest -m regression -q

report:
	python -m pytest --html=reports/report.html --self-contained-html

smoke-report:
	python -m pytest -m smoke --html=reports/smoke_report.html --self-contained-html

api:
	./venv/bin/python -m pytest -m api -q

ui:
	./venv/bin/python -m pytest -m ui -q

parallel:
	python -m pytest -n 4
