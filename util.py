import re

import constants


def ToFullWikiURLIfNecessary(short_url) -> str:
    if constants.WIKI_DOMAIN_NAME in short_url:
        return short_url
    else:
        return f"{constants.WIKI_DOMAIN_NAME}{short_url}"


def RemoveParenthesesAndWithin(a_string) -> str:
    return re.sub(r" ?\([^)]+\)", "", a_string)


def FileLength(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for i, l in enumerate(f):
            pass
    return i + 1
