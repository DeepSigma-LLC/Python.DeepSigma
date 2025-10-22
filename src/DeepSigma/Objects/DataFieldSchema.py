from src.DeepSigma.Objects import DataField
from typing import List
import numpy
from src.DeepSigma.Objects.NumpyCustom import NumpyDataTypeAdapter as Adapter


class DataFieldSchema:

    def __init__(self):
        self._data_fields: List[DataField] = []

    def add(self, data_field: DataField):
        """
        Add data field to schema.
        :param data_field:
        :return:
        """
        self._data_fields.append(data_field)

    def get_numpy_data_type_schema(self) -> numpy.dtype:
        """
        Gets a constructed numpy data type schema from the desired fields.
        :return:
        """
        return numpy.dtype(self.__get_converted_data_type_schema())

    def __get_converted_data_type_schema(self) -> list[tuple[str, numpy.dtype]]:
        """
        Returns a list of field names and numpy data types.
        :return:
        """
        dtype_schema: list[tuple[str, numpy.dtype]] = []
        for item in self._data_fields:
            item_tuple: tuple[str, numpy.dtype] = (item.name, Adapter.convert_to_numpy_data_type(item.data_type))
            dtype_schema.append(item_tuple)
        return dtype_schema