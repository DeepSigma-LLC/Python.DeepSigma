from enum import Enum


class PortfolioPerformanceDataField(Enum):
    Datetime = 0,
    GainLoss = 1,
    Denominator = 2,
    PortfolioReturn = 3,
    BenchmarkReturn = 4,
    UniverseReturn = 5
