WIKI_DOMAIN_NAME = "https://en.wikipedia.org"

SAMPLE_MAIN_HTML_FILE = "tests/data/mcc_main_page.html"

POLITE_SLEEP_SECONDS = 16

FIELD_ORDERS = ["MCC", "MNC", "Brand"]

LOWERCASE_FIELD_ORDERS = [field.lower() for field in FIELD_ORDERS]

REQUIRED_FIELDS = LOWERCASE_FIELD_ORDERS
