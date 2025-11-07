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

#test_df = clean_data()
#print(test_df)

