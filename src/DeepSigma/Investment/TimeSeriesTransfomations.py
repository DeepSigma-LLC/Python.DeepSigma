from src.DeepSigma.Objects.DataSeries import DataSeries
from typing import Dict

class TimeSeriesTransformations:

    @staticmethod
    def get_daily_returns(data_series: DataSeries) -> Dict:
        raise NotImplementedError()
        return {}

    @staticmethod
    def get_cumulative_return(data_series: DataSeries) -> Dict:
        starting_value = data_series.get_data()[0]
        new_values: Dict = {}
        for key in data_series.get_data().keys():
            new_values[key] = data_series.get_data()[key] / starting_value - 1
        return new_values