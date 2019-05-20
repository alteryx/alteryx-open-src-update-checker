import os
import warnings
from threading import Thread

import featuretools as ft

from .utils import get_response_json

warnings.simplefilter("always")


def initialize():
    bg_thread = Thread(target=check_version)
    bg_thread.start()


def check_version(version=ft.__version__, headers={}):
    ft_update_check = os.environ.get('FEATURETOOLS_UPDATE_CHECKER', True)

    if ft_update_check in ['0', 'False', 'false', 'FALSE']:
        return
    else:
        data = get_response_json(version=version, headers=headers)

        try:
            is_latest = data['is_latest']
            version = data['version']

        except Exception:
            return

        if not is_latest:
            msg = "Featuretools is out-of-date, latest == %s" % version
            warnings.warn(msg)
