import os
import warnings
from importlib import import_module
from threading import Thread

from .utils import get_response_json


def initialize(library='featuretools'):
    bg_thread = Thread(target=check_version, kwargs={'library': library})
    bg_thread.start()


def check_version(library='featuretools', version=None, headers={}):
    update_check = os.environ.get('ALTERYX_OPEN_SRC_UPDATE_CHECKER', True)

    # Use append=False when setting simplefilter so we know filter gets added
    # to the start of the filters list and we can remove later with pop
    warnings.simplefilter('ignore', append=False)
    try:
        lib = import_module(library)
    except Exception:
        return
    warnings.filters.pop(0)
    if version is None:
        version = lib.__version__

    if update_check in ['0', 'False', 'false', 'FALSE']:
        return

    data = get_response_json(library=library, version=version, headers=headers)

    try:
        is_latest = data['is_latest']
        latest_version = data['version']

    except Exception:
        return

    if not is_latest:
        msg = "%s is out-of-date: installed == %s, latest == %s" % (library, version, latest_version)
        # Use append=False when setting simplefilter so we know filter gets added
        # to the start of the filters list and we can remove later with pop
        warnings.simplefilter('always', append=False)
        warnings.warn(msg)
        warnings.filters.pop(0)
