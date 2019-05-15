from unittest import TestCase

import featuretools_update_client


class TestFeatureToolsUpdateClient(TestCase):
    def test_regular(self):
        r = featuretools_update_client.check_version()
        self.assertEqual(r.status_code, 200)
        self.assertTrue("is_latest" in r.text)
