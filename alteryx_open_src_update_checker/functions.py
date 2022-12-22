import os
import warnings
from importlib import import_module
from threading import Thread

from alteryx_open_src_update_checker.utils import get_response_json


def initialize(library="featuretools"):
    bg_thread = Thread(target=check_version, kwargs={"library": library})
    bg_thread.start()


def check_version(library="featuretools", version=None, headers={}):
    update_check = os.environ.get("ALTERYX_OPEN_SRC_UPDATE_CHECKER", True)
    try:
        lib = import_module(library)
    except Exception:
        return

    if version is None:
        version = lib.__version__

    if update_check in ["0", "False", "false", "FALSE"]:
        return

    data = get_response_json(library=library, version=version, headers=headers)

    try:
        is_latest = data["is_latest"]
        latest_version = data["version"]

    except Exception:
        return

    if not is_latest:
        msg = "%s is out-of-date: installed == %s, latest == %s" % (
            library,
            version,
            latest_version,
        )
        warnings.warn(msg)
