from src.MetaKit.DataAccess.Bloomberg.Objects.BloombergDataPointAbstract import IBBGDataPoint
from src.MetaKit.DataAccess.Bloomberg.Objects.BloombergDataPointStructure import BloombergDataPointStructure
from typing import List


class BloombergDataPoint(IBBGDataPoint):
    def __init__(self):
        self.__total_response_message: str = ""
        self.__data_points: List[BloombergDataPointStructure] = []

    def add(self, data_point: BloombergDataPointStructure) -> None:
        """Adds underlying data structures to object class."""
        self.__data_points.append(data_point)

    def get_data(self) -> List[BloombergDataPointStructure]:
        """Gets underlying data points."""
        return self.__data_points

    def get_value(self, ticker: str, field: str):
        results = [x for x in self.__data_points if x.ticker == ticker and x.field == field]
        result = results[0]
        if result is None:
            result = BloombergDataPointStructure()
        return result.value

    def count(self) -> int:
        return len(self.__data_points)

    def get_message(self) -> str:
        return self.__total_response_message

    def set_message(self, message: str) -> None:
        self.__total_response_message = message
