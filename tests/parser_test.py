#!/usr/bin/env python3

import os
import sys
import unittest

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], ".."))

import constants
from mobile_code_data import MobileCodeDataEntry
import parser


class TestGetSubMncPageLinks(unittest.TestCase):
    def test_LengthAsExpectedUsingSampleData(self):
        with open(
            constants.SAMPLE_MAIN_HTML_FILE, "r", encoding="utf-8"
        ) as main_html_file:
            main_soup = parser.MakeSoup(main_html_file)
            sub_links = parser.ExtractMobileCodeSubLinks(main_soup)
            self.assertEqual(6, len(sub_links))


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
            self.assertEqual([4, 72, 1], all_table_lengths)


class TestToDataEntry(unittest.TestCase):
    def setUp(self):
        self.HEADERS = [
            "mcc",
            "mnc",
            "brand",
            "operator",
            "status",
            "bands",
            "references_and_notes",
        ]

    def test_DataOneLessThanHeaders(self):
        data_row_tag = parser.MakeSoup(
            """
<tr>
<td>001</td>
<td>01</td>
<td>TEST</td>
<td>Test Network</td>
<td>Operational</td>
<td>any</td>
<td>
</td></tr>"""
        )
        self.assertEqual(
            MobileCodeDataEntry(
                mcc="001",
                mnc="01",
                brand="TEST",
                operator="Test Network",
                status="Operational",
                bands="any",
                references_and_notes="",
            ),
            parser.ToDataEntry(data_row_tag, self.HEADERS),
        )

    def test_EmptyBrand(self):
        data_row_tag = parser.MakeSoup(
            """
<tr>
<td>901</td>
<td>02</td>
<td></td>
<td><i>Unassigned</i></td>
<td>Returned spare</td>
<td>Unknown</td>
<td>Formerly: Sense Communications International
</td></tr>"""
        )
        self.assertEqual(
            MobileCodeDataEntry(
                mcc="901",
                mnc="02",
                brand="",
                operator="Unassigned",
                status="Returned spare",
                bands="Unknown",
                references_and_notes="Formerly: Sense Communications International",
            ),
            parser.ToDataEntry(data_row_tag, self.HEADERS),
        )

    def test_ContainsLinks(self):
        data_row_tag = parser.MakeSoup(
            """
<tr>
<td>901</td>
<td>01</td>
<td>ICO</td>
<td><a href="/wiki/ICO_Satellite_Management" class="mw-redirect" title="ICO Satellite Management">ICO Satellite Management</a></td>
<td>Not operational</td>
<td>Satellite</td>
<td>MNC withdrawn<sup id="cite_ref-itu_ob_1091_5-0" class="reference"><a href="#cite_note-itu_ob_1091-5">[5]</a></sup>
</td></tr>"""
        )
        self.assertEqual(
            MobileCodeDataEntry(
                mcc="901",
                mnc="01",
                brand="ICO",
                operator="ICO Satellite Management",
                status="Not operational",
                bands="Satellite",
                references_and_notes="MNC withdrawn[5]",
            ),
            parser.ToDataEntry(data_row_tag, self.HEADERS),
        )


if __name__ == "__main__":
    unittest.main()
