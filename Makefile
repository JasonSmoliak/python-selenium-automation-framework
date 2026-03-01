test:
	python -m pytest -q

smoke:
	python -m pytest -m smoke -q

regression:
	python -m pytest -m regression -q
