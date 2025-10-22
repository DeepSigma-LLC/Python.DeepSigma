from src import AlphaVantageBase
from src import AlphaVantagePeriodicityInterval

class AlphaVantageCommodityData(AlphaVantageBase):
    def __init__(self, api_key: str):
        pass

    @classmethod
    def get_wti_crude_oil_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the West Texas Intermediate (WTI) crude oil prices in
        daily, weekly, and monthly horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=WTI&interval=" + periodicity.name
              + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_brent_oil_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the Brent (Europe) crude oil prices in daily, weekly, and monthly horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=BRENT&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_natural_gas_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the Henry Hub natural gas spot prices in daily, weekly, and monthly horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=NATURAL_GAS&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_copper_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the global price of copper in monthly, quarterly, and annual horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=COPPER&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_aluminum_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the global price of aluminum in monthly, quarterly, and annual horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=ALUMINUM&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_wheat_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the global price of wheat in monthly, quarterly, and annual horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=WHEAT&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_corn_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the global price of corn in monthly, quarterly, and annual horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=CORN&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_cotton_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the global price of cotton in monthly, quarterly, and annual horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=COTTON&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_sugar_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the global price of sugar in monthly, quarterly, and annual horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=SUGAR&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_coffee_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the global price of coffee in monthly, quarterly, and annual horizons.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=COFFEE&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_commodity_index_prices(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the global price index of all commodities in
        monthly, quarterly, and annual temporal dimensions.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)
