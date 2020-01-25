#!/usr/bin/env python3

import requests


class NotOK(Exception):
    pass


def GetPageContentWithLogging(URL) -> str:
    response = requests.get(URL)
    print(
        f"Page Request '{URL}': Status({response.status_code}), Content Type({response.headers['content-type']}), Encoding({response.encoding})"
    )
    if response.status_code != 200:
        raise NotOK
    return response.content.decode(response.encoding)


if __name__ == "__main__":
    MCC_Main_Page_URL = "https://en.wikipedia.org/wiki/Mobile_country_code"
    main_page_content = GetPageContentWithLogging(MCC_Main_Page_URL)
    with open("/tmp/mcc_main_page.html", "w", encoding="utf-8") as main_page_file:
        main_page_file.write(main_page_content)
