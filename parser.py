#!/usr/bin/env python3

import re
from typing import List

from bs4 import BeautifulSoup

import constants
from mobile_code_data import MobileCodeDataEntry
import util


def MakeSoup(html):
    return BeautifulSoup(html, "html.parser")


def ExtractMobileCodeSubLinks(main_soup) -> List[str]:
    return [
        util.ToFullWikiURLIfNecessary(link_tag.get("href"))
        for link_tag in main_soup.find_all(
            "a", string=re.compile(r"^Mobile Network Codes in ITU region.*")
        )
    ]


def PurifyHeaderName(a_header_name) -> str:
    return util.RemoveParenthesesAndWithin(a_header_name).replace(" ", "_").lower()


def GetPureHeaders(header_row_tag) -> List[str]:
    return [
        PurifyHeaderName(a_header_name)
        for a_header_name in header_row_tag.stripped_strings
    ]


def isMobileCodeTable(headers) -> bool:
    return set(constants.REQUIRED_FIELDS).issubset(set(headers))


def CheckAttributesAvailability(attributes):
    for attribute_name in attributes:
        if not hasattr(MobileCodeDataEntry, attribute_name):
            raise AttributeError(attribute_name)


def ToDataEntry(data_row_tag, attributes):
    values = [data_tag.get_text().strip() for data_tag in data_row_tag.find_all("td")]
    return MobileCodeDataEntry(**dict(zip(attributes, values)))


def ExtractAllDataRows(header_row_tag, headers):
    return [
        ToDataEntry(data_row_tag, headers)
        for data_row_tag in header_row_tag.find_next_siblings("tr")
    ]


def ParseOneTable(table_tag):
    header_row_tag = table_tag.tbody.tr
    headers = GetPureHeaders(header_row_tag)

    if isMobileCodeTable(headers):
        CheckAttributesAvailability(headers)
        return ExtractAllDataRows(header_row_tag, headers)
    return []


def ExtractAllMobileCodeTables(soup):
    return [
        ParseOneTable(table_tag)
        for table_tag in soup.find_all("table", class_="wikitable")
    ]


if __name__ == "__main__":
    import pprint

    pp = pprint.PrettyPrinter(indent=4)

    with open(constants.SAMPLE_MAIN_HTML_FILE, "r", encoding="utf-8") as main_html_file:
        pp.pprint(ExtractAllMobileCodeTables(MakeSoup(main_html_file)))
