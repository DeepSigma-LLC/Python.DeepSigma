from src import ChartCoordinateSystemType
from src import ChartGridlineType
from src import ChartAxes
from typing import List, Tuple, Optional
from src import ChartSeries


class Chart:
    def __init__(self, chart_title: str, show_legend: bool = False, show_gridlines: bool = False,
                 gridline_type: ChartGridlineType = ChartGridlineType.Both,
                 chart_coordinate_system: ChartCoordinateSystemType = ChartCoordinateSystemType.Cartesian,
                 is_three_dimensional: bool = False) -> None:
        self.__chart_coordinate_system_type: ChartCoordinateSystemType = chart_coordinate_system
        self.__chart_title: str = chart_title
        self.__show_gridlines: bool = show_gridlines
        self.__gridline_type: ChartGridlineType = gridline_type
        self.__show_legend: bool = show_legend
        self.__three_dimensional: bool = is_three_dimensional
        self.shared_x_axis_grid_location: Optional[Tuple[int, int]] = None
        self.shared_y_axis_grid_location: Optional[Tuple[int, int]] = None

        self.__data_series: List[ChartSeries] = []

        self.x_axis: ChartAxes = ChartAxes("x-axis")
        self.y_axis: ChartAxes = ChartAxes("y-axis")
        self.y_secondary_axis: ChartAxes = ChartAxes("y-secondary-axis")
        self.z_axis: ChartAxes = ChartAxes("z-axis")

    def add_series(self, series: ChartSeries) -> None:
        self.__data_series.append(series)

    def get_all_series(self) -> List[ChartSeries]:
        return self.__data_series

    def get_chart_title(self) -> str:
        return self.__chart_title

    def get_show_gridlines(self) -> bool:
        return self.__show_gridlines

    def set_gridlines_show(self, gridlines_show: bool) -> None:
        self.__show_gridlines = gridlines_show

    def get_gridline_type(self) -> ChartGridlineType:
        return self.__gridline_type

    def get_show_legend(self) -> bool:
        return self.__show_legend

    def get_three_dimensional(self) -> bool:
        return self.__three_dimensional

    def get_coordinate_system_type(self) -> ChartCoordinateSystemType:
        return self.__chart_coordinate_system_type

    def get_is_three_dimensional(self) -> bool:
        return self.__three_dimensional

    def set_is_three_dimensional(self, is_three_dimensional: bool) -> None:
        self.__three_dimensional = is_three_dimensional

    def set_shared_x_axis_grid_location(self, column_index: int, row_index: int) -> None:
        self.shared_x_axis_grid_location = (row_index, column_index)

    def set_shared_y_axis_grid_location(self, column_index: int, row_index: int) -> None:
        self.shared_y_axis_grid_location = (row_index, column_index)

    def get_shared_x_axis_grid_location(self) -> Tuple[int, int]:
        return self.shared_x_axis_grid_location

    def get_shared_y_axis_grid_location(self) -> Tuple[int, int]:
        return self.shared_y_axis_grid_location

    def get_has_secondary_y_axis(self) -> bool:
        for series in self.__data_series:
            if series.use_y_secondary:
                return True
        return False

