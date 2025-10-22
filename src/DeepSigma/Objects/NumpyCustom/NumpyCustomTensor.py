import numpy as np
from enum import Enum
import datetime
from src import NumpyDataTypeAdapter
from typing import List


class NumpyCustomTensor:
    _data_tensor: np.array = np.array([])

    def __init__(self, field_data_schema: np.dtype):
        self.__field_data_schema: np.dtype = field_data_schema
        pass

    def set_data(self, data: List) -> None:
        """
        Set data into the tensor from a list.
        Usage for a two-dimensional array: set_data( [(5000, 1), (6000, 2), (7000, 3)] )
        :param data:
        :return: None
        """
        self._data_tensor = np.array(data, dtype=self.__field_data_schema)

    def get_data(self) -> np.array:
        """
        Gets all data from the underlying data structure.
        :return: Numpy array
        """
        return self._data_tensor

    def get_data_from_field(self, selected_field: Enum) -> np.array:
        """
        Gets all data from the underlying data structure for a selected field.
        :param selected_field:
        :return: Numpy array
        """
        return self._data_tensor[selected_field.name]

    def get_data_filtered(self, start_date: datetime, end_date: datetime) -> np.array:
        """
        Gets all data after selecting a date range.
        :param start_date:
        :param end_date:
        :return: Numpy array
        """
        data = self._data_tensor
        numpy_start_date = NumpyDataTypeAdapter.get_numpy_datetime(start_date)
        numpy_end_date = NumpyDataTypeAdapter.get_numpy_datetime(end_date)
        filtered_rows = data[(data[:, 0] >= numpy_start_date) & (data[:, 0] <= numpy_end_date)]
        return filtered_rows

    def get_data_field_filtered(self, selected_enum: Enum, start_date: datetime, end_date: datetime) -> np.array:
        """
        Gets all data for a field after selecting a date range.
        :param selected_enum:
        :param start_date:
        :param end_date:
        :return: Numpy array
        """
        data = self._data_tensor
        numpy_start_date = NumpyDataTypeAdapter.get_numpy_datetime(start_date)
        numpy_end_date = NumpyDataTypeAdapter.get_numpy_datetime(end_date)
        filtered_rows = data[(data[:, 0] >= numpy_start_date) & (data[:, 0] <= numpy_end_date)]
        return filtered_rows[selected_enum.name]
