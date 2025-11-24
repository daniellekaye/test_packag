import pandas as pd
import datetime
from data_cleaning_test import clean_data, tech_data_only, clean_tech_company_dataset
from attributes import calculate_price_volatility, calculate_trading_volume, calculate_PE_ratio

tech_df = tech_data_only()
tech_company_df = clean_tech_company_dataset()

#print out values for 3 attributes
volatility = calculate_price_volatility(tech_df)
print(f"Mean Price Volatility: {volatility}")
trading_volume = calculate_trading_volume(tech_df)
print(f"Mean Trading Volume: {trading_volume}")
pe_ratio = calculate_PE_ratio(tech_company_df)
print(f"Mean P/E Ratio: {pe_ratio}")