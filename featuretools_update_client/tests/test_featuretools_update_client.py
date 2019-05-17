import warnings
from unittest import TestCase, skipIf
from unittest.mock import Mock, patch

import requests

import featuretools_update_client
from featuretools_update_client.utils import get_response_json

try:
    from unittest.mock import Mock, patch
except ImportError:
    import mock as Mock
    from mock import patch



# Tests that rely on a response from the real API server to pass
# may fail if the server cannot be reached. Set SKIP_REAL to False
# to run only the mocked tests and skip any tests tha rely on the
# real API server.
SKIP_REAL = False


class TestFeatureToolsUpdateClient(TestCase):
    @skipIf(SKIP_REAL, 'Skipping tests that hit the real API server.')
    def test_current_version_live(self):
        # get the current featuretools version from the api
        data = get_response_json(version='0.7')
        version = data['version']

        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version(version=version)
            self.assertEqual(len(w), 0)

    @skipIf(SKIP_REAL, 'Skipping tests that hit the real API server.')
    def test_old_version_live(self):
        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version(version='0.7')
            self.assertEqual(len(w), 1)
            assert "Featuretools is out-of-date, latest ==" in str(w[-1].message)

    @patch('featuretools_update_client.utils.requests.get')
    def test_current_version_mock(self, mock_get):
        return_json = {"is_latest": True,
                       "upload_time": "Wed, 24 Apr 2019 15:54:56 GMT",
                       "version": "0.7.1"}
        mock_response = Mock()
        mock_response.json.return_value = return_json
        mock_get.return_value = mock_response

        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version(version='0.7.1')
            self.assertEqual(len(w), 0)

    @patch('featuretools_update_client.utils.requests.get')
    def test_old_version_mock(self, mock_get):
        return_json = {"is_latest": False,
                       "upload_time": "Wed, 24 Apr 2019 15:54:56 GMT",
                       "version": "0.7.1"}
        mock_response = Mock()
        mock_response.json.return_value = return_json
        mock_get.return_value = mock_response

        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version(version='0.7')
            self.assertEqual(len(w), 1)
            assert "Featuretools is out-of-date, latest ==" in str(w[-1].message)

    @patch('featuretools_update_client.utils.requests.get')
    def test_ok_but_empty_response(self, mock_get):
        return_json = {}
        mock_response = Mock()
        mock_response.json.return_value = return_json
        mock_get.return_value = mock_response

        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version()
            self.assertEqual(len(w), 0)

    @patch('featuretools_update_client.utils.requests.get')
    def test_bad_response(self, mock_get):
        mock_response = Mock()
        http_error = requests.exceptions.HTTPError()
        mock_response.raise_for_status.side_effect = http_error
        mock_get.return_value = mock_response

        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version()
            self.assertEqual(len(w), 0)

    @patch('featuretools_update_client.utils.requests.get')
    def test_non_json_response(self, mock_get):
        mock_response = Mock()
        mock_response.content = "Text response"
        mock_get.return_value = mock_response

        with warnings.catch_warnings(record=True) as w:
            featuretools_update_client.check_version()
            self.assertEqual(len(w), 0)
