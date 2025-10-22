

def linear_approximation(y_0: float, delta_x: float, dx: float, dx_2: float = 0) -> float:
    return y_0 + dx * delta_x + (1/2) * dx_2 ** 2

def newtons_solution_approximation_method(equation, differential_equation, guessed_solution_for_x,
                                              digit_precision: int = 8, max_iteration: int = 2000):
    estimated_x = guessed_solution_for_x
    result = guessed_solution_for_x
    continue_search = True
    i = 0
    while continue_search:
        result = estimated_x - equation(estimated_x) / differential_equation(estimated_x)

        # Stop once the solutions desired precision is found as indicated by the approximation not improving.
        if round(result, digit_precision) == round(estimated_x, digit_precision):
            continue_search = False
        elif i > max_iteration:
            continue_search = False

        estimated_x = result
        i = i + 1
    return result

def euler_approximation_method(differential_equation, y_0: float, x_0: float,
                                   x_n: float, number_of_steps: int = 20) -> float:
    """
            Implementation of an iterative approximation method to an equation when we know the differential equation.
            This numerical method was developed by Euler.
            This method assumes the differential equation is only a function of x.
            The method will need to be modified to handle multi-variable differential equations.
            :param differential_equation:
            :param y_0: Initial value for y.
            :param x_0: Initial value for x.
            :param x_n: Target value for x.
            :param number_of_steps: Determines step size of the approximation. For continuous and
                differentiable functions, the smaller the step size the better the approximation.
            :return: Result of the iterative approximation.
            """
    step_size = (x_n - x_0) / number_of_steps
    x = x_0
    y_prior = y_0
    result = None
    i = 0
    while i < number_of_steps:
        result = y_prior + step_size * differential_equation(x)
        y_prior = result
        x = x + step_size
        i += 1
    return result
