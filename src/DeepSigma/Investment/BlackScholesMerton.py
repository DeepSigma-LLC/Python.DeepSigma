import numpy as np
from scipy.stats import norm
from src.DeepSigma.Investment.Enums import OptionType
from typing import Optional


class BlackScholesMerton:
    def __init__(self, spot_price: float, strike_price: float, time_to_maturity: float, risk_free_rate: float,
                 volatility: float, continuous_dividend_yield: float = 0.0):
        self.spot_price: float = spot_price
        self.strike_price: float = strike_price
        self.time_to_maturity: float = time_to_maturity
        self.risk_free_rate: float = risk_free_rate
        self.continuous_dividend_yield: float = continuous_dividend_yield
        self.sigma: float = volatility
        self.__time_scaled_volatility: float = self.sigma * np.sqrt(self.time_to_maturity)
        self.__time_scaled_risk_free_rate: float = self.risk_free_rate * self.time_to_maturity
        self.__pv_discount_factor: float = np.exp(-self.__time_scaled_risk_free_rate)
        self.__dividend_yield_discount_factor: float = np.exp(-self.continuous_dividend_yield * self.time_to_maturity)
        self.__variance: float = self.sigma**2

    def calculate_price(self, option_type: OptionType) -> Optional[float]:
        """
        Calculates the price of an option.
        :param option_type:
        :return:
        """
        d1 = self.get_calculated_d1()
        d2 = self.get_calculated_d2()

        price: Optional[float] = None
        match option_type:
            case OptionType.Call:
                price = (self.spot_price * self.__dividend_yield_discount_factor * norm.cdf(d1)
                         - self.strike_price * self.__pv_discount_factor * norm.cdf(d2))
            case OptionType.Put:
                price = (self.strike_price * self.__pv_discount_factor * norm.cdf(-d2)
                         - self.spot_price * self.__dividend_yield_discount_factor * norm.cdf(d1) * norm.cdf(-d1))
            case _:
                raise ValueError("option_type must be 'call' or 'put'")
        return price

    def calculate_delta(self, option_type: OptionType) -> Optional[float]:
        d1: float = self.get_calculated_d1()
        match option_type:
            case OptionType.Call:
                return norm.cdf(d1)
            case OptionType.Put:
                return norm.cdf(d1) - 1
            case _:
                raise ValueError("option_type must be 'call' or 'put'")

    def get_calculated_d1(self) -> float:
        d1: float = (
                (np.log(self.spot_price / self.strike_price)
                 + (self.risk_free_rate - self.continuous_dividend_yield +  0.5 * self.__variance) * self.time_to_maturity
                 )
                / self.__time_scaled_volatility)
        return d1

    def get_calculated_d2(self) -> float:
        d1: float = self.get_calculated_d1()
        d2: float = (d1 - self.__time_scaled_volatility)
        return d2