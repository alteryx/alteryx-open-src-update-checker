import featuretools as ft
import requests

from .settings import BASE_URL


def get_response_json(version=ft.__version__, headers={}):
    try:
        response = requests.get(BASE_URL + '?version=' + version,
                                headers=headers).json()
    except Exception:
        return None

    return response
