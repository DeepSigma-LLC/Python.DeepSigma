from src import ChartAxes


class ChartConfig:
    def __init__(self, chart_title: str = "", x_axes: ChartAxes = ChartAxes, y_axes: ChartAxes = ChartAxes,
                 y2_axes: ChartAxes = None, show_legend: bool = False) -> None:
        self.__chart_title: str = chart_title
        self.__x_axes: ChartAxes = x_axes
        self.__y_axes: ChartAxes = y_axes
        self.__y2_axes: ChartAxes = y2_axes
        self.__show_legend: bool = show_legend

    def get_chart_title(self) -> str:
        return self.__chart_title

    def set_chart_title(self, chart_title: str) -> None:
        self.__chart_title = chart_title

    def get_x_axes(self) -> ChartAxes:
        return self.__x_axes

    def set_x_axes(self, x_axes: ChartAxes) -> None:
        self.__x_axes = x_axes

    def get_y_axes(self) -> ChartAxes:
        return self.__y_axes

    def set_y_axes(self, y_axes: ChartAxes) -> None:
        self.__y_axes = y_axes

    def get_y2_axes(self) -> ChartAxes:
        return self.__y2_axes

    def set_y2_axes(self, y2_axes: ChartAxes) -> None:
        self.__y2_axes = y2_axes

    def get_show_legend(self) -> bool:
        return self.__show_legend

    def set_show_legend(self, show_legend: bool) -> None:
        self.__show_legend = show_legend