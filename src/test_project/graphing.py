import pandas as pd
import matplotlib.pyplot as plt
from data_cleaning_test import clean_data
import datetime

#clean the data
df = clean_data()
#print(df)

#print available stock symbols
available_symbols = df['Symbol'].unique()
print("Available stock symbols:", available_symbols)
user_input = input("Enter a stock symbol from the above list: ")

if user_input not in available_symbols:
    print("Invalid stock symbol. Please run the program again and enter a valid symbol.")
    exit()

#choose a stock symbol to plot
selected_symbol = user_input
symbol_data = df[df['Symbol'] == selected_symbol]

#get start and end date from the data
end_date = symbol_data.index.max()
start_date = symbol_data.index.min()
#print(f"Data for {selected_symbol} from {start_date.date()} to {end_date.date()}")

#resample to monthly average closing prices over the last 10 years
full_data = symbol_data.loc[start_date:end_date]
monthly_data = full_data['Close'].resample('ME').mean()

#plot the data
plt.figure(figsize=(12, 6))
plt.plot(monthly_data.index, monthly_data.values)
plt.title(f'{selected_symbol} Closing Prices - Last 10 Years (Monthly Avg)')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.grid(True)
plt.tight_layout()
plt.show()