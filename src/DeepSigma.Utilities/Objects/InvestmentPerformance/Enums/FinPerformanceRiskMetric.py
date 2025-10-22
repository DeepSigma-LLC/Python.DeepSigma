from enum import Enum


class FinPerformanceRiskMetric(Enum):
    Beta = 0
    ExcessReturn = 1,
    TrackingError = 2,
    StandardDeviation = 3,
    DrawDown = 4,
    DrawDownObservationDuration = 5
    UlcerIndex = 6,

