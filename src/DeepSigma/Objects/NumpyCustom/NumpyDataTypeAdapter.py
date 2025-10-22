"""
   Adapter responsible for converting python data types to numpy data types.
"""
import numpy as np
import datetime


def convert_to_numpy_data_type(python_data_type: type, max_string_size: int = 20):
    """
    Converts python data types to numpy data types.
    :param python_data_type:
    :param max_string_size:
    :return:
    """
    if python_data_type == float:
        return np.float64
    elif python_data_type == datetime.datetime:
        return "datetime64[D]"
    elif python_data_type == int:
        return np.int64
    elif python_data_type == str:
        return 'U'+str(max_string_size)
    elif python_data_type == bool:
        return np.bool_
    else:
        raise NotImplementedError("The passed data type mapping is not yet implemented by the custom adapter.")

def get_numpy_datetime(date_time: datetime.datetime) -> np.datetime64:
    return np.datetime64(date_time)
