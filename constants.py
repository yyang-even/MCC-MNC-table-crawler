#!/usr/bin/env python3

WIKI_DOMAIN_NAME = "https://en.wikipedia.org"

SAMPLE_MAIN_HTML_FILE = "tests/data/mcc_main_page.html"

DEFAULT_OUTPUT_FILE_PATH = "/tmp/mobile_code_table.csv"

POLITE_SLEEP_SECONDS = 16

FIELD_ORDERS = ["MCC", "MNC", "Brand"]

LOWERCASE_FIELD_ORDERS = list(map(str.lower, FIELD_ORDERS))

REQUIRED_FIELDS = LOWERCASE_FIELD_ORDERS

TABLE_SIZES_OF_MAIN = [4, 72, 1]

NUMBER_SUB_LINKS = 6
