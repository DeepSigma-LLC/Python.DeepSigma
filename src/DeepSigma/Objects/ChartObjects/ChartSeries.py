from enum import Enum
from src.DeepSigma.Objects.ChartObjects.Enums.ChartType import ChartType
from src.DeepSigma.Objects.DataSeries.DataSeries import DataSeries


class ChartSeries:
    def __init__(self, chart_type: ChartType, data_series: DataSeries, x_field: Enum, y_field: Enum, z_field: Enum = None,
                 use_y_secondary_axis: bool = False, color: str = "blue") -> None:
        self.__chart_type: ChartType = chart_type
        self.data_series: DataSeries = data_series
        self.x_field: Enum = x_field
        self.y_field: Enum = y_field
        self.z_field: Enum = z_field
        self.use_y_secondary: bool = use_y_secondary_axis
        self.color: str = color

    def get_chart_type(self) -> ChartType:
        return self.__chart_type

    def get_color(self) -> str:
        return self.color