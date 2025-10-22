from src.DeepSigma.Objects.ChartObjects.Enums.ChartAxisFormatType import ChartAxisFormatType


class ChartAxes:
    def __init__(self, axes_label: str = "", chart_axis_format: ChartAxisFormatType = ChartAxisFormatType.NoFormat,
                 axes_as_log: bool = False, number_of_ticks: int = None):
        self.__axes_label: str = axes_label
        self.__axes_format: ChartAxisFormatType = chart_axis_format
        self.__axes_as_log: bool = axes_as_log
        self.__number_of_ticks: int = number_of_ticks

    def get_axes_label(self) -> str:
        return self.__axes_label

    def get_axes_format(self) -> ChartAxisFormatType:
        return self.__axes_format

    def get_axes_as_log(self) -> bool:
        return self.__axes_as_log

    def get_number_of_ticks(self) -> int:
        return self.__number_of_ticks

    def set_axes_label(self, axes_label: str) -> None:
        self.__axes_label = axes_label

    def set_axes_as_log(self, axes_as_log: bool) -> None:
        self.__axes_as_log = axes_as_log

    def set_number_of_ticks(self, number_of_ticks: int) -> None:
        self.__number_of_ticks = number_of_ticks

    def get_axes_format(self, chart_axis_format_type: ChartAxisFormatType) -> None:
        self.__axes_format = chart_axis_format_type
