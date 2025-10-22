from src.MetaKit.Objects.ChartObjects.ChartAxes import ChartAxes
from src.MetaKit.Objects.ChartObjects.ChartConfig import ChartConfig
from src.MetaKit.Objects.ChartObjects.ChartSeries import *
from typing import List


class ChartGroup(ChartConfig):
    def __init__(self, title: str, x_axes: ChartAxes, y_axes: ChartAxes, y2_axes: ChartAxes = ChartAxes) -> None:
        self._data: List[ChartSeries] = []
        super().__init__(title, x_axes, y_axes, y2_axes)

    def add_series(self, series: ChartSeries) -> None:
        """
        Adds a series to the series group.
        :param series:
        :return:
        """
        self._data.append(series)

    def get_all_series(self) -> List[ChartSeries]:
        """
        Returns a list of all data series within the series group.
        :return:
        """
        return self._data

    def get_series_by_index(self, index: int) -> ChartSeries:
        """
        Returns series by index.
        :param index:
        :return:
        """
        return self._data[index]

    def remove_series_by_name(self, series_name: str):
        self._data = [x for x in self._data if x.data_series.get_series_name() != series_name]


    def has_y2_axis(self) -> bool:
        for series in self._data:
            if series.use_y2:
                return True
        return False

    def get_labels_for_all_series_in_order(self):
        return [series.data_series.get_series_name() for series in self._data]
