import pandas as pd

path = r'test_package\data\sp500_stocks.csv'
df = pd.read_csv(path)

df.dropna(inplace = True)

print(df.head(20))