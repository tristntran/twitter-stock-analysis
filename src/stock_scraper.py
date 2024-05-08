"""
This module scrapes stock data from Yahoo Finance
"""
import yfinance as yf
import pandas as pd


def get_stock_data(ticker: str, start_date: str, end_date: str):
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


def scrape_stocks_from_dict(
    stocks_names_tickers, start_date: str = "2021-01-01", end_date: str = "2021-12-31"
):
    """Scrapes stock data for a dictionary of stock tickers and names

    Args:
        stocks_dict (_type_): _description_
        start_date (str, optional): _description_. Defaults to "2021-01-01".
        end_date (str, optional): _description_. Defaults to "2021-12-31".

    Returns:
        _type_: _description_
    """
    all_data_list = []
    for ticker, name in stocks_names_tickers.items():
        print(f"{name} ({ticker})")
        data = get_stock_data(ticker, start_date=start_date, end_date=end_date)
        data["name"] = name
        all_data_list.append(data)

    all_data = pd.concat(all_data_list)
    all_data["date"] = all_data.index.to_series()
    return all_data


if __name__ == "__main__":
    stocks_dict = {
        "GME": "GameStop",
        "AAPL": "Apple",
        "AMC": "AMC",
        "BB": "BlackBerry",
        "NOK": "Nokia",
        "NVDA": "Nvidia",
        "PLTR": "Palantir",
        "TSLA": "Tesla",
        "SPY": "SPY",
        "^GSPC": "S&P 500",
    }
    scrape_stocks_from_dict(stocks_dict).to_csv("stocks.csv")
