from src import IBBGDataPoint
from src import BloombergHistoricalBarDataStructure
from src import BloombergDataBar
from datetime import datetime
from typing import Dict, List


class BloombergHistoricalBarDataPoint(IBBGDataPoint):
    def __init__(self):
        self.__total_response_message: str = ""
        self.__data_points: List[BloombergHistoricalBarDataStructure] = []

    def add(self, data_point: BloombergHistoricalBarDataStructure) -> None:
        self.__data_points.append(data_point)

    def get_data(self) -> List[BloombergHistoricalBarDataStructure]:
        """Get underlying data point structures."""
        return self.__data_points

    def get_bar(self, ticker: str, date_time: datetime) -> BloombergDataBar:
        values: Dict[datetime, BloombergDataBar] = self.get_values_as_dictionary(ticker)
        result: BloombergDataBar = values[date_time]
        return result

    def get_value_time_series(self, ticker: str) -> Dict[datetime, BloombergDataBar]:
        return self.get_values_as_dictionary(ticker)

    def count(self) -> int:
        return len(self.__data_points)

    def get_message(self) -> str:
        return self.__total_response_message

    def set_message(self, message: str) -> None:
        self.__total_response_message = message

    def get_values_as_dictionary(self, ticker: str) -> Dict[datetime, BloombergDataBar]:
        values: Dict[datetime, BloombergDataBar] = {}
        data = [x for x in self.__data_points if x.ticker == ticker][0].data
        if data is not None:
            values = data
        return values
