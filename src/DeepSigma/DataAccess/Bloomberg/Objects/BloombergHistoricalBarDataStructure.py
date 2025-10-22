from datetime import datetime
from src import BloombergDataBar
from typing import Dict


class BloombergHistoricalBarDataStructure:
    def __init__(self):
        self.ticker: str = None
        self.data: Dict[datetime, BloombergDataBar] = {}
        self.parsed_message: str = None
