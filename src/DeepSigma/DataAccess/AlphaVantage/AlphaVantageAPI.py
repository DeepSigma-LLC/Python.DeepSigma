from src import AlphaVantageBase
from src import AlphaVantageFundamentalData
from src import AlphaVantageFX
from src import AlphaVantageStockData
from src import AlphaVantageEconomicData
from src import AlphaVantageCommodityData
from src import AlphaVantageOptionData
from src import AlphaVantageCrypto
from src import AlphaVantageUtilities
from src import AlphaVantageFixedIncomeData


class AlphaVantageAPI(AlphaVantageBase):
    def __init__(self, api_key: str):
        self.Stocks = AlphaVantageStockData(api_key)
        self.FixedIncome = AlphaVantageFixedIncomeData(api_key)
        self.Options = AlphaVantageOptionData(api_key)
        self.FX = AlphaVantageFX(api_key)
        self.Crypto = AlphaVantageCrypto(api_key)
        self.Commodities = AlphaVantageCommodityData(api_key)
        self.Fundamentals = AlphaVantageFundamentalData(api_key)
        self.Economics = AlphaVantageEconomicData(api_key)
        self.Utilities = AlphaVantageUtilities(api_key)
        pass
