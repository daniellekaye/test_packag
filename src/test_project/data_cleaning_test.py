import pandas as pd

path = r'test_package\data\sp500_stocks.csv'
df = pd.read_csv(path)

# remove null values
df.dropna(inplace = True)

# print(df.tail(20))

#find companies with values for all dates
startDate = df['Date'].min()
startDate = pd.to_datetime(startDate)
#print("start: " + str(startDate))

endDate = df['Date'].max()
endDate = pd.to_datetime(endDate)
#print("end: " + str(endDate))

dateRange = endDate - startDate
print("range: " + str(dateRange))

countOfDays = df.groupby('Symbol')['Date'].nunique()
#print(countOfDays)

# print(f"Data ranges from {startDate} to {endDate}")