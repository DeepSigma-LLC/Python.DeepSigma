from enum import Enum


class SeriesCandle(Enum):
    open = "open"
    close = "close"
    high = "high"
    low = "low"
    volume = "volume"