from dataclasses import dataclass


@dataclass
class MobileCodeDataEntry:
    mcc: int = 0
    mnc: int = 0
    brand: str = ""
    operator: str = ""
    status: str = ""
    bands: str = ""
    references_and_notes: str = ""
