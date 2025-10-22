

class BloombergDataPointStructure:
    def __init__(self):
        self.ticker: str = None
        self.field: str = None
        self.value: str = None
        self.parsed_message: str = None
