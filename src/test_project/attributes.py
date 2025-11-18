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
    return overall_avg_volume

def calculare_PE_ratio(df):
    """
    Calculate the mean P/E ratio for all stocks in the DataFrame.
    P/E ratio is defined as the closing price divided by earnings per share (EPS).
    """

    #calculate individual P/E ratio for each stock
    df['PE_ratio'] = df['Close'] / df['EPS']
    pe_ratio = df.groupby('Symbol')['PE_ratio'].mean().reset_index()
    pe_ratio.columns = ['Symbol', 'avg_PE_ratio']

    #calculate overall average P/E ratio
    overall_avg_pe_ratio = pe_ratio['avg_PE_ratio'].mean()
    return overall_avg_pe_ratio