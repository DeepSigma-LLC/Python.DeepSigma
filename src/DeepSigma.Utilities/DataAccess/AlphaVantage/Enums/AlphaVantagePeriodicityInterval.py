from enum import Enum


class AlphaVantagePeriodicityInterval(Enum):
    annual = 1
    semiannual = 2
    quarterly = 4
    monthly = 12
    weekly = 52
    daily = 365
