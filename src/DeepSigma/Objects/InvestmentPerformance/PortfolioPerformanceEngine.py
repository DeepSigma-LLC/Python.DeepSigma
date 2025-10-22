from src.DeepSigma.Objects.InvestmentPerformance import PortfolioPerformanceData
from src.DeepSigma.Objects.InvestmentPerformance.Enums import PortfolioPerformanceDataField
from src.DeepSigma.Objects.InvestmentPerformance.Enums import PortfolioPerformanceDataField as FieldName
import numpy as np


class PortfolioPerformanceEngine:
    def __init__(self, performance_data: PortfolioPerformanceData):
        self.Data = performance_data
        pass

    def get_computed_cumulative_gain_loss(self) -> float:
        return sum(self.Data.get_data_by_field(FieldName.GainLoss))

    def get_computed_cumulative_return(self,
                                       field_enum: PortfolioPerformanceDataField = FieldName.PortfolioReturn) -> float:
        returns = self.Data.get_data_by_field(field_enum)
        return np.prod(1+returns)-1
