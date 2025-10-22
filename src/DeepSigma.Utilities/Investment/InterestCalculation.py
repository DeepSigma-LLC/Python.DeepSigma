"""Contains functions for interest calculations."""
import math


def simple_interest_rate(present_value: float, future_value: float) -> float:
    return future_value / present_value - 1

def geometric_interest_rate(present_value: float, future_value: float, periods: int) -> float:
    return (future_value/present_value)**(1/periods) - 1

def continuously_compounded_interest_rate(present_value: float, future_value: float, periods: int):
    return math.log(future_value/present_value)

