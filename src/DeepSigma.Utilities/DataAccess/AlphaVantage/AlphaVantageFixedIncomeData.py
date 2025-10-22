from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageBase import AlphaVantageBase
from src.MetaKit.DataAccess.AlphaVantage.Enums.AlphaVantagePeriodicityInterval import AlphaVantagePeriodicityInterval
from src.MetaKit.DataAccess.AlphaVantage.Enums.AlphaVantageTreasuryMaturities import AlphaVantageTreasuryMaturities


class AlphaVantageFixedIncomeData(AlphaVantageBase):
    def __init__(self, api_key: str):
        pass

    @classmethod
    def get_federal_funds_rate(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the daily, weekly, and monthly federal funds rate (interest rate) of the United States.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_us_treasury_yields(cls, maturity: AlphaVantageTreasuryMaturities,
                               periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the daily, weekly, and monthly US treasury yield of a given maturity timeline
        (e.g., 5 year, 30 year, etc).
        :param maturity:
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=" + periodicity.name
               + "&maturity=" + maturity.value
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)


