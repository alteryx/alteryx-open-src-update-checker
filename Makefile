.PHONY: clean
clean:
	find . -name '*.pyo' -delete
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	find . -name '*~' -delete
	find . -name '.coverage.*' -delete

.PHONY: lint
lint:
	black . --preview --check
	ruff .

.PHONY: lint-fix
lint-fix:
	black . --preview
	ruff . --fix

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
	$(eval PACKAGE=$(shell python -c 'import setuptools; setuptools.setup()' --version))
	tar -zxvf "dist/alteryx_open_src_update_checker-${PACKAGE}.tar.gz"
	mv "alteryx_open_src_update_checker-${PACKAGE}" unpacked_sdist
