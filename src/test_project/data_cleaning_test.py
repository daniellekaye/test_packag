import pandas as pd
import datetime

def clean_data():
    path = r'test_package\data\sp500_stocks.csv'
    df = pd.read_csv(path)

    # remove rows with empty cells
    df.dropna(inplace=True)

    # change strings to date time
    df['Date'] = pd.to_datetime(df['Date'])

    # set data frame index to date
    df.set_index('Date', inplace=True)

    # set start and end date
    start_date = datetime.datetime(2014, 1, 1)
    end_date = datetime.datetime(2024, 12, 20)

    # filter data frame to only include data within the date range
    mask = (df.index >= start_date) & (df.index <= end_date)
    df = df.loc[mask]
    return df

def tech_data_only():
    path = r'test_package\data\sp500_companies.csv'
    df = pd.read_csv(path)
    df.dropna(inplace=True)

    #set df index to sector
    sector_df = df.set_index('Sector')

    #filter to only technology sector
    tech_df = sector_df.loc['Technology']

    #save all company symbols in a list
    tech_symbols = tech_df['Symbol'].tolist()

    #clean stock data
    stock_df = clean_data()

    #make mask of only technology company stocks
    tech_stock_df = stock_df[stock_df['Symbol'].isin(tech_symbols)]

    return tech_stock_df

# test_df = tech_data_only()
# print(test_df)

