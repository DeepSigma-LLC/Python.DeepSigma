from src import AlphaVantageBase
from src import AlphaVantageNewsSortType
from src import AlphaVantageSupportedNewTopics


class AlphaVantageUtilities(AlphaVantageBase):
    def __init__(self, api_key: str):
        pass

    @classmethod
    def get_ticker_search_results(cls, search_text: str):
        """
        The Search Endpoint returns the best-matching symbols and market information based on keywords of your choice.
        :param search_text:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + search_text
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_market_status(cls):
        """
        This endpoint returns the current market status (open vs. closed) of major trading venues
        for equities, forex, and cryptocurrencies around the world.
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=MARKET_STATUS"
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_etf_profiles(cls, ticker: str):
        """
        This API returns key ETF metrics (e.g., net assets, expense ratio, and turnover),
        along with the corresponding ETF holdings / constituents with allocation by asset types and sectors.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=ETF_PROFILE&symbol=" + ticker
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_top_gainers_lossers(cls):
        """
        This endpoint returns the top 20 gainers, losers, and the most active traded tickers in the US market.
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey="
               + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_news(cls, tickers: list[str], sort_type: AlphaVantageNewsSortType = AlphaVantageNewsSortType.LATEST,
                 result_limit: int = 50):
        url = ("https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers="
               + ','.join(tickers)
               + "&sort=" + sort_type.name
               + "&limit=" + result_limit
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_news(cls, topics: list[AlphaVantageSupportedNewTopics],
                 sort_type: AlphaVantageNewsSortType = AlphaVantageNewsSortType.LATEST,
                 result_limit: int = 50):
        url = ("https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers="
               + "&topics=" + ','.join(topic.name for topic in topics)
               + "&sort=" + sort_type.name
               + "&limit=" + result_limit
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)
