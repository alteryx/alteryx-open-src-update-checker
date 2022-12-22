.PHONY: clean
clean:
	find . -name '*.pyo' -delete
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	find . -name '*~' -delete
	find . -name '.coverage.*' -delete

.PHONY: lint
lint:
	isort --check-only alteryx_open_src_update_checker
	black alteryx_open_src_update_checker -t py311 --check
	ruff alteryx_open_src_update_checker/

.PHONY: lint-fix
lint-fix:
	black alteryx_open_src_update_checker -t py311
	isort alteryx_open_src_update_checker

.PHONY: test
test: lint
	pytest -s -vv -x -n auto alteryx_open_src_update_checker/tests

.PHONY: testcoverage
testcoverage: lint
	pytest -s -vv -x -n auto alteryx_open_src_update_checker/tests --cov=alteryx_open_src_update_checker

.PHONY: installdeps
installdeps:
	pip install -e ".[dev]"
	pre-commit install

.PHONY: upgradepip
upgradepip:
	python -m pip install --upgrade pip

.PHONY: upgradebuild
upgradebuild:
	python -m pip install --upgrade build

.PHONY: upgradesetuptools
upgradesetuptools:
	python -m pip install --upgrade setuptools

.PHONY: package
package: upgradepip upgradebuild upgradesetuptools
	python -m build
	$(eval PACKAGE=$(shell python -c "from pep517.meta import load; metadata = load('.'); print(metadata.version)"))
	tar -zxvf "dist/alteryx_open_src_update_checker-${PACKAGE}.tar.gz"
	mv "alteryx_open_src_update_checker-${PACKAGE}" unpacked_sdist
