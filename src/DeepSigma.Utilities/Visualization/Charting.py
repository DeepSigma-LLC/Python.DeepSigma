import matplotlib.pyplot as plot
import numpy as np
from typing import Union, Tuple, Optional
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib
from matplotlib.container import BarContainer
from matplotlib.lines import Line2D
from matplotlib.patches import Wedge
from src.MetaKit.Objects.ChartObjects.Enums.ChartCoordinateSystemType import ChartCoordinateSystemType
from src.MetaKit.Visualization import MatplotlibChartingUtility
from src.MetaKit.Objects.DataSeries.DataSeries import *
from src.MetaKit.Objects.ChartObjects.ChartGroup import ChartGroup
from scipy.interpolate import PchipInterpolator
import scipy.stats as stats
import seaborn as sns
from src.MetaKit.Objects.ChartObjects.ChartCollectionGroup import ChartCollectionGroup
from src.MetaKit.Objects.ChartObjects.Chart import Chart
from src.MetaKit.Objects.ChartObjects.Enums.ChartGridlineType import ChartGridlineType
from matplotlib import gridspec
from src.MetaKit.Objects.ChartObjects.Enums.ChartType import ChartType
from src.MetaKit.Visualization.MatplotlibAxisMap import MatplotlibAxisMap


def build_chart(chart_collection_group: ChartCollectionGroup, dark_mode: bool = False):
    row_count = chart_collection_group.get_chart_row_count()
    column_count = chart_collection_group.get_chart_column_count()

    plot.style.use("default")
    if dark_mode:
        plot.style.use("dark_background")

    figure = plot.figure(figsize=(12, 8))
    grid: gridspec = gridspec.GridSpec(nrows=row_count, ncols=column_count)

    current_sub_plot: Axes
    axes_map: MatplotlibAxisMap = MatplotlibAxisMap()
    for column_i in range(0, column_count):
        charts: List[Chart] = chart_collection_group.get_charts_in_column(column_i)
        for row_i in range(0, row_count):
            # If the chart does not exist, turn off the axis and skip.
            if row_i >= len(charts) or charts[row_i] is None:
                #axis_container[column_i][row_i].axis('off')
                continue

            chart: Chart = charts[row_i]
            current_sub_plot, sub_plot_y2 = __create_plot_axes(chart, figure, grid, column_i, row_i, axes_map)
            __build_chart(current_sub_plot, chart, sub_plot_y2)
            current_sub_plot.set_title(chart.get_chart_title())
            current_sub_plot.set_xlabel(chart.x_axis.get_axes_label())
            current_sub_plot.set_ylabel(chart.y_axis.get_axes_label())

            if sub_plot_y2 is not None and chart.get_has_secondary_y_axis():
                sub_plot_y2.set_ylabel(chart.y_secondary_axis.get_axes_label(), rotation=270, labelpad=15, va='top')
            elif sub_plot_y2 is not None:
                sub_plot_y2.set_yticks([])
                sub_plot_y2.set_yticklabels([])

            __set_gridlines(chart, current_sub_plot)

    plot.tight_layout()
    plot.show()


