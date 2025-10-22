from typing import List, Optional
from src.DeepSigma.Objects.ChartObjects.Chart import Chart



class ChartCollectionGroup:
    def __init__(self) -> None:
        self.__charts: List[List] = []

    def add_chart(self, chart: Chart, row_index: Optional[int] = None, column_index: Optional[int] = None) -> None:
        """
        Adds a chart object to the collection group. Note: if row or column indexes are left as None,
        the method will auto-assign the charts vertically into rows in column at index 0.
        :param chart:
        :param row_index:
        :param column_index:
        :return:
        """
        # Ensure we have at least one column
        if len(self.__charts) == 0:
            self.__charts.append([])

        if row_index is None or column_index is None:
            self.__charts[0].append(chart)
        else:
            # Ensure we have enough columns
            while len(self.__charts) <= column_index:
                self.__charts.append([])

            # Ensure we have enough rows in the target column
            while len(self.__charts[column_index]) <= row_index:
                self.__charts[column_index].append(None)

            self.__charts[column_index][row_index] = chart

    def get_charts_in_column(self, column_index: int) -> List[Chart]:
        if len(self.__charts) == 0:
            raise IndexError("No charts available")
        return self.__charts[column_index]

    def get_chart_row_count(self) -> int:
        if not self.__charts or not self.__charts[0]:
            return 0
        return len(self.__charts[0])

    def get_chart_column_count(self) -> int:
        return len(self.__charts)
