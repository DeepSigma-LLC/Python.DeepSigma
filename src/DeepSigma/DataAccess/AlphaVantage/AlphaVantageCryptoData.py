from src import AlphaVantageBase
from src import AlphaVantageOutputSize
from src import AlphaVantageTimeInterval


class AlphaVantageCrypto(AlphaVantageBase):
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
               + "&apikey=" + super()._get_api_key())
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
        url = ("https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol="
               + from_currency + "&market=" + to_currency
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
        url = ("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol="
               + from_currency + "&market=" + to_currency + "&outputsize=" + output_size.name
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
        url = ("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol="
               + from_currency + "&market=" + to_currency + "&outputsize=" + output_size.name
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
        url = ("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol="
               + from_currency + "&market=" + to_currency + "&outputsize=" + output_size.name
               + "&apikey="+super()._get_api_key())
        return super()._get_data_from_url(url)