def __build_chart(chart_plot_primary: Axes, chart: Chart, chart_plot_secondary: Axes = None) -> None:
    for series in chart.get_all_series():
        color: str = series.get_color()
        x = series.data_series.get_data_from_field(series.x_field) if series.x_field is not None else None
        y = series.data_series.get_data_from_field(series.y_field) if series.y_field is not None else None
        z = series.data_series.get_data_from_field(series.z_field) if series.z_field is not None else None
        label: str = series.data_series.get_series_name()

        selected_plot: Axes = chart_plot_primary
        if series.use_y_secondary:
            selected_plot = chart_plot_secondary

        match series.get_chart_type():
            case ChartType.LineChart:
                selected_plot.plot(x, y, label=label, color=color, marker='o')
            case ChartType.StepChart:
                selected_plot.step(x, y, label=label, color=color, marker='o')
            case ChartType.SplineChart:
                new_point_count = len(x) * 20
                x_smooth = np.linspace(x.min(), x.max(), new_point_count)
                spline = PchipInterpolator(x, y)
                y_smooth = spline(x_smooth)

                selected_plot.plot(x_smooth, y_smooth, label=label, color=color)
                selected_plot.scatter(x, y, color=color)
            case ChartType.ScatterChart:
                selected_plot.scatter(x, y, label=label, color=color)
            case ChartType.BarChart:
                selected_plot.bar(x, y, label=label, color=color)
            case ChartType.HorizontalBarChart:
                selected_plot.barh(x, y, label=label, color=color)
            case ChartType.HistogramChart:
                selected_plot.hist(y, color=color, bins=10, label=label, density=False)
            case ChartType.QQChart:
                stats.probplot(y, dist="norm", plot=plot)
            case ChartType.PieChart:
                selected_plot.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
                selected_plot.set_aspect('equal')
                selected_plot.axis('equal')  # ensures it's a circle
                selected_plot.set_axis_off()
            case ChartType.DonutChart:
                donut_width = 0.4
                radius = 0.7
                selected_plot.pie(y, labels=x, autopct='%1.1f%%', wedgeprops=dict(width=donut_width))
                my_circle = plot.Circle((0, 0), radius, color="white")
                plot.gcf().gca().add_artist(my_circle)
            case ChartType.RadarChart:
                if len(x) != len(y):
                    raise ValueError("x and y must be the same length")

                angles = np.linspace(0, 2 * np.pi, len(x), endpoint=False)

                # Close the plot by appending the first value to the end
                angles = np.append(angles, angles[0])
                values = np.append(y, y[0])

                # Create the radar chart
                selected_plot.plot(angles, values, color=color, linewidth=2)
                selected_plot.fill(angles, values, color=color, alpha=0.25)

                selected_plot.set_xticks(angles[:-1])
                selected_plot.set_xticklabels(x)
            case ChartType.ViolinChart:
                selected_plot.violinplot(y, showmeans=True, showmedians=True)
            case ChartType.SurfaceChart:
                selected_plot.plot(x, y, z, color=color)
            case _:
                raise NotImplementedError("Chart type not supported yet.")

    if chart.get_show_legend():
        object_handles, series_labels = chart_plot_primary.get_legend_handles_labels()
        if chart_plot_secondary is not None:
            lines2, labels2 = chart_plot_secondary.get_legend_handles_labels()
            object_handles.extend(lines2)
            series_labels.extend(labels2)
        chart_plot_primary.legend(object_handles, series_labels, loc='best')


def __create_plot_axes(chart: Chart, figure: Figure, grid: gridspec.GridSpec,
                       column_i: int, row_i: int,
                       axes_map:  MatplotlibAxisMap) -> tuple[Axes, Axes]:
    x_axis_location = chart.get_shared_x_axis_grid_location()
    y_axis_location = chart.get_shared_y_axis_grid_location()

    share_x: Optional[Axes] = None
    share_y: Optional[Axes] = None
    if x_axis_location is not None:
        share_x = axes_map.get_axis(x_axis_location[0], x_axis_location[1])

    if y_axis_location is not None:
        share_y = axes_map.get_axis(y_axis_location[0], y_axis_location[1])

    subplot_kwargs = {}
    __get_plot_coordinate_system_projection(chart, subplot_kwargs)
    sub_plot = figure.add_subplot(grid[row_i, column_i], sharex=share_x, sharey=share_y, **subplot_kwargs)

    y2_sub_plot: Optional[Axes]
    if (chart.get_coordinate_system_type() == ChartCoordinateSystemType.Cartesian
            and not chart.get_is_three_dimensional()):
        y2_sub_plot = sub_plot.twinx()
    else:
        y2_sub_plot = None

    axes_map.save_axis_map(column_i, row_i, sub_plot, y2_sub_plot)

    return sub_plot, y2_sub_plot


def __get_plot_coordinate_system_projection(chart: Chart, subplot_kwargs: dict) -> None:
    if chart.get_is_three_dimensional():
        subplot_kwargs['projection'] = '3d'
    elif chart.get_coordinate_system_type() == ChartCoordinateSystemType.Polar:
        subplot_kwargs['projection'] = 'polar'
    elif chart.get_coordinate_system_type() == ChartCoordinateSystemType.Cartesian:
        pass
    else:
        raise NotImplementedError("Coordinate system not supported yet.")


def __set_gridlines(chart: Chart, axis: Axes) -> None:
    """
    Set the gridline parameters for the chart.
    :param chart:
    :param axis:
    :return:
    """
    if chart.get_show_gridlines():
        if chart.get_gridline_type() == ChartGridlineType.HorizontalOnly:
            axis.grid(visible=True, axis="y")
        elif chart.get_gridline_type() == ChartGridlineType.VerticalOnly:
            axis.grid(visible=True, axis="x")
        else:
            axis.grid(visible=True)


def scatter_plot(chart_group: ChartGroup, show_plot: bool = True, show_grid = True, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    lines: List[Line2D] = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        line: Line2D = None
        if series.use_y2:
            line, = ax2.scatter(x, y, label=series.data_series.get_series_name())
        else:
            line, = ax.scatter(x, y, label=series.data_series.get_series_name())
        lines.append(line)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=lines, show_grid=show_grid,
                            show_plot=show_plot)

