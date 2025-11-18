import pandas as pd
import datetime
from data_cleaning_test import clean_data, tech_data_only

def calculate_price_volatility(df):
    """
    Calculate the mean price volatility for all stocks in the DataFrame.
    Volatility is defined as the standard deviation of the closing prices.
    """

    #calculate individual volatility for each stock
    volatility = df.groupby('Symbol')['Close'].std().reset_index()
    volatility.columns = ['Symbol', 'price_volatility']

    #calculate average volatility for all stocks
    avg_volatility = volatility['price_volatility'].mean()

    #round to 3 decimal places
    avg_volatility = round(avg_volatility, 3)

    return avg_volatility

def calculate_trading_volume(df):
    """
    Calculate the mean trading volume for all stocks in the DataFrame.
    """

    #calculate individual average trading volume for each stock
    avg_volume = df.groupby('Symbol')['Volume'].mean().reset_index()
    avg_volume.columns = ['Symbol', 'avg_trading_volume']

    #calculate overall average trading volume
    overall_avg_volume = avg_volume['avg_trading_volume'].mean()
   
   #round to 3 decimal places
    overall_avg_volume = round(overall_avg_volume, 3)

    return overall_avg_volume


def calculate_PE_ratio(df):
    """
    Calculate the mean P/E ratio for all stocks in the DataFrame.
    P/E ratio, in this circumstance, is a company's market cap divided by its EBITDA.
    """
    #calculate individual P/E ratio for each stock
    pe_ratio = df.groupby('Symbol').apply(lambda x: x['Marketcap'].iloc[0] / x['EBITDA'].iloc[0] if x['EBITDA'].iloc[0] != 0 else None).reset_index()
    pe_ratio.columns = ['Symbol', 'PE_ratio']
    