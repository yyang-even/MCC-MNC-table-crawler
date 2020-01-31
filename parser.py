#!/usr/bin/env python3

import re
from typing import List

from bs4 import BeautifulSoup

import constants


def MakeSoup(html_text):
    return BeautifulSoup(html_text, "html.parser")


def GetSubMncPageLinks(main_soup) -> List[str]:
    return [
        link.get("href")
        for link in main_soup.find_all(
            "a", string=re.compile(r"^Mobile Network Codes in ITU region.*")
        )
    ]


if __name__ == "__main__":
    with open(constants.SAMPLE_MAIN_HTML_FILE, "r", encoding="utf-8") as main_html_file:
        main_soup = MakeSoup(main_html_file)
        GetSubMncPageLinks(main_soup)
