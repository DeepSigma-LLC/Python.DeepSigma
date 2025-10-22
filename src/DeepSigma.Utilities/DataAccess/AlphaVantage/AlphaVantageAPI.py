from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageBase import AlphaVantageBase
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageFundamentalData import AlphaVantageFundamentalData
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageFX import AlphaVantageFX
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageStockData import AlphaVantageStockData
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageEconomicData import AlphaVantageEconomicData
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageCommodityData import AlphaVantageCommodityData
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageOptionData import AlphaVantageOptionData
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageCryptoData import AlphaVantageCrypto
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageUtilities import AlphaVantageUtilities
from src.MetaKit.DataAccess.AlphaVantage.AlphaVantageFixedIncomeData import AlphaVantageFixedIncomeData


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
