#!/usr/bin/env python3
# type: ignore[attr-defined]

import itertools
import pprint
from typing import Any

import constants
import formatter
import parser
import requester
import util


def GetDataIterable(main_url: str) -> Any:
    main_page_content = requester.GetPageContentWithLogging(main_url)

    main_soup = parser.MakeSoup(main_page_content)
    sub_soups = map(
        parser.MakeFineSoup,
        map(
            requester.GetPageContentWithLogging,
            parser.ExtractMobileCodeSubLinks(main_soup),
        ),
    )
    all_soups = itertools.chain([main_soup], sub_soups)

    all_data = map(
        itertools.chain.from_iterable, map(parser.ExtractAllMobileCodeTables, all_soups)
    )

    return itertools.chain.from_iterable(all_data)


def MainCSV(
    main_url: str = util.ToFullWikiURLIfNecessary("/wiki/Mobile_country_code"),
) -> None:
    formatter.WriteToCsvFile(
        constants.DEFAULT_OUTPUT_FILE_PATH,
        GetDataIterable(main_url),
        constants.FIELD_ORDERS,
        constants.LOWERCASE_FIELD_ORDERS,
    )


def MainPrettyPrint(
    main_url: str = util.ToFullWikiURLIfNecessary("/wiki/Mobile_country_code"),
) -> None:
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(list(GetDataIterable(main_url)))


if __name__ == "__main__":
    MainCSV()
