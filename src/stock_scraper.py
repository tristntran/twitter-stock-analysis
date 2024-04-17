import yfinance as yf

def get_stock_data(ticker:str, start_date:str, end_date: str):
    """Gets stock data within the 
    date range for the given ticker

    Args:
        ticker (_type_): The stock ticker
        start_date (_type_): The start date YYYY-MM-DD
        end_date (_type_): The end date YYYY-MM-DD

    Returns:
        _type_: _description_
    """
    data = yf.download(ticker, start_date, end_date)
    return data

if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2019-04-15"
    end_date = "2024-04-15"
    stock_data = get_stock_data(ticker, start_date, end_date)
    print(stock_data)