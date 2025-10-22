
import yfinance as yf


class YahooFinance:

    @staticmethod
    def get_stock_data(symbols):
        """Fetches stock data for given symbols and returns a sorted dictionary."""

        stock_data = {}

        for symbol in symbols:
            try:
                ticker = yf.Ticker(symbol)
                data = ticker.info
                stock_data[symbol] = {
                    'price': data.get('currentPrice'),
                    'marketCap': data.get('marketCap'),
                    'volume': data.get('volume')
                }
            except Exception:
                print(f"Error fetching data for {symbol}")

        # Sort the dictionary by stock price (descending)
        sorted_stock_data = dict(sorted(stock_data.items(), key=lambda item: item[1]['price'], reverse=True))

        return sorted_stock_data
