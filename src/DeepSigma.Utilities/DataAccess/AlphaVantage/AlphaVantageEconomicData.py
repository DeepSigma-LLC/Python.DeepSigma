from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageBase import AlphaVantageBase
from src.MetaKit.DataAccess.AlphaVantage.Enums.AlphaVantagePeriodicityInterval import AlphaVantagePeriodicityInterval


class AlphaVantageEconomicData(AlphaVantageBase):
    def __init__(self, api_key: str):
        pass

    @classmethod
    def get_us_real_gdp(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the annual and quarterly Real GDP of the United States.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=REAL_GDP&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_us_real_gdp_per_capita(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the quarterly Real GDP per Capita data of the United States.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_us_cpi(cls, periodicity: AlphaVantagePeriodicityInterval):
        """
        This API returns the monthly and semiannual consumer price index (CPI) of the United States.
        CPI is widely regarded as the barometer of inflation levels in the broader economy.
        :param periodicity:
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=CPI&interval=" + periodicity.name
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_us_inflation(cls):
        """
        This API returns the annual inflation rates (consumer prices) of the United States.
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=INFLATION"
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_us_retail_sales(cls):
        """
        This API returns the monthly Advance Retail Sales: Retail Trade data of the United States.
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=RETAIL_SALES"
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_us_durable_goods_orders(cls):
        """
        This API returns the monthly manufacturers' new orders of durable goods in the United States.
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=DURABLES"
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_us_unemployment(cls):
        """
        This API returns the monthly unemployment data of the United States.
        The unemployment rate represents the number of unemployed as a percentage of the labor force.
        Labor force data are restricted to people 16 years of age and older,
        who currently reside in 1 of the 50 states or the District of Columbia,
        who do not reside in institutions (e.g., penal and mental facilities, homes for the aged),
        and who are not on active duty in the Armed Forces
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=UNEMPLOYMENT"
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)

    @classmethod
    def get_us_non_farm_payroll(cls):
        """
        This API returns the monthly US All Employees:
        Total Nonfarm (commonly known as Total Nonfarm Payroll),
        a measure of the number of U.S. workers in the economy that excludes proprietors,
        private household employees, unpaid volunteers, farm employees, and the unincorporated self-employed.
        :return:
        """
        url = ("https://www.alphavantage.co/query?function=NONFARM_PAYROLL"
               + "&apikey=" + super()._get_api_key())
        return super()._get_data_from_url(url)
