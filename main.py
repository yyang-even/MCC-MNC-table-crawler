#!/usr/bin/env python3

import itertools

import formatter
import parser
import requester


if __name__ == "__main__":
    MCC_Main_Page_URL = util.ToFullWikiURLIfNecessary("/wiki/Mobile_country_code")

    main_page_content = requester.GetPageContentWithLogging(MCC_Main_Page_URL)

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
        "/tmp/mobile_code_table.csv",
        itertools.chain.from_iterable(all_data),
        constants.FIELD_ORDERS,
        constants.LOWERCASE_FIELD_ORDERS,
    )
