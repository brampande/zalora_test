import logging
import unittest
from scripts.module.bitcoin_data_transformation import BitcoinDataTransformation
from unittest import mock


class TestTransformBitcoinData(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_transform_data(self):
        with mock.patch('scripts.module.bitcoin_data_transformation'):
            with mock.patch.object(BitcoinDataTransformation, 'transform_data', return_value=None) as mock_transform:
                obj = BitcoinDataTransformation(csv_file='bitcoin.csv')
                obj.transform_data(output_file_location='result.csv')
            mock_transform.assert_called_once_with(output_file_location='result.csv')


if __name__ == '__main__':
    unittest.main()
