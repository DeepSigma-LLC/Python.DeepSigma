from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageBase import AlphaVantageBase
from datetime import date
from src.MetaKit.Utilities.DateTimeUtilities import DateTimeUtilities

class AlphaVantageFundamentalData(AlphaVantageBase):

    def __init__(self, api_key: str):
        pass

    @classmethod
    def get_company_overview(cls, ticker: str):
        """
        Returns company overview for a given ticker.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=OVERVIEW&symbol=" + ticker + "&apikey="
               + super()._get_api_key())
        return cls._get_data_from_url(url)

    @classmethod
    def get_company_income_statement(cls, ticker: str):
        """
        Returns company income statement for a given ticker.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=" + ticker + "&apikey="
               + super()._get_api_key())
        return cls._get_data_from_url(url)

    @classmethod
    def get_company_balance_sheet(cls, ticker: str):
        """
        Returns company balance sheet for a given ticker.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=" + ticker + "&apikey="
               + super()._get_api_key())
        return cls._get_data_from_url(url)

    @classmethod
    def get_company_cash_flow(cls, ticker: str):
        """
        Returns company cash flow for a given ticker.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=CASH_FLOW&symbol=" + ticker + "&apikey="
               + super()._get_api_key())
        return cls._get_data_from_url(url)

    @classmethod
    def get_company_earnings(cls, ticker: str):
        """
        Returns company earnings for a given ticker.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=EARNINGS&symbol=" + ticker + "&apikey="
               + super()._get_api_key())
        return cls._get_data_from_url(url)

    @classmethod
    def get_company_dividends(cls, ticker: str):
        """
        Returns company dividends for a given ticker.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=DIVIDENDS&symbol=" + ticker + "&apikey="
               + super()._get_api_key())
        return cls._get_data_from_url(url)

    @classmethod
    def get_company_splits(cls, ticker: str):
        """
        Returns company stock splits for a given ticker.
        :param ticker:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=SPLITS&symbol=" +
               ticker + "&apikey=" + super()._get_api_key())
        return cls._get_data_from_url(url)

    @classmethod
    def get_insider_transactions(cls, ticker: str):
        url = ("https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&symbol="
               + ticker + "&apikey=" + super()._get_api_key())
        return cls._get_data_from_url(url)

    @classmethod
    def get_earnings_call_transcription(cls, ticker: str, selected_date: date):
        quarter = DateTimeUtilities.get_quarter(selected_date)
        url = ("https://www.alphavantage.co/query?function=EARNINGS_CALL_TRANSCRIPT&symbol=" + ticker +
               "&quarter=" + str(selected_date.year) + "Q" + str(quarter) +
               "&apikey=" + super()._get_api_key())
        return cls._get_data_from_url(url)
    