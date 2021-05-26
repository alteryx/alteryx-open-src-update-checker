.PHONY: clean
clean:
	find . -name '*.pyo' -delete
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	find . -name '*~' -delete

.PHONY: lint
lint:
	flake8 alteryx_open_src_update_checker && isort --check-only --recursive alteryx_open_src_update_checker

.PHONY: lint-fix
lint-fix:
	autopep8 --in-place --recursive --max-line-length=100 --select="E225,E303,E302,E203,E128,E231,E251,E271,E127,E126,E301,W291,W293,E226,E306,E221" alteryx_open_src_update_checker
	isort --recursive alteryx_open_src_update_checker

.PHONY: test
test: lint
	pytest -s -vv -x alteryx_open_src_update_checker/tests

.PHONY: testcoverage
testcoverage: lint
	pytest -s -vv -x alteryx_open_src_update_checker/tests --cov=alteryx_open_src_update_checker

.PHONY: installdeps
installdeps:
	pip install --upgrade pip
	pip install -e .
	pip install -r dev-requirements.txt

.PHONY: package_alteryx_open_src_update_checker
package_alteryx_open_src_update_checker:
	python setup.py sdist
	$(eval ALTERYX_OPEN_SRC_UPDATE_CHECKER_VERSION=$(shell python setup.py --version))
	tar -zxvf "dist/alteryx_open_src_update_checker-${ALTERYX_OPEN_SRC_UPDATE_CHECKER_VERSION}.tar.gz"
	mv "alteryx_open_src_update_checker-${ALTERYX_OPEN_SRC_UPDATE_CHECKER_VERSION}" unpacked_sdist
