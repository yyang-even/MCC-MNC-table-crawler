#!/usr/bin/env python3

import os
import sys
import unittest
from unittest.mock import patch
from unittest.mock import Mock

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], ".."))

import constants
import main
import util


class TestMain(unittest.TestCase):
    def setUp(self):
        try:
            os.remove(constants.DEFAULT_OUTPUT_FILE_PATH)
        except:
            pass

    @patch("main.requester.GetPageContentWithLogging", autospec=True)
    def test_Sanity(self, mock_html_getter):
        mock_html_getter.return_value = util.ReadWholeFile(
            constants.SAMPLE_MAIN_HTML_FILE
        )
        main.MainCSV()
        self.assertTrue(os.path.isfile(constants.DEFAULT_OUTPUT_FILE_PATH))
        number_data_lines = sum(constants.TABLE_SIZES_OF_MAIN) * (
            constants.NUMBER_SUB_LINKS + 1
        )
        self.assertEqual(
            number_data_lines + 1, util.FileLength(constants.DEFAULT_OUTPUT_FILE_PATH)
        )


if __name__ == "__main__":
    unittest.main()
