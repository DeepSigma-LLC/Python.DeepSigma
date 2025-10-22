from src.DeepSigma.Objects.DataSeries import DataSeries
from typing import List, Union
from enum import Enum
from src.DeepSigma.Objects.DataField import DataField


class CategoricalSeries(DataSeries):
    def __init__(self, series_name: str, categorical_field_name: Union[str, Enum] = "Category",
                 field_value_name: Union[str, Enum] = "Value"):
        x_field = DataField(field_name=categorical_field_name, data_type=str)
        y_field = DataField(field_name=field_value_name, data_type=float)
        fields: List[DataField] = [x_field, y_field]
        super().__init__(series_name, fields)