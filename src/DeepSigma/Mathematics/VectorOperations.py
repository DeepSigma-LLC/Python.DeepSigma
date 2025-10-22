"""Custom class containing common vector operations."""
from src.DeepSigma.Mathematics import MatrixOperations
import math
import numpy as np


def vector_item_count(vector: np.array) -> int:
    num_columns = np.shape(vector)[0]
    return num_columns

def vector_length(vector: np.array) -> float:
    """Returns length of vector.
    Note: Per linear algebra, vector length is equal to the square root of the dot product of a vector
    by itself.
    """
    return MatrixOperations.dot_product(vector, vector) ** (1 / 2)

def vector_to_unit_vector(vector: np.array) -> np.array:
    """ Returns vector scaled to length of 1.
            Note: Per linear algebra, to obtain the unit vector, divide the vector coordinates by the
            length of the vector."""
    length = vector_length(vector)
    return vector / length

def is_unit_vector(vector: np.array) -> bool:
    """
            Returns boolean determining if vector is a unit vector by confirming its length is equal to 1.
            :param vector:
            :return: boolean
    """
    length = vector_length(vector)

    if length == 1:
        return True
    return False

def are_vectors_perpendicular(vector_0: np.array, vector_1: np.array) -> bool:
    """
            Returns boolean if the two vectors passed as parameters are perpendicular.

            Logic is derived from the law of perpendicular vectors which says that the dot product of two
            non-zero vectors is zero only when the vectors are perpendicular.
            :param vector_0:
            :param vector_1:
            :return: boolean
    """
    result = False
    product = MatrixOperations.dot_product(vector_0, vector_1)

    if product == 0:
        result = True
    return result

def angle_between_vectors(vector_0: np.array, vector_1: np.array) -> float:
    """
            Returns the angle between two vectors.

            Per linear algebra, the cosine of the angle between to unit vectors is equal to the dot
            product of those two vectors.
            :param vector_0:
            :param vector_1:
            :return: Angle between any two vectors.
    """
    unit_vector_0 = vector_to_unit_vector(vector_0)
    unit_vector_1 = vector_to_unit_vector(vector_1)

    dot_product = MatrixOperations.dot_product(unit_vector_0, unit_vector_1)
    return math.acos(dot_product)

