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
            sub_links = parser.ExtractMobileCodeSubLinks(main_soup)
            self.assertEqual(constants.NUMBER_SUB_LINKS, len(sub_links))


class TestPurifyHeaderName(unittest.TestCase):
    def test_AllCharsShouldBeCovertedToLowercase(self):
        self.assertEqual("mcc", parser.PurifyHeaderName("MCC"))

    def test_ParenthesesShouldBeRemoved(self):
        self.assertEqual("bands", parser.PurifyHeaderName("Bands (MHz)"))

    def test_RemainingSpacesShouldBeReplacedWithUnderscores(self):
        self.assertEqual(
            "references_and_notes", parser.PurifyHeaderName("References and notes")
        )


class TestIsMobileCodeTable(unittest.TestCase):
    def test_SameSetAsRequiredFiledsShouldReturnTrue(self):
        self.assertTrue(parser.isMobileCodeTable(constants.REQUIRED_FIELDS))

    def test_SuperSetOfRequiredFiledsShouldReturnTrue(self):
        self.assertTrue(parser.isMobileCodeTable(constants.REQUIRED_FIELDS + ["dummy"]))

    def test_SubSetOfRequiredFiledsShouldReturnFalse(self):
        self.assertFalse(parser.isMobileCodeTable(constants.REQUIRED_FIELDS[1:]))


class TestCheckAttributesAvailability(unittest.TestCase):
    def test_RaiseIfNoSuchAttribute(self):
        self.assertRaises(AttributeError, parser.CheckAttributesAvailability, ["dummy"])


class TestExtractAllMobileCodeTables(unittest.TestCase):
    def test_Sanity(self):
        with open(
            constants.SAMPLE_MAIN_HTML_FILE, "r", encoding="utf-8"
        ) as main_html_file:
            all_table_lengths = list(
                map(
                    len,
                    parser.ExtractAllMobileCodeTables(parser.MakeSoup(main_html_file)),
                )
            )
            self.assertEqual(constants.TABLE_SIZES_OF_MAIN, all_table_lengths)


if __name__ == "__main__":
    unittest.main()
