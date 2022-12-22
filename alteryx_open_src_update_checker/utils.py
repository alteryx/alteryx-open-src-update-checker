from importlib import import_module

import requests

from alteryx_open_src_update_checker.settings import BASE_URL


def get_response_json(library="featuretools", version=None, headers={}):
    try:
        lib = import_module(library)
    except Exception:
        return

    if version is None:
        version = lib.__version__
    try:
        response = requests.get(
            BASE_URL + "?library={}&version={}".format(library, version),
            headers=headers,
        ).json()
    except Exception:
        return None

    return response
