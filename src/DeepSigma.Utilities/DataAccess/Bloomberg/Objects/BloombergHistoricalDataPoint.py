from src.MetaKit.DataAccess.Bloomberg.Objects.BloombergDataPointAbstract import IBBGDataPoint
from src.MetaKit.DataAccess.Bloomberg.Objects.BloombergHistoricalDataStructure import BloombergHistoricalDataStructure
from datetime import datetime
from typing import List, Dict


class BloombergHistoricalDataPoint(IBBGDataPoint):
    def __init__(self):
        self.__total_response_message: str = ""
        self.__data_points: List[BloombergHistoricalDataStructure] = []

    def add(self, data_point: BloombergHistoricalDataStructure) -> None:
        self.__data_points.append(data_point)

    def get_data(self) -> List[BloombergHistoricalDataStructure]:
        """Get underlying data point structures."""
        return self.__data_points

    def get_value(self, ticker: str, field: str, date_time: datetime):
        values: Dict[datetime, float] = self.get_values_as_dictionary(ticker, field)
        if date_time in values.keys():
            result: float = values[date_time]
            return result
        else:
            return None

    def get_value_time_series(self, ticker: str, field: str) -> Dict[datetime, float]:
        return self.get_values_as_dictionary(ticker, field)

    def count(self) -> int:
        return len(self.__data_points)

    def get_message(self) -> str:
        return self.__total_response_message

    def set_message(self, message: str) -> None:
        self.__total_response_message = message

    def get_values_as_dictionary(self, ticker: str, field: str) -> Dict[datetime, float]:
        values: Dict[datetime, float] = {}
        data = [x for x in self.__data_points if x.ticker == ticker and x.field == field]
        if data is not None:
            values = data[0].data
        return values