def line_chart(chart_group: ChartGroup, show_plot: bool = True, show_grid = True, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    lines: List[Line2D] = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        line: Line2D = None
        if series.use_y2:
            line, = ax2.plot(x, y, label=series.data_series.get_series_name(), marker='o')
        else:
            line, = ax.plot(x, y, label=series.data_series.get_series_name(),  marker='o')
        lines.append(line)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=lines, show_grid=show_grid,
                            show_plot=show_plot)

def line_spline_chart(chart_group: ChartGroup, show_plot: bool = True, show_grid = True, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    lines: List[Line2D] = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        new_point_count = len(x)*20
        x_smooth = np.linspace(x.min(), x.max(), new_point_count)
        spline = PchipInterpolator(x, y)
        y_smooth = spline(x_smooth)

        line: Line2D = None
        if series.use_y2:
            line, = ax2.plot(x_smooth, y_smooth, label=series.data_series.get_series_name())
        else:
            line, = ax.plot(x_smooth, y_smooth, label=series.data_series.get_series_name())
        lines.append(line)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=lines, show_grid=show_grid,
                            show_plot=show_plot)


def step_chart(chart_group: ChartGroup, show_plot: bool = True, show_grid = True, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    lines: List[Line2D] = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        line: Line2D = None
        if series.use_y2:
            line, = ax2.step(x, y, label=series.data_series.get_series_name(), marker='o')
        else:
            line, = ax.step(x, y, label=series.data_series.get_series_name(), marker='o')
        lines.append(line)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=lines, show_grid=show_grid,
                            show_plot=show_plot)


def histogram(chart_group: ChartGroup, density: bool = True, bin_count: int = 5, show_plot: bool = True,
              show_grid = False, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    lines: List = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        line : Union[Line2D, BarContainer, None] = None
        if series.use_y2:
            line = ax2.hist(y, density=density, bins=bin_count, edgecolor='black',
                             label=series.data_series.get_series_name())
        else:
            line = ax.hist(y, density=density, bins=bin_count, edgecolor='black',
                              label=series.data_series.get_series_name())
        lines.append(line)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=lines, show_grid=show_grid,
                            show_plot=show_plot)

def bar_chart(chart_group: ChartGroup, show_plot: bool = True, show_grid = False, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    lines: List = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        line: BarContainer
        if series.use_y2:
            line = ax2.bar(x, y, label=series.data_series.get_series_name())
        else:
            line = ax.bar(x, y, label=series.data_series.get_series_name())
        lines.append(line)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=lines, show_grid=show_grid,
                            show_plot=show_plot)

def bar_horizontal_chart(chart_group: ChartGroup, show_plot: bool = True, show_grid = False, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    lines: List = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        line: BarContainer
        if series.use_y2:
            line = ax2.barh(x, y, label=series.data_series.get_series_name())
        else:
            line = ax.barh(x, y, label=series.data_series.get_series_name())
        lines.append(line)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=lines, show_grid=show_grid,
                            show_plot=show_plot)

def stacked_area_chart(chart_group: ChartGroup, show_plot: bool = True, show_grid = False, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    labels: List[str] = []
    x = None
    y = []
    for series in chart_group.get_all_series():
        labels.append(series.data_series.get_series_name())
        x = series.data_series.get_data_from_field(series.x_field)
        y.append(series.data_series.get_data_from_field(series.y_field))
    line = ax.stackplot(x, *y, labels=labels)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, show_grid=show_grid, show_plot=show_plot)

def pie_chart(chart_group: ChartGroup, show_plot: bool = True, dark_mode: bool = False) -> matplotlib.pyplot:
    ax: Axes
    ax2: Axes
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode = dark_mode)

    wedges: List = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        wedges, texts, _ = ax.pie(y, labels=x, autopct='%1.1f%%', startangle=90)

    ax.set_aspect('equal')
    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=wedges, show_plot=show_plot)

def donut_chart(chart_group: ChartGroup, show_plot: bool = True,
                radius: float = 0.7, donut_width: float = 0.4, dark_mode: bool = False) -> matplotlib.pyplot:
    ax: Axes
    ax2: Axes
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    wedges: List = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        wedges, text, _ = ax.pie(y, labels=x,  autopct='%1.1f%%', wedgeprops=dict(width=donut_width))
        my_circle = plot.Circle((0, 0), radius, color="white")
        plot.gcf().gca().add_artist(my_circle)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=wedges, show_plot=show_plot)

