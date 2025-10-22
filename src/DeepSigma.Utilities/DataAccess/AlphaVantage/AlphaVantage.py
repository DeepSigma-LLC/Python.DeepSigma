import datetime
import requests
import pandas as pd
from src.MetaKit.Utilities.DataUtilities import DataFrameUtilities
from src.MetaKit.Utilities.StringUtilities import StringUtilties
from src.MetaKit.DataAccess.AlphaVantage import AlphaVantageBase
from src.MetaKit.DataAccess.AlphaVantage.Enums import AlphaVantageTimeInterval


class AlphaVantageOGAPI(AlphaVantageBase):


    def get_daily_stock_data(self, ticker: str) -> pd.DataFrame:
        # API_URL = "https://www.alphavantage.co/query"
        # data = {"function": "TIME_SERIES_DAILY",
             # "symbol": ticker,
             # "outputsize" : "full",
             ## "datatype": "json",
             # "apikey": self._api_key}
        # response = requests.get(API_URL, data)

        api_url = ('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' +
                   ticker + '&apikey=' + self._api_key)
        dataframe = self.__get_data_frame_from_query(api_url, 'Time Series (Daily)')
        return dataframe

    def get_intraday_stock_data(self, ticker: str, time_interval: AlphaVantageTimeInterval) -> pd.DataFrame:
        api_url = ('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker +
                   '&interval=' + AlphaVantageOGAPI.__get_time_interval(time_interval)
                   + '&apikey=' + self._api_key)
        dataframe = self.__get_data_frame_from_query(api_url, 'Time Series (5min)')
        return dataframe

    def get_stock_quote_snapshot(self, ticker: str) -> pd.DataFrame:
        api_url = ('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' +
                   ticker + '&apikey=' + self._api_key)
        dataframe = self.__get_data_frame_from_query(api_url, 'Global Quote')
        return dataframe

    def ticker_search(self, search_string: str):
        raise NotImplementedError()

    def global_market_status(self):
        raise NotImplementedError()

    def historical_option(self, ticker: str, date: datetime):
        api_url = ('https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol=' + ticker +
                   '&date=' + date.strftime('%Y-%m-%d') +'&apikey=' + self._api_key)
        dataframe = self.__get_data_frame_from_query(api_url, 'data')
        return dataframe

    def option_realtime(self, ticker: str):
        api_url = 'https://www.alphavantage.co/query?function=REALTIME_OPTIONS&symbol=IBM&apikey=demo'

    @staticmethod
    def __get_time_interval(time_interval: AlphaVantageTimeInterval):
        raise NotImplementedError()

    def __get_data_frame_from_query(self, query: str, target_api_response_index: str):
        response = requests.get(query)
        response_json = response.json()
        self.__save_last_api_response(response_json)
        dataframe = pd.DataFrame
        if target_api_response_index == 'Global Quote':
            dataframe = pd.DataFrame(response_json)
            dataframe.reset_index(inplace=True)

        else:
            dataframe = pd.DataFrame.from_dict(response_json[target_api_response_index], orient='index').sort_index(axis=1)
        original_field_names = dataframe.columns.tolist()
        print(original_field_names)
        new_field_names = [AlphaVantageOGAPI.__field_reformat(field) for field in original_field_names]
        dataframe = DataFrameUtilities.update_dataframe_field_names(dataframe, original_field_names, new_field_names)
        # dataframe = DataFrameUtilities.update_dataframe_datatypes(dataframe)
        return dataframe


    @staticmethod
    def __field_reformat(field: str) -> str:
        new_field = StringUtilties.remove_all_numbers(field)
        new_field = StringUtilties.remove_all_spaces(new_field)
        new_field = new_field.replace('.', '')
        new_field = StringUtilties.capitalize_each_word(new_field)
        return new_field
