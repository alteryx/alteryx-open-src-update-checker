import requests
import warnings

import featuretools as ft


def check_version():
    base_url = 'https://api.featurelabs.com/update_check/?version='
    version = ft.__version__
    response = requests.get(base_url + version)
    data = response.json()

    if not data['is_latest']:
        msg = "Featuretools is out-of-date, latest == %s" % data['version']
        warnings.warn(msg)

    return response
