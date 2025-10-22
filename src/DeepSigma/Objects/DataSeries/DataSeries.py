from typing import List
from enum import Enum
from src.DeepSigma.Objects.NumpyCustom.NumpyCustomTensor import NumpyCustomTensor
from src.DeepSigma.Objects.DataField import DataField
from src.DeepSigma.Objects.DataFieldSchema import DataFieldSchema
import numpy

class DataSeries:
    def __init__(self, series_name: str, fields: List[DataField]):
        self._series_name: str = series_name
        self.__fields: List[DataField] = fields
        schema = DataFieldSchema()

        for field in fields:
            schema.add(field)

        self._data: NumpyCustomTensor = NumpyCustomTensor(schema.get_numpy_data_type_schema())

    def add_data_from_individual_lists(self, datasets: List[List]) -> None:
        """
        Adds data to a data series from individual lists. Usage example:
        If you have three fields,
        then series.add_data_from_individual_lists( [ [1, 2, 3], [60, 65, 61], [70, 71, 72] ] )
        :param datasets:
        :return:
        """
        if len(datasets) == 0:
            raise AttributeError('Data cannot both be None.')

        if len(datasets) > len(self.__fields):
            raise AttributeError('You cannot add more datasets than their are fields.')

        first_length = len(datasets[0])
        if not all(len(dataset) == first_length for dataset in datasets):
            raise AttributeError('Lists must have the same length.')

        # Transpose the data to create pairs
        data = list(zip(*datasets))  # Note the asterisk here
        self.add_data(data)

    def add_data(self, data: List) -> None:
        """
        Adds data to the data series. Usage: series.add( [(500, 1),(600, 2), (700, 3)] )
        :param data:
        :return:
        """
        self._data.set_data(data)

    def get_data(self) -> numpy.array:
        """
        Returns underlying data from data series.
        :return: numpy.array
        """
        return self._data.get_data()

    def get_data_from_field(self, field_name: Enum) -> numpy.array:
        """
        Returns underlying data from data series for a specified field name.
        :return: numpy.array
        """
        return self._data.get_data_from_field(field_name)

    def get_series_name(self) -> str:
        """
        Return series name.
        :return:
        """
        return self._series_name
