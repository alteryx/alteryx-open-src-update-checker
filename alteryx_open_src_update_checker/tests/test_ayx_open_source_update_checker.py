import warnings

import pytest
import requests

import alteryx_open_src_update_checker
from alteryx_open_src_update_checker.utils import get_response_json

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch

# Tests that rely on a response from the real API server to pass
# may fail if the server cannot be reached. Set SKIP_REAL to False
# to run only the mocked tests and skip any tests tha rely on the
# real API server.
SKIP_REAL = False
skip_real = pytest.mark.skipif(
    SKIP_REAL,
    reason="Skipping tests that hit the real API server",
)

headers = {"Testing": "True"}

libraries = ["featuretools", "evalml", "woodwork", "composeml"]


@pytest.fixture(params=libraries)
def library(request):
    return request.param


@skip_real
def test_default():
    data = get_response_json(headers=headers)
    assert data["library"] == "featuretools"
    version = data["version"]

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                version=version,
                headers=headers,
            )
            assert len(w) == 0


@skip_real
def test_current_version_live(library):
    data = get_response_json(library=library, headers=headers)
    version = data["version"]

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                version=version,
                headers=headers,
            )
            assert len(w) == 0


@skip_real
def test_old_version_live(library):
    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                version="0.0.1",
                headers=headers,
            )
            print(library)
            assert len(w) == 1
            assert "{} is out-of-date: installed == 0.0.1, latest == ".format(
                library,
            ) in str(w[-1].message)


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_timeout(mock_get, library):
    mock_get.side_effect = requests.exceptions.Timeout

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                version="0.0.1",
                headers=headers,
            )
            assert len(w) == 0


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_connection_error(mock_get, library):
    mock_get.side_effect = requests.exceptions.ConnectionError

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                version="0.0.1",
                headers=headers,
            )
            assert len(w) == 0


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_too_many_redirects(mock_get, library):
    mock_get.side_effect = requests.exceptions.TooManyRedirects

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                version="0.0.1",
                headers=headers,
            )
            assert len(w) == 0


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_httperror(mock_get, library):
    mock_get.side_effect = requests.exceptions.HTTPError

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                version="0.0.1",
                headers=headers,
            )
            assert len(w) == 0


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_current_version_mock(mock_get, library):
    return_json = {
        "is_latest": True,
        "upload_time": "Wed, 24 Apr 2019 15:54:56 GMT",
        "version": "0.0.1",
    }
    mock_response = Mock()
    mock_response.json.return_value = return_json
    mock_get.return_value = mock_response

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                version="0.0.1",
                headers=headers,
            )
            assert len(w) == 0


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_old_version_mock(mock_get, library):
    return_json = {
        "is_latest": False,
        "upload_time": "Wed, 24 Apr 2019 15:54:56 GMT",
        "version": "0.7.1",
    }
    mock_response = Mock()
    mock_response.json.return_value = return_json
    mock_get.return_value = mock_response

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                version="0.0.1",
                headers=headers,
            )
            assert len(w) == 1
            assert "{} is out-of-date: installed == 0.0.1, latest == 0.7.1".format(
                library,
            ) == str(w[-1].message)


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_ok_but_empty_response(mock_get, library):
    return_json = {}
    mock_response = Mock()
    mock_response.json.return_value = return_json
    mock_get.return_value = mock_response

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                headers=headers,
            )
            assert len(w) == 0


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_bad_response(mock_get, library):
    mock_response = Mock()
    http_error = requests.exceptions.HTTPError()
    mock_response.raise_for_status.side_effect = http_error
    mock_get.return_value = mock_response

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                headers=headers,
            )
            assert len(w) == 0


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_non_json_response(mock_get, library):
    mock_response = Mock()
    mock_response.content = "Text response"
    mock_get.return_value = mock_response

    with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": "TRUE"}):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            alteryx_open_src_update_checker.check_version(
                library=library,
                headers=headers,
            )
            assert len(w) == 0


@patch("alteryx_open_src_update_checker.utils.requests.get")
def test_environment_variables(mock_get, library):
    return_json = {
        "is_latest": False,
        "upload_time": "Wed, 24 Apr 2019 15:54:56 GMT",
        "version": "0.7.1",
    }
    mock_response = Mock()
    mock_response.json.return_value = return_json
    mock_get.return_value = mock_response

    # this test would fail unless the check is skipped by setting
    # the alteryx_open_src_update_checker environment variable to false
    for env_value in ["0", "False", "false", "FALSE"]:
        with patch.dict("os.environ", {"ALTERYX_OPEN_SRC_UPDATE_CHECKER": env_value}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                alteryx_open_src_update_checker.check_version(
                    library=library,
                    version="0.0.1",
                    headers=headers,
                )
                assert len(w) == 0
