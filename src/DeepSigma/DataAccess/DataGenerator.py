import numpy as np
from typing import Union, List


def get_equally_spaced_values(start_value: Union[int, float], end_value: Union[int, float],
                              number_of_elements) -> np.ndarray:
    """
    Function that returns an array of values between start and end values.
    :param start_value:
    :param end_value:
    :param number_of_elements:
    :return:
    """
    return np.linspace(start = start_value, stop = end_value, num = number_of_elements)


def get_data_grid(x_start: Union[int, float], x_end: Union[int, float], y_start: Union[int, float],
                  y_end: Union[int, float], x_number_of_elements: int = 50,
                  y_number_of_elements: int = 50) -> List[np.ndarray]:
    """
    Returns generates grid of values that can be used in generating 3D graphics.
    :param x_start:
    :param x_end:
    :param y_start:
    :param y_end:
    :param x_number_of_elements:
    :param y_number_of_elements:
    :return:
    """
    x = get_equally_spaced_values(start_value = x_start, end_value = x_end, number_of_elements = x_number_of_elements)
    y = get_equally_spaced_values(start_value = y_start, end_value = y_end, number_of_elements = y_number_of_elements)
    return np.meshgrid(x, y)


def get_normal_data(mean: Union[int, float] = 0, standard_deviation: Union[int, float] = 1,
                    number_of_elements: int = 1000) -> np.ndarray:
    """
    Function that draws random sample from a normal (Gaussian) distribution.

    By default, this function returns sample data from the standard normal distribution
    (where mean = 0 and standard deviation = 1).
    :param mean:
    :param standard_deviation:
    :param number_of_elements: Sample size to return.
    :return:
    """
    return np.random.normal(loc = mean, scale = standard_deviation, size = number_of_elements)