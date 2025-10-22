from enum import Enum


class BloombergPeriodicity(Enum):
    Daily = "DAILY"
    Weekly = "WEEKLY"
    Monthly = "MONTHLY"
    Quarterly = "QUARTERLY"
    SemiAnnual = "SEMI_ANNUALLY"
    Annual = "YEARLY"
