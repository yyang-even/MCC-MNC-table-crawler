#!/usr/bin/env python3
# type: ignore[attr-defined]

import requests

import util


@util.PacedCall()
def GetPageContentWithLogging(URL: str) -> str:
    response = requests.get(URL, allow_redirects=True)
    print(
        f"Page Request '{URL}': Status({response.status_code}), Content Type({response.headers['content-type']}), Encoding({response.encoding})"
    )
    response.raise_for_status()

    return response.text


if __name__ == "__main__":
    MCC_Main_Page_URL = util.ToFullWikiURLIfNecessary("/wiki/Mobile_country_code")
    main_page_content = GetPageContentWithLogging(MCC_Main_Page_URL)
    with open("/tmp/mcc_main_page.html", "w", encoding="utf-8") as main_page_file:
        main_page_file.write(main_page_content)
