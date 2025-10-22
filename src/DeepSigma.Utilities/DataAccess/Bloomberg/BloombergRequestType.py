from enum import Enum


class BloombergRequestType(Enum):
    DataPoint = "ReferenceDataRequest"
    Historical = "HistoricalDataRequest"
    IntradayBar = "IntradayBarRequest"
