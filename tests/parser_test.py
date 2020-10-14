#!/usr/bin/env python3
# type: ignore[attr-defined]

import os
import sys
import unittest

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], ".."))

import constants
import parser


class TestGetSubMncPageLinks(unittest.TestCase):
    def test_LengthAsExpectedUsingSampleData(self) -> None:
        with open(
            constants.SAMPLE_MAIN_HTML_FILE, "r", encoding="utf-8"
        ) as main_html_file:
            main_soup = parser.MakeSoup(main_html_file)
            sub_links = parser.ExtractMobileCodeSubLinks(main_soup)
            self.assertEqual(constants.NUMBER_SUB_LINKS, len(sub_links))


class TestPurifyHeaderName(unittest.TestCase):
    def test_AllCharsShouldBeCovertedToLowercase(self) -> None:
        self.assertEqual("mcc", parser.PurifyHeaderName("MCC"))

    def test_ParenthesesShouldBeRemoved(self) -> None:
        self.assertEqual("bands", parser.PurifyHeaderName("Bands (MHz)"))

    def test_RemainingSpacesShouldBeReplacedWithUnderscores(self) -> None:
        self.assertEqual(
            "references_and_notes", parser.PurifyHeaderName("References and notes")
        )


class TestIsMobileCodeTable(unittest.TestCase):
    def test_SameSetAsRequiredFiledsShouldReturnTrue(self) -> None:
        self.assertTrue(parser.isMobileCodeTable(constants.REQUIRED_FIELDS))

    def test_SuperSetOfRequiredFiledsShouldReturnTrue(self) -> None:
        self.assertTrue(parser.isMobileCodeTable(constants.REQUIRED_FIELDS + ["dummy"]))

    def test_SubSetOfRequiredFiledsShouldReturnFalse(self) -> None:
        self.assertFalse(parser.isMobileCodeTable(constants.REQUIRED_FIELDS[1:]))


class TestCheckAttributesAvailability(unittest.TestCase):
    def test_RaiseIfNoSuchAttribute(self) -> None:
        self.assertRaises(AttributeError, parser.CheckAttributesAvailability, ["dummy"])


class TestExtractAllMobileCodeTables(unittest.TestCase):
    def test_Sanity(self) -> None:
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
