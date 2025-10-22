from src.MetaKit.Objects.DataSeries.Enums.TimeSeriesPurpose import TimeSeriesPurpose
from src.MetaKit.Objects.DataSeries.DataSeries import DataSeries
from typing import  List, Union
from enum import Enum
from datetime import datetime
from src.MetaKit.Objects.DataField import DataField


class TimeSeries(DataSeries):
    _time_series_purpose = TimeSeriesPurpose.unclassified

    def __init__(self, series_name: str, date_field_name: Union[str, Enum] = "Date",
                 value_field_name: Union[str, Enum] = "Value", time_series_purpose = TimeSeriesPurpose.unclassified):
        x_field = DataField(field_name=date_field_name, data_type=datetime)
        y_field = DataField(field_name=value_field_name, data_type=float)
        fields: List[DataField] = [x_field, y_field]
        super().__init__(series_name, fields)
        self._series_purpose: TimeSeriesPurpose = time_series_purpose

    def get_time_series_purpose(self) -> TimeSeriesPurpose:
        """
        Gets time series purpose.
        :return:
        """
        return self._series_purpose
