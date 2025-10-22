import unittest
from src import VectorOperations
import math
import numpy as np


class TestVectorOperations(unittest.TestCase):

    def test_vector_item_count_is_zero(self):
        vector = np.array([])
        result = VectorOperations.vector_item_count(vector)
        self.assertEquals(result, 0)

    def test_vector_item_count_is_one(self):
        vector = np.array([0])
        result = VectorOperations.vector_item_count(vector)
        self.assertEquals(result, 1)

    def test_vector_item_count_is_3(self):
        vector = np.array([1, 0, 4])
        result = VectorOperations.vector_item_count(vector)
        self.assertEquals(result, 3)

    def test_vector_length_is_zero(self):
        vector = np.array([0, 0, 0])
        result = VectorOperations.vector_length(vector)
        self.assertEquals(result, 0)

    def test_vector_length_is_1(self):
        vector = np.array([1, 0, 0])
        result = VectorOperations.vector_length(vector)
        self.assertEquals(result, 1)


    def test_vector_length_is_5(self):
        vector = np.array([3, 4])
        result = VectorOperations.vector_length(vector)
        self.assertEquals(result, 5)

    def test_is_unit_vector_is_true(self):
        vector = np.array([1, 0, 0])
        result = VectorOperations.is_unit_vector(vector)
        self.assertTrue(result)

    def test_is_unit_vector_zero_vector_is_false(self):
        vector = np.array([0, 0, 0])
        result = VectorOperations.is_unit_vector(vector)
        self.assertFalse(result)

    def test_is_unit_vector_is_false(self):
        vector = np.array([2, 3, 5])
        result = VectorOperations.is_unit_vector(vector)
        self.assertFalse(result)

    def test_vector_to_unit_vector(self):
        vector = np.array([2, 0, 0])
        calculated_unit_vector = VectorOperations.vector_to_unit_vector(vector)
        equivalent_unit_vector = np.array([1, 0, 0])
        self.assertEquals(calculated_unit_vector.all(), equivalent_unit_vector.all())

    def test_are_vectors_perpendicular_is_true(self):
        vector1 = np.array([1, 0, 0])
        vector2 = np.array([0, 1, 0])
        result = VectorOperations.are_vectors_perpendicular(vector1, vector2)
        self.assertTrue(result)

    def test_are_vectors_perpendicular_is_false(self):
        vector1 = np.array([1, 0, 0])
        vector2 = np.array([1, 0, 0])
        result = VectorOperations.are_vectors_perpendicular(vector1, vector2)
        self.assertFalse(result)

    def test_angle_between_vectors_is_zero(self):
        vector1 = np.array([2, 0, 0])
        vector2 = np.array([1, 0, 0])
        result = VectorOperations.angle_between_vectors(vector1, vector2)
        self.assertEquals(result, 0)

    def test_angle_between_vectors_is_90_degrees(self):
        vector1 = np.array([1, 0])
        vector2 = np.array([0, 1])
        result = VectorOperations.angle_between_vectors(vector1, vector2)
        self.assertEquals(result, math.pi/2)


if __name__ == '__main__':
    unittest.main()
