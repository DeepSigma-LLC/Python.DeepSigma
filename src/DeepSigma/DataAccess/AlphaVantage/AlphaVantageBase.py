import datetime
import requests


class AlphaVantageBase:
    __last_response_message = ""
    __api_key = "demo"

    def __int__(self, api_key: str):
        self.reset_api_key(api_key)

    @classmethod
    def reset_api_key(cls, api_key: str):
        cls.__api_key = api_key

    @classmethod
    def get_last_api_response_message(cls):
        return cls.__last_response_message

    @classmethod
    def _get_data_from_url(cls, url: str):
        result = requests.get(url)
        cls.__save_last_api_response(result)
        return result.json()

    @classmethod
    def _get_api_key(cls) -> str:
        return cls.__api_key

    @classmethod
    def __save_last_api_response(cls, response: str):
        cls.__last_response_message = response
