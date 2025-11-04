import pandas as pd

path = r'test_package\data\sp500_stocks.csv'
df = pd.read_csv(path)

#remove rows with empty cells
df.dropna(inplace=True)

# change to date time
df['Date'] = pd.to_datetime(df['Date'])

#set data frame index to date
df.set_index('Date', inplace=True)

#find start and end dates
start_date = df.index.min()
end_date = df.index.max()
print(f"Data ranges from {start_date} to {end_date}")

# Find which dates have 501 entries, then restrict df to that range