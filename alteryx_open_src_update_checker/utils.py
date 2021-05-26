import requests
from importlib import import_module

from .settings import BASE_URL


def get_response_json(library='featuretools', version=None, headers={}):
    lib = import_module(library)
    if version is None:
        version = lib.__version__
    try:
        response = requests.get(BASE_URL + '?library=' + library + '&version=' + version,
                                headers=headers).json()
    except Exception:
        return None

    return response
