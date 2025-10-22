import numpy
import numpy as np
import pandas
import pandas as pd
import json
from types import SimpleNamespace
from typing import List


def matrix_to_dataframe(matrix: np.array, column_headers: List[str] = None) -> pd.DataFrame:
    """
            Numpy array to data frame.
            :param matrix:
            :param column_headers:
            :return:
            """
    if column_headers is None:
        return pd.DataFrame(matrix)
    return pd.DataFrame(matrix, columns=column_headers)

def dataframe_to_matrix(data_frame: pd.DataFrame) -> numpy.array:
    """
            Data frame to numpy array.
            :param data_frame:
            :return:
            """
    return data_frame.to_numpy()

def dict_to_dataframe(dict_data: dict) -> pandas.DataFrame:
    """
            Dictionary to data frame.
            :param dict_data:
            :return:
            """
    dataframe = pd.DataFrame.from_dict(dict_data, orient='index')
    dataframe.reset_index(level=0, inplace=True)
    return dataframe

def list_to_dataframe(list_of_objects: list[object]) -> pandas.DataFrame:
    """
            List of objects to data frame.
            :param list_of_objects:
            :return:
            """
    return pd.DataFrame.from_records(obj.__dict__ for obj in list_of_objects)

def json_to_object(json_data: str) -> object:
    """
            Json to object.
            :param json_data:
            :return:
            """
    json_str = json.dumps(json_data)
    data_object = json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))
    return data_object

def update_dataframe_field_names(dataframe: pd.DataFrame,
                                 original_field_names: List[str], new_field_names: List[str]) -> pd.DataFrame:
    """Update data frame field names with new field names."""
    i = 0
    while i < len(original_field_names):
        dataframe = dataframe.rename(columns={original_field_names[i]: new_field_names[i]})
        i = i + 1
    dataframe = dataframe[new_field_names]
    return dataframe

def update_dataframe_datatypes(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.astype(float)
    dataframe.index = pd.to_datetime(dataframe.index)
    return dataframe
