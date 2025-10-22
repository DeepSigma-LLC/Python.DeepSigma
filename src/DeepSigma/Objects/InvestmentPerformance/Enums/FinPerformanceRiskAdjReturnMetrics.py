from enum import Enum


class FinPerformanceRiskAdjReturnMetric(Enum):
    SharpeRatio = 0,
    SortinoRatio = 1,
    InformationRatio = 2,
    TreynorRatio = 3,
    JensonAlpha = 4
