import unittest
from src import MatrixOperations
import numpy as np


class TestMatrixOperations(unittest.TestCase):

    def test_row_count_is_2(self):
        matrix = np.array([[1, 2, 3],
                          [4, 5, 6]])
        result = MatrixOperations.row_count(matrix)
        self.assertEquals(result, 2)

    def test_column_count_is_3(self):
        matrix = np.array([[1, 2, 3],
                          [4, 5, 6]])
        result = MatrixOperations.column_count(matrix)
        self.assertEquals(result, 3)

    def test_column_count_is_0(self):
        matrix = np.array([[]])
        result = MatrixOperations.column_count(matrix)
        self.assertEquals(result, 0)

    def test_column_count_is_1(self):
        matrix = np.array([[0]])
        result = MatrixOperations.column_count(matrix)
        self.assertEquals(result, 1)


if __name__ == '__main__':
    unittest.main()
