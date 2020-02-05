#!/usr/bin/env python3

import itertools
import re
from typing import List

from bs4 import BeautifulSoup
from bs4 import SoupStrainer

import constants
from mobile_code_data import MobileCodeDataEntry
import util


def MakeSoup(html):
    return BeautifulSoup(html, "html.parser")


def MakeFineSoup(html):
    return BeautifulSoup(
        html, "html.parser", parse_only=SoupStrainer("table", class_="wikitable")
    )


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
    return list(map(PurifyHeaderName, header_row_tag.stripped_strings))


def isMobileCodeTable(headers) -> bool:
    return set(constants.REQUIRED_FIELDS).issubset(set(headers))


def CheckAttributesAvailability(attributes):
    for attribute_name in attributes:
        if not hasattr(MobileCodeDataEntry, attribute_name):
            raise AttributeError(attribute_name)


def ToDataEntry(data_row_tag, attributes):
    values = [data_tag.get_text().strip() for data_tag in data_row_tag.find_all("td")]
    return MobileCodeDataEntry(**dict(zip(attributes, values)))


def ExtractAllDataRows(header_row_tag, headers) -> List[MobileCodeDataEntry]:
    return [
        ToDataEntry(data_row_tag, headers)
        for data_row_tag in header_row_tag.find_next_siblings("tr")
    ]


def ParseOneTable(table_tag) -> List[MobileCodeDataEntry]:
    header_row_tag = table_tag.tbody.tr
    headers = GetPureHeaders(header_row_tag)

    if isMobileCodeTable(headers):
        CheckAttributesAvailability(headers)
        return ExtractAllDataRows(header_row_tag, headers)
    return []


def ExtractAllMobileCodeTables(soup) -> List[List[MobileCodeDataEntry]]:
    return list(
        itertools.filterfalse(
            lambda l: not l,
            map(ParseOneTable, soup.find_all("table", class_="wikitable")),
        )
    )


if __name__ == "__main__":
    import pprint

    import formatter

    pp = pprint.PrettyPrinter(indent=4)

    with open(constants.SAMPLE_MAIN_HTML_FILE, "r", encoding="utf-8") as main_html_file:
        mobile_code_tables = ExtractAllMobileCodeTables(MakeSoup(main_html_file))
        pp.pprint(mobile_code_tables)

        formatter.WriteToCsvFile(
            "/tmp/mcc_main_table.csv",
            itertools.chain.from_iterable(mobile_code_tables),
            constants.FIELD_ORDERS,
            constants.LOWERCASE_FIELD_ORDERS,
        )
