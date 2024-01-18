build:
	rm -rf dist/*
	-pipx uninstall cirq-py
	poetry build -v
	pipx install dist/cirq_py-0.1.0-py3-none-any.whl --force

run:
	poetry run python -m cirq ${A}

test:
	pytest tests/test_cirq.py