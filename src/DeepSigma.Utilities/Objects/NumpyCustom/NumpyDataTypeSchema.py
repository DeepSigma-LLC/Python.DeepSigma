import numpy as np
from enum import Enum
from src.MetaKit.Objects.NumpyCustom import NumpyDataTypeAdapter as Adapter


class NumpyDataTypeSchema:

    def __init__(self):
        self.__data_type_field_pairs: list[tuple[Enum, type]] = []

    def add_item(self, enum: Enum, data_type: type) -> None:
        """
        Adds a new field to the field object.
        :param enum:
        :param data_type:
        :return:
        """
        new_item: tuple[Enum, type] = (enum, data_type)
        self.__data_type_field_pairs.append(new_item)

    def get_numpy_data_type_schema(self) -> np.dtype:
        """
        Gets a constructed numpy data type schema from the desired fields.
        :return:
        """
        return np.dtype(self.__get_converted_data_type_schema())

    def __get_converted_data_type_schema(self) -> list[tuple[str, np.dtype]]:
        """
        Returns a list of field names and numpy data types.
        :return:
        """
        dtype_schema: list[tuple[str, np.dtype]] = []
        for item in self.__data_type_field_pairs:
            item_tuple: tuple[str, np.dtype] = (item[0].name, Adapter.convert_to_numpy_data_type(item[1]))
            dtype_schema.append(item_tuple)
        return dtype_schema
