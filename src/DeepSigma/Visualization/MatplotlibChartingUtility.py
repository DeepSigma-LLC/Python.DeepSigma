from matplotlib.lines import Line2D
from typing import List, Union
from matplotlib.patches import Wedge
from src import ChartAxes
from matplotlib.axes import Axes
import matplotlib.ticker as formate
from src import ChartGroup
from src import ChartAxisFormatType

def configure_chart(ax: Axes, ax2: Axes, config: ChartGroup, series_object: List[Union[Line2D,Wedge]],
                    labels: List[str], config_axes: bool) -> None:
    ax.set_title(config.get_chart_title())

    if config.get_show_legend():
        ax.legend(series_object, labels, title="Legend")

    if config_axes:
        __configure_chart_axes(ax, ax2, config)

def __configure_chart_axes(ax: Axes, ax2: Axes, config: ChartGroup) -> None:
    x_axis: ChartAxes = config.get_x_axes()
    y_axis: ChartAxes = config.get_y_axes()
    y2_axis: ChartAxes = config.get_y2_axes()

    ax.set_xlabel(x_axis.get_axes_label())
    ax.set_ylabel(y_axis.get_axes_label())
    __set_x_axis_format(ax, x_axis)
    __set_y_axis_format(ax, y_axis)

    if config.has_y2_axis():
        ax2.set_ylabel(y2_axis.get_axes_label(), rotation=270, labelpad=15, va='top')
        __set_y_axis_format(ax2, y2_axis)


def __set_y_axis_format(ax: Axes, axes_config: ChartAxes) -> None:
    if axes_config.get_number_of_ticks() is not None:
        ax.yaxis.set_major_locator(formate.MaxNLocator(axes_config.get_number_of_ticks()))

    if axes_config.get_axes_as_log():
        ax.set_yscale("log")

    if axes_config.get_axes_format() == ChartAxisFormatType.NoFormat:
            return
    elif axes_config.get_axes_format() == ChartAxisFormatType.Percentage:
        formatter = formate.PercentFormatter()
        ax.yaxis.set_major_formatter(formatter)
    elif axes_config.get_axes_format() == ChartAxisFormatType.DollarValue:
        ax.yaxis.set_major_formatter(formate.StrMethodFormatter("${x:,.2f}"))


def __set_x_axis_format(ax: Axes, axes_config: ChartAxes) -> None:
    if axes_config.get_number_of_ticks() is not None:
        ax.xaxis.set_major_locator(formate.MaxNLocator(axes_config.get_number_of_ticks()))

    if axes_config.get_axes_as_log():
        ax.set_xscale("log")

    if axes_config.get_axes_format() == ChartAxisFormatType.NoFormat:
            return
    elif axes_config.get_axes_format() == ChartAxisFormatType.Percentage:
        formatter = formate.PercentFormatter()
        ax.xaxis.set_major_formatter(formatter)
    elif axes_config.get_axes_format() == ChartAxisFormatType.DollarValue:
        ax.xaxis.set_major_formatter(formate.StrMethodFormatter("${x:,.2f}"))
