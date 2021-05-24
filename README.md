# Featuretools Update Checker
[![CircleCI](https://circleci.com/gh/FeatureLabs/featuretools_update_checker.svg?style=svg)](https://circleci.com/gh/FeatureLabs/featuretools_update_checker)

<p align="center">
    <a href="https://github.com/FeatureLabs/featuretools_update_checker/actions/workflows/unit_tests_with_latest_deps.yml" target="_blank">
        <img src="https://github.com/FeatureLabs/featuretools_update_checker/actions/workflows/unit_tests_with_latest_deps.yml/badge.svg?branch=master" alt="Tests" />
    </a>
    <a href="https://pepy.tech/project/featuretools_update_checker" target="_blank">
        <img src="https://pepy.tech/badge/featuretools_update_checker/month" alt="PyPI Downloads" />
    </a>
</p>
<hr>

Featuretools update checker is a python library to automatically check that you have the latest version of Featuretools.
## Installation
Install with pip
```shell
python -m pip install "featuretools[update_checker]"
```

## Disable Checker
- You can disable the update checker by changing your environment variables to include the following:
```yaml
export FEATURETOOLS_UPDATE_CHECKER=False
```

## Uninstall
- To uninstall the update checker, you can do the following:
```shell
python -m pip uninstall featuretools_update_checker
```

## Feature Labs
<a href="https://www.featurelabs.com/">
    <img src="http://www.featurelabs.com/wp-content/uploads/2017/12/logo.png" alt="Featuretools" />
</a>

Featuretools update checker is an open source project created by [Feature Labs](https://www.featurelabs.com/). To see the other open source projects we're working on visit Feature Labs [Open Source](https://www.featurelabs.com/open). If building impactful data science pipelines is important to you or your business, please [get in touch](https://www.featurelabs.com/contact/).
