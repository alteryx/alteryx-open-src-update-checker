import warnings
from unittest import TestCase, skipIf

import requests

import featuretools_update_checker
from featuretools_update_checker.utils import get_response_json

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch

# Tests that rely on a response from the real API server to pass
# may fail if the server cannot be reached. Set SKIP_REAL to False
# to run only the mocked tests and skip any tests tha rely on the
# real API server.
SKIP_REAL = False

headers = {'Testing': 'True'}


class TestFeatureToolsUpdateClient(TestCase):
    @skipIf(SKIP_REAL, 'Skipping tests that hit the real API server.')
    def test_current_version_live(self):
        # get the current featuretools version from the api
        data = get_response_json(version='0.7', headers=headers)
        version = data['version']

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(version=version,
                                                          headers=headers)
                self.assertEqual(len(w), 0)

    @skipIf(SKIP_REAL, 'Skipping tests that hit the real API server.')
    def test_old_version_live(self):
        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(version='0.7',
                                                          headers=headers)
                self.assertEqual(len(w), 1)
                assert "Featuretools is out-of-date: installed == 0.7, latest == " in str(w[-1].message)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(version='0.7.1',
                                                          headers=headers)
                self.assertEqual(len(w), 0)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(version='0.7.1',
                                                          headers=headers)
                self.assertEqual(len(w), 0)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_too_many_redirects(self, mock_get):
        mock_get.side_effect = requests.exceptions.TooManyRedirects

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(version='0.7.1',
                                                          headers=headers)
                self.assertEqual(len(w), 0)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_httperror(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(version='0.7.1',
                                                          headers=headers)
                self.assertEqual(len(w), 0)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_current_version_mock(self, mock_get):
        return_json = {"is_latest": True,
                       "upload_time": "Wed, 24 Apr 2019 15:54:56 GMT",
                       "version": "0.7.1"}
        mock_response = Mock()
        mock_response.json.return_value = return_json
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(version='0.7.1',
                                                          headers=headers)
                self.assertEqual(len(w), 0)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_old_version_mock(self, mock_get):
        return_json = {"is_latest": False,
                       "upload_time": "Wed, 24 Apr 2019 15:54:56 GMT",
                       "version": "0.7.1"}
        mock_response = Mock()
        mock_response.json.return_value = return_json
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(version='0.7',
                                                          headers=headers)
                self.assertEqual(len(w), 1)
                assert "Featuretools is out-of-date: installed == 0.7, latest == 0.7.1" == str(w[-1].message)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_ok_but_empty_response(self, mock_get):
        return_json = {}
        mock_response = Mock()
        mock_response.json.return_value = return_json
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(headers=headers)
                self.assertEqual(len(w), 0)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_bad_response(self, mock_get):
        mock_response = Mock()
        http_error = requests.exceptions.HTTPError()
        mock_response.raise_for_status.side_effect = http_error
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(headers=headers)
                self.assertEqual(len(w), 0)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_non_json_response(self, mock_get):
        mock_response = Mock()
        mock_response.content = "Text response"
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': 'TRUE'}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                featuretools_update_checker.check_version(headers=headers)
                self.assertEqual(len(w), 0)

    @patch('featuretools_update_checker.utils.requests.get')
    def test_environment_variables(self, mock_get):
        return_json = {"is_latest": False,
                       "upload_time": "Wed, 24 Apr 2019 15:54:56 GMT",
                       "version": "0.7.1"}
        mock_response = Mock()
        mock_response.json.return_value = return_json
        mock_get.return_value = mock_response

        # this test would fail unless the check is skipped by setting
        # the FEATURETOOLS_UPDATE_CHECKER environment variable to false
        for env_value in ['0', 'False', 'false', 'FALSE']:
            with patch.dict('os.environ', {'FEATURETOOLS_UPDATE_CHECKER': env_value}):
                with warnings.catch_warnings(record=True) as w:
                    warnings.simplefilter("always")
                    featuretools_update_checker.check_version(version='0.7',
                                                              headers=headers)
                    self.assertEqual(len(w), 0)
