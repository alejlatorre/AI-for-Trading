import pandas as pd
import numpy as np

IN_PATH = 'data/'

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    prices_sd = prices.groupby(['ticker'])['price'].std()
    most_volatile = prices_sd.nlargest(1).index[0]

    return most_volatile

def test_run(filename):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    filename = 'prices.csv'
    test_run(filename=IN_PATH + filename)