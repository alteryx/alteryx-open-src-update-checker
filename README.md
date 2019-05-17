# Featuretools Update Checker
[![CircleCI](https://circleci.com/gh/FeatureLabs/featuretools_update_client/tree/master.svg?style=svg&circle-token=8f6cfba4e8f07c5602f570cf894a216ab8fedaa2)](https://circleci.com/gh/FeatureLabs/featuretools_update_client/tree/master)

Featuretools Update Checker is a python library to automatically check that you have the latest version of Featuretools.
## Installation
Install with pip

	python -m pip install featuretools
 
## Example
Below is an example of using the Update Checker
```python
import featuretools as ft 
> Featuretools is out-of-date, latest == 0.7.1
```
- The update checker uses an entrypoint of featuretools so it will run everytime you import featuretools.
- The update checker will siliently finish if it detects no response from the server, or timeouts.
- The update checker will check asynchronously and not slow down your code.


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

## Disable Checker
- You can easily disable to update checker by changing your environment variables to include the following:
```yaml
FEATURETOOLS_UPDATE_CHECKER=False
```
## Feature Labs
<a href="https://www.featurelabs.com/">
    <img src="http://www.featurelabs.com/wp-content/uploads/2017/12/logo.png" alt="Featuretools" />
</a>

Featuretools Update Checker is an open source project created by [Feature Labs](https://www.featurelabs.com/). To see the other open source projects we're working on visit Feature Labs [Open Source](https://www.featurelabs.com/open). If building impactful data science pipelines is important to you or your business, please [get in touch](https://www.featurelabs.com/contact/).


