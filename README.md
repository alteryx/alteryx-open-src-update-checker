# Featuretools Update Checker

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

## Built at Alteryx Innovation Labs

<a href="https://www.alteryx.com/innovation-labs">
    <img src="https://evalml-web-images.s3.amazonaws.com/alteryx_innovation_labs.png" alt="Alteryx Innovation Labs" />
</a>

