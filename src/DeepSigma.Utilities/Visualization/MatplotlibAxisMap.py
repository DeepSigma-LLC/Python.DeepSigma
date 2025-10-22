from matplotlib.axes import Axes
from typing import Optional


class MatplotlibAxisMap:
    def __init__(self):
        self.map: dict[tuple[int, int], tuple[Axes, Axes]] = {}

    def get_axis(self, column_i: int, row_i: int) -> Optional[Axes]:
        if self.map[column_i, row_i] is None:
            return None
        return self.map[column_i, row_i][0]

    def get_axis_secondary(self, column_i: int, row_i: int) -> Optional[Axes]:
        if self.map[column_i, row_i] is None:
            return None
        return self.map[column_i, row_i][1]

    def save_axis_map(self, column_i: int, row_i: int, axis: Axes, axis2: Optional[Axes] = None) -> None:
        self.map[column_i, row_i] = (axis, axis2)
