from datetime import datetime
from typing import Dict


class BloombergHistoricalDataStructure:
    def __init__(self):
        self.ticker: str = None
        self.field: str = None
        self.data: Dict[datetime, float] = {}
        self.parsed_message: str = None
