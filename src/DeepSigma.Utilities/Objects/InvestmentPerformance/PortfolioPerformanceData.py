import numpy
from enum import Enum
import datetime
from src.MetaKit.Objects.InvestmentPerformance.Enums.PortfolioPerformanceDataField import PortfolioPerformanceDataField as FieldName
from src.MetaKit.Objects.NumpyCustom.NumpyCustomTensor import NumpyCustomTensor
from src.MetaKit.Objects.NumpyCustom.NumpyDataTypeSchema import NumpyDataTypeSchema
from typing import List


class PortfolioPerformanceData:
    __data_fields: List[str] = [x.name for x in FieldName]
    __data_tensor: NumpyCustomTensor

    def __init__(self):
        self.__data_tensor = NumpyCustomTensor(self.__get_data_schema())
        pass

    def get_all_data(self) -> numpy.array:
        return self.__data_tensor.get_data()

    def get_data_by_field(self, field_enum: Enum) -> numpy.array:
        return self.__data_tensor.get_data()[field_enum.name]

    def update_data_by_field(self, field_enum: Enum, new_arr: []):
        self.__data_tensor.get_data()[field_enum.name] = numpy.array(new_arr)

    def set_data(self, data: []):
        self.__data_tensor.set_data(data)

    def set_computed_portfolio_return(self) -> None:
        self.update_data_by_field(field_enum=FieldName.PortfolioReturn,
                                  new_arr=self.get_data_by_field(FieldName.GainLoss) /
                                  self.get_data_by_field(FieldName.Denominator))

    def get_computed_excess_return(self) -> numpy.array:
        data = self.__data_tensor
        return data.get_data_field(FieldName.PortfolioReturn) - data.get_data_field(FieldName.BenchmarkReturn)

    def get_field_names(self) -> List[str]:
        return self.__data_fields

    @staticmethod
    def __get_data_schema() -> numpy.dtype:
        data_schema = NumpyDataTypeSchema()
        data_schema.add_item(FieldName.Datetime, datetime.datetime)
        data_schema.add_item(FieldName.GainLoss, float)
        data_schema.add_item(FieldName.Denominator, float)
        data_schema.add_item(FieldName.PortfolioReturn, float)
        data_schema.add_item(FieldName.BenchmarkReturn, float)
        data_schema.add_item(FieldName.UniverseReturn, float)
        return data_schema.get_numpy_data_type_schema()
