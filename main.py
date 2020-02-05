#!/usr/bin/env python3

import itertools

import constants
import formatter
import parser
import requester
import util


def Main(main_url=util.ToFullWikiURLIfNecessary("/wiki/Mobile_country_code")):
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

    formatter.WriteToCsvFile(
        constants.DEFAULT_OUTPUT_FILE_PATH,
        itertools.chain.from_iterable(all_data),
        constants.FIELD_ORDERS,
        constants.LOWERCASE_FIELD_ORDERS,
    )


if __name__ == "__main__":
    Main()
