from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageBase import AlphaVantageBase
from src.MetaKit.DataAccess.AlphaVantage.Enums.AlphaVantageOutputSize import AlphaVantageOutputSize
from src.MetaKit.DataAccess.AlphaVantage.Enums.AlphaVantageTimeInterval import AlphaVantageTimeInterval


class AlphaVantageFX(AlphaVantageBase):
    def __init__(self, api_key: str):
        pass

    @classmethod
    def get_exchange_rate(cls, from_currency: str, to_currency: str):
        """
        Gets current exchange rate.
        :param from_currency:
        :param to_currency:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency="
               + from_currency + "&to_currency=" + to_currency
               + "&apikey="+super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_exchange_rates_intraday(cls, from_currency: str, to_currency: str,
                                    time_interval: AlphaVantageTimeInterval,
                                    output_size: AlphaVantageOutputSize = AlphaVantageOutputSize.compact):
        """
        Gets intraday exchange rates.
        :param from_currency:
        :param to_currency:
        :param time_interval:
        :param output_size:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol="
               + from_currency + "&to_symbol=" + to_currency
               + "&interval=" + time_interval.value
               + "&outputsize=" + output_size.name
               + "&apikey="+super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_exchange_rates_daily(cls, from_currency: str, to_currency: str,
                                 output_size: AlphaVantageOutputSize = AlphaVantageOutputSize.compact):
        """
        Gets daily exchange rates.
        :param from_currency:
        :param to_currency:
        :param output_size:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=FX_DAILY&from_symbol="
               + from_currency + "&to_symbol=" + to_currency + "&outputsize=" + output_size.name
               + "&apikey="+super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_exchange_rates_weekly(cls, from_currency: str, to_currency: str,
                                  output_size: AlphaVantageOutputSize = AlphaVantageOutputSize.compact):
        """
        Gets weekly exchange rates.
        :param from_currency:
        :param to_currency:
        :param output_size:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol="
               + from_currency + "&to_symbol=" + to_currency + "&outputsize=" + output_size.name
               + "&apikey="+super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_exchange_rates_monthly(cls, from_currency: str, to_currency: str,
                                   output_size: AlphaVantageOutputSize = AlphaVantageOutputSize.compact):
        """
        Gets monthly exchange rates.
        :param from_currency:
        :param to_currency:
        :param output_size:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol="
               + from_currency + "&to_symbol=" + to_currency + "&outputsize=" + output_size.name
               + "&apikey="+super()._get_api_key())
        return super()._get_data_from_url(url)
