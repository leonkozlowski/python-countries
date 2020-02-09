.PHONY: black
black:
	tox -e black

.PHONY: tests
tests:
	tox

.PHONY: lint
lint:
	tox -e pylint

.PHONY: flake
flake:
	tox -e flake8

.PHONY: clean
clean:
	rm -rf build
	rm -rf doc/build