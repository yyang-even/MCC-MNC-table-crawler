#!/usr/bin/env python3

import os
import sys
import unittest

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], ".."))

import constants
import parser


class TestGetSubMncPageLinks(unittest.TestCase):
    def test_LengthAsExpectedUsingSampleData(self):
        with open(
            constants.SAMPLE_MAIN_HTML_FILE, "r", encoding="utf-8"
        ) as main_html_file:
            main_soup = parser.MakeSoup(main_html_file)
            sub_links = parser.GetSubMncPageLinks(main_soup)
            self.assertEqual(6, len(sub_links))


if __name__ == "__main__":
    unittest.main()
