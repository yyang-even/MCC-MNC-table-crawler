#!/usr/bin/env python3

import csv
from typing import Any, List, Optional


def WriteToCsvFile(
    filepath: str,
    iterable_data: Any,
    pretty_fieldnames: str,
    lowercase_fieldnames: Optional[List[str]] = None,
) -> None:
    with open(filepath, "w", encoding="utf-8") as csv_file:
        if lowercase_fieldnames is None:
            lowercase_fieldnames = list(map(str.lower, pretty_fieldnames))

        csv_file.write(f"{','.join(pretty_fieldnames)}\n")

        csv_writer = csv.DictWriter(
            csv_file, fieldnames=lowercase_fieldnames, extrasaction="ignore"
        )
        for data in iterable_data:
            csv_writer.writerow(vars(data))
