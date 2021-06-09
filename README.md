# Alteryx Open Source Update Checker
<p align="center">
    <a href="https://github.com/FeatureLabs/alteryx-open-src-update-checker/actions/workflows/unit_tests_with_latest_deps.yml" target="_blank">
        <img src="https://github.com/FeatureLabs/alteryx-open-src-update-checker/actions/workflows/unit_tests_with_latest_deps.yml/badge.svg?branch=master" alt="Tests" />
    </a>
    <a href="https://pepy.tech/project/alteryx_open_src_update_checker" target="_blank">
        <img src="https://pepy.tech/badge/alteryx_open_src_update_checker/month" alt="PyPI Downloads" />
    </a>
</p>
<hr>

Alteryx open source update checker is a Python library to automatically check that you have the latest version of an Alteryx open source library. If your Alteryx open source library is out of date, a warning to upgrade will be shown. 

## Installation

- Install with pip (as an add-on to Alteryx open source libraries):
```shell
python -m pip install "featuretools[update_checker]"
python -m pip install "evalml[update_checker]"
python -m pip install "woodwork[update_checker]"
python -m pip install "compose[update_checker]"
```

## Disable Checker
- You can disable the update checker by changing your environment variables to include the following:
```yaml
export ALTERYX_OPEN_SRC_UPDATE_CHECKER=False
```

## Uninstall
- To uninstall the update checker, you can do the following:
```shell
python -m pip uninstall alteryx_open_src_update_checker
```

## Built at Alteryx Innovation Labs

<a href="https://www.alteryx.com/innovation-labs">
    <img src="https://evalml-web-images.s3.amazonaws.com/alteryx_innovation_labs.png" alt="Alteryx Innovation Labs" />
</a>

