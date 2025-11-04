import pandas as pd

path = "test_package\data\sp500_companies.csv"
df = pd.read_csv(path)

print(df.head())