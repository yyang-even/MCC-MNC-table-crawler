#!/usr/bin/env python3

import os
import sys
import unittest

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], ".."))

from mobile_code_data import MobileCodeDataEntry
import parser


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

    def test_PartialLinks(self):
        data_row_tag = parser.MakeSoup(
            """
<tr>
<td>272</td>
<td>02</td>
<td>3</td>
<td><a href="/wiki/Hutchison_3G" class="mw-redirect" title="Hutchison 3G">Hutchison 3G</a> Ireland limited</td>
<td>Operational</td>
<td>GSM 900 / GSM 1800 / UMTS 2100</td>
<td>Former <a href="/wiki/O2_(Ireland)" title="O2 (Ireland)">Telefónica O<sub>2</sub></a>
</td></tr>"""
        )
        self.assertEqual(
            MobileCodeDataEntry(
                mcc="272",
                mnc="02",
                brand="3",
                operator="Hutchison 3G Ireland limited",
                status="Operational",
                bands="GSM 900 / GSM 1800 / UMTS 2100",
                references_and_notes="Former Telefónica O2",
            ),
            parser.ToDataEntry(data_row_tag, self.HEADERS),
        )


if __name__ == "__main__":
    unittest.main()