def radar_chart(chart_group: ChartGroup, show_plot: bool = True, dark_mode: bool = False) -> matplotlib.pyplot:
    ax: Axes
    ax2: Axes
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode, is_polar=True)

    lines: List[Line2D] = []
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)  # category labels
        y = series.data_series.get_data_from_field(series.y_field)  # numeric values

        if len(x) != len(y):
            raise ValueError("x and y must be the same length")

        # Convert to radar chart format
        angles = np.linspace(0, 2 * np.pi, len(x), endpoint=False).tolist()
        angles += angles[:1]
        new_y = np.concatenate((y, [y[0]]))

        # Radar chart line
        line = ax.plot(angles, new_y, color='blue', linewidth=2)[0]
        ax.fill(angles, new_y, color='blue', alpha=0.25)

        # Label each spoke
        ax.set_xticks(angles[:-1])  # exclude repeated last point
        ax.set_xticklabels(x)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, series_objects=lines, show_plot=show_plot, show_grid=True)

def boxplot_chart(chart_group: ChartGroup, show_plot: bool = True, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    labels: List = []
    data: List = []
    for series in chart_group.get_all_series():
        labels.append(series.data_series.get_series_name())

        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        data.append(y)

    # not in for loop intentional
    ax.boxplot(data, tick_labels=labels)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, show_plot=show_plot)

def qq_plot(chart_group: ChartGroup, show_plot: bool = True, show_grid = True, dark_mode: bool = False) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)

        if series.use_y2:
            stats.probplot(y, dist="norm", plot=plot)
        else:
            stats.probplot(y, dist="norm", plot=plot)

    return __finalize_setup(chart_group, ax, ax2,
                            configure_axes=True, show_grid=show_grid, show_plot=show_plot)


def violin_plot(chart_group: ChartGroup, show_plot: bool = True, dark_mode: bool = True) -> matplotlib.pyplot:
    ax, ax2, _ = __initialize_chart(chart_group, dark_mode=dark_mode)

    data: List = []
    labels: List[str] = []
    ticks: List[int] = []
    i: int = 0
    for series in chart_group.get_all_series():
        x = series.data_series.get_data_from_field(series.x_field)
        y = series.data_series.get_data_from_field(series.y_field)
        data.append(y)
        ticks.append(i)
        labels.append(series.data_series.get_series_name())
        i = i + 1

    # not in for loop intentional
    sns.violinplot(data=data)
    plot.xticks(ticks=ticks, labels=labels)

    return __finalize_setup(chart_group, ax, ax2, configure_axes=True, show_plot=show_plot)

def __initialize_chart(chart_group: ChartGroup, dark_mode: bool = True,
                       is_polar: bool = False) -> Tuple[Axes, Axes, Figure]:
    """Initially configures chart"""
    if dark_mode:
        plot.style.use("dark_background")
    else:
        plot.style.use("default")

    figure, ax = plot.subplots(constrained_layout=True, subplot_kw=dict(polar=is_polar))
    ax2 = None
    if chart_group.has_y2_axis():
        ax2 = ax.twinx()
    return ax, ax2, figure

def __finalize_setup(chart_group: ChartGroup, ax: Axes, ax2: Axes, configure_axes: bool,
                     series_objects: List[Union[Line2D,Wedge]] = None, show_grid: bool = False,
                     show_plot: bool = True) -> matplotlib.pyplot:
    """Finalized the chart setup configuration"""
    if series_objects is not None and len(series_objects) > 0 and isinstance(series_objects[0], Line2D):
        set_line_colors(series_objects)
    labels: List = [] #[series.get_label() for series in series_objects]
    MatplotlibChartingUtility.configure_chart(ax, ax2, chart_group, series_objects, labels, configure_axes)

    plot.grid(show_grid)

    if show_plot:
        plot.show()
    return plot

def set_line_colors(lines: List[Line2D]):
    i = 0
    for line in lines:
        line.set_color(get_preferred_chart_color_hierarchy()[i])
        i = i + 1


def optimal_bin_width_freedman_diaconis_method(data: List) -> int:
    quartile_25, quartile_75 = np.percentile(data, [25, 75])
    inter_quartile_range = quartile_75 - quartile_25
    bin_width = 2 * inter_quartile_range * len(data) ** (-1/3)
    optimal_bin_count = round((data.max() - data.min()) / bin_width)
    return optimal_bin_count


def get_preferred_chart_color_hierarchy() -> List[str]:
    """
    Returns the list of distinct colors used for charting.
    :return: List[colors as str]
    """
    return ["blue", "red", "green", 'purple' ,"gray", "magenta", "orange", "cyan"]
