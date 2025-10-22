from src import AlphaVantageBase
from datetime import date


class AlphaVantageOptionData(AlphaVantageBase):
    def __init__(self, api_key: str):
        pass

    @classmethod
    def get_option_data_historical(cls, ticker: str, selected_date: date):
        """
        This API returns the full historical options chain for a specific symbol on a specific date.
        Implied volatility (IV) and common Greeks (e.g., delta, gamma, theta, vega, rho) are also returned.
        :param ticker:
        :param selected_date:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol=" + ticker +
               "&date=" + selected_date +
               "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_option_data_realtime(cls, ticker: str, require_greeks: bool = True):
        """
        This API returns realtime US options data with full market coverage.
        :param ticker:
        :param require_greeks:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=REALTIME_OPTIONS&symbol=" +
               ticker +
               "&require_greeks=" + str(require_greeks).lower() +
               "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_option_data_realtime(cls, ticker: str, contract: str, require_greeks: bool = True):
        """
        This API returns realtime US options data with full market coverage.
        :param ticker:
        :param contract:
        :param require_greeks:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=REALTIME_OPTIONS&symbol=" +
               ticker + "&require_greeks=" + str(require_greeks).lower() +
               "&contract=" + contract + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

