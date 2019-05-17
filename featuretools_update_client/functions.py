import warnings

import featuretools as ft

from .utils import get_response_json


def initialize(version=ft.__version__):
    check_version(version)


def check_version(version=ft.__version__):
    data = get_response_json(version=version)

    try:
        is_latest = data['is_latest']
        version = data['version']

    except Exception:
        return

    if not is_latest:
        msg = "Featuretools is out-of-date, latest == %s" % version
        warnings.warn(msg)
