from abc import abstractmethod
from typing import List


class IBBGDataPoint:

    @abstractmethod
    def add(self, data_points) -> None:
        pass

    @abstractmethod
    def get_data(self) -> List:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def get_message(self) -> str:
        pass

    @abstractmethod
    def set_message(self, message: str) -> str:
        pass
