from src import AlphaVantageBase
from src import AlphaVantageOutputSize
from src import AlphaVantageTimeInterval
from datetime import date

class AlphaVantageStockData(AlphaVantageBase):
    def __init__(self, api_key: str):
        pass

    @classmethod
    def get_price_quotes_realtime_bulk_request(cls, tickers: list[str]):
        """
        This API returns realtime quotes for US-traded symbols in bulk,
        accepting up to 100 symbols per API request and covering both regular and extended
        (pre-market and post-market) trading hours.
        :param tickers:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=REALTIME_BULK_QUOTES&symbol=" +
               ",".join(tickers)
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_price_quotes_realtime(cls, ticker: str):
        """
        This endpoint returns the latest price and volume information for a ticker of your choice.
        You can specify one ticker per API request.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + ticker
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)


    @classmethod
    def get_prices_intraday(cls, ticker: str, selected_date: date,
                            time_interval: AlphaVantageTimeInterval,
                            extended_hours: bool = False,
                            adjusted: bool = True,
                            output_size: AlphaVantageOutputSize = AlphaVantageOutputSize.compact):
        """
        Gets intraday price candles.
        :param ticker:
        :param selected_date:
        :param time_interval:
        :param extended_hours:
        :param adjusted:
        :param output_size:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="
               + ticker
               + "&interval=" + time_interval.value
               + "&month=" + str(selected_date.year) + "-" + str(selected_date.month)
               + "&extended_hours=" + str(extended_hours).lower()
               + "&adjusted=" + str(adjusted).lower()
               + "&outputsize=" + output_size.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_prices_daily(cls, ticker: str,
                         adjusted: bool = True,
                         output_size: AlphaVantageOutputSize = AlphaVantageOutputSize.compact):
        """
        Gets daily price candles.
        :param ticker:
        :param adjusted:
        :param output_size:
        :return:
        """
        function_text = cls.__update_function("TIME_SERIES_DAILY", adjusted)
        url = ("https://www.alphavantage.co/query?function=" + function_text
               + "&symbol=" + ticker
               + "&outputsize=" + output_size.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_prices_monthly(cls, ticker: str, adjusted: bool = True):
        """
        Gets monthly price candles.
        :param ticker:
        :param adjusted:
        :return:
        """
        function_text = cls.__update_function("TIME_SERIES_MONTHLY", adjusted)
        url = ("https://www.alphavantage.co/query?function=" + function_text
               + "&symbol=" + ticker
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_prices_weekly(cls, ticker: str, adjusted: bool = True):
        """
        Gets weekly price candles.
        :param ticker:
        :param adjusted:
        :return:
        """
        function_text = cls.__update_function("TIME_SERIES_WEEKLY", adjusted)
        url = ("https://www.alphavantage.co/query?function=" + function_text + "&symbol=" + ticker
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @staticmethod
    def __update_function(function: str, adjusted: bool):
        if adjusted:
            return function + "_ADJUSTED"
        return function

