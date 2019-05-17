# Featuretools Update Client
[![CircleCI](https://circleci.com/gh/FeatureLabs/featuretools_update_client/tree/master.svg?style=svg&circle-token=8f6cfba4e8f07c5602f570cf894a216ab8fedaa2)](https://circleci.com/gh/FeatureLabs/featuretools_update_client/tree/master)

## URLs
- https://api.featurelabs.com/update_check/
- https://api.featurelabs.com/update_check/?version=0.7.0
- https://api.featurelabs.com/update_check/?version=0.7.d
- https://api.featurelabs.com/update_check/?version=+
- https://api.featurelabs.com/update_check/?version=bad
- https://api.featurelabs.com/update_check/?version=0.7.0&version_featuretools_enterprise=1.4.0

## Test
First make sure all dependencies are installed
 ```shell
  make installdeps
  ```

The tests for this library include tests that use a live API as well as tests that mock the response
from the API. If changes are made to the live API or if a network connection is not available,
the tests that use the live API can fail or produce inconsistent test results.

The value of the `SKIP_REAL` variable in `test_featuretools_update_client.py`
determines which tests are run. To run all tests, including the tests that use the real API, set
`SKIP_REAL = False`. To run only the tests that use mock responses, set `SKIP_REAL = True`.

After setting `SKIP_REAL` to the desired value, run the tests with:
  ```shell
  make test
  ```

