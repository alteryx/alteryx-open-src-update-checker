import warnings
from unittest import TestCase

import featuretools_update_client


class TestFeatureToolsUpdateClient(TestCase):
    def test_old_version(self):
        with warnings.catch_warnings(record=True) as w:
            # Trigger a warning
            featuretools_update_client.check_version()
            # Verify proper warning was displayed
            assert "Featuretools is out-of-date, latest ==" in str(w[-1].message)
