#!/usr/bin/env python3

import itertools
import os
import sys
import tempfile
import unittest

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], ".."))

import constants
import formatter
from mobile_code_data import MobileCodeDataEntry
import util


class TestWriteToCsvFile(unittest.TestCase):
    def setUp(self):
        self.NUMBER_OF_DATA = 5

    def test_Sanity(self):
        with tempfile.TemporaryDirectory() as tmp_dir_name:
            csv_file_path = os.path.join(tmp_dir_name, "formatter_sanity_test.csv")
            formatter.WriteToCsvFile(
                csv_file_path,
                itertools.repeat(MobileCodeDataEntry(), self.NUMBER_OF_DATA),
                constants.FIELD_ORDERS,
            )

            self.assertTrue(os.path.isfile(csv_file_path))
            self.assertEqual(self.NUMBER_OF_DATA + 1, util.FileLength(csv_file_path))


if __name__ == "__main__":
    unittest.main()
