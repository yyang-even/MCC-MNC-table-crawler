# type: ignore[attr-defined]

import functools
import re
import time
from typing import Any, Callable

import constants


def ToFullWikiURLIfNecessary(short_url: str) -> str:
    if constants.WIKI_DOMAIN_NAME in short_url:
        return short_url
    else:
        return f"{constants.WIKI_DOMAIN_NAME}{short_url}"


def RemoveParenthesesAndWithin(a_string: str) -> str:
    return re.sub(r" ?\([^)]+\)", "", a_string)


def FileLength(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


def ReadWholeFile(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def PacedCall(interval_seconds: int = constants.POLITE_SLEEP_SECONDS) -> Any:
    def decorator_PacedCall(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper_PacedCall(*args: Any, **kwargs: Any) -> Callable:
            time_now_seconds = time.time()
            elapsed_seconds = time_now_seconds - wrapper_PacedCall._last_time_called
            seconds_diff = interval_seconds - elapsed_seconds

            wrapper_PacedCall._last_time_called = time_now_seconds
            if seconds_diff > 0:
                time.sleep(seconds_diff)
                wrapper_PacedCall._last_time_called = (
                    wrapper_PacedCall._last_time_called + seconds_diff
                )
            return func(*args, **kwargs)

        wrapper_PacedCall._last_time_called = 0
        return wrapper_PacedCall

    return decorator_PacedCall
