import warnings
from unittest import TestCase

import requests

import featuretools_update_client


class TestFeatureToolsUpdateClient(TestCase):
    def test_current_version(self):
        # get the current featuretools version from the api
        r = requests.get('https://api.featurelabs.com/update_check/?version=0.7')
        version = r.json()['version']

        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version(version=version)
            self.assertEqual(len(w), 0)

    def test_old_version(self):
        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version(version='0.7')
            self.assertEqual(len(w), 1)
            assert "Featuretools is out-of-date, latest ==" in str(w[-1].message)
