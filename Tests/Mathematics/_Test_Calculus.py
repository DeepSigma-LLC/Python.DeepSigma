import unittest
from src.MetaKit.Mathematics import Calculus


class TestCalculus(unittest.TestCase):

    def test_linear_approximation_is_1(self):
        x_0 = 0
        dx = 1
        x_1 = 1
        dx_2 = 0
        result = Calculus.linear_approximation(x_0, x_1, dx, dx_2)
        self.assertEquals(result, 1)

    def test_linear_approximation_is_0(self):
        x_0 = 0
        dx = 0
        x_1 = 1
        dx_2 = 0
        result = Calculus.linear_approximation(x_0, x_1, dx, dx_2)
        self.assertEquals(result, 0)

    def test_linear_approximation_is_4(self):
        # assume y = x^2 and x = 0. We want to estimate y where x = 2
        x_0 = 0
        x_1 = 1
        dx = 2
        dx_2 = 2
        result = Calculus.linear_approximation(x_0, x_1, dx, dx_2)
        self.assertEquals(result, 4)

    def test_Euler_approximation_method_rounded_result_is_9(self):
        # assume y = x^2. Then the differential equation is dx = 2x
        result = Calculus.euler_approximation_method(self.differential_eq, 0, 0, 3, 40)
        result = round(result, 0)
        self.assertEquals(result, 9)

    @staticmethod
    def differential_eq(x: float):
        return 2*x

    def test_newton_solution_approximation_method(self):
        # assume y = x^6 + 2. Therefore, dx = 6x^5
        required_precision = 7
        result = Calculus.newtons_solution_approximation_method(self.equation_1, self.diff_eq_of_eq_1,
                                                                1, required_precision)
        self.assertEquals(round(result, required_precision), round(1.12246205,required_precision))

    @staticmethod
    def equation_1(x: float):
        return x**6 - 2

    @staticmethod
    def diff_eq_of_eq_1(x: float):
        return 6*(x**5)

if __name__ == '__main__':
    unittest.main()
