import logging
import unittest
from scripts.module.helpers.GCSHelpers import GCSHelpers
from unittest import mock


class TestGCSHelpers(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_download_file_from_gcs_by_url(self):
        with mock.patch('scripts.module.helpers.GCSHelpers.requests.get') as mock_get:
            mock_get.return_value.status_code = 201
            with mock.patch.object(GCSHelpers, 'download_file_from_gcs_by_url', return_value=None) as modk_download_file:
                obj = GCSHelpers()
                obj.download_file_from_gcs_by_url(file_path="test.csv", url='localhos:80')
            modk_download_file.assert_called_once_with(file_path='test.csv', url='localhos:80')


if __name__ == '__main__':
    unittest.main()
