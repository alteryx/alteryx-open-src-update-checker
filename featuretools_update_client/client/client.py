import json
import warnings

import featuretools as ft
import requests


def initialize():
    host = 'https://api.featurelabs.com'
    url = host + '/update_check/?version=' + ft.__version__
    r = requests.get(url)
    data = json.loads(r.content.decode('utf-8'))
    if data['is_latest'] is False:
        msg = "Featuretools is out-of-date, latest == %s" % data['version']
        warnings.warn(msg)
    return
