import warnings

import featuretools as ft
import requests


def check_version():
    base_url = 'https://api.featurelabs.com/update_check/?version='
    version = ft.__version__

    # Catch requests errors
    try:
        response = requests.get(base_url + version)
    except requests.exceptions.RequestException:
        return

    # Catch invalid/missing data returned
    try:
        data = response.json()
        is_latest = data['is_latest']
        version = data['version']
    except Exception:
        return

    if not is_latest:
        msg = "Featuretools is out-of-date, latest == %s" % version
        warnings.warn(msg)
