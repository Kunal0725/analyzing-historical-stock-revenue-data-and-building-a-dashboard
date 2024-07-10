import yfinance as yf

# Extracting Tesla stock data
tesla_data = yf.download('TSLA', start='2023-01-01', end='2023-12-31')

# Reset index
tesla_data.reset_index(inplace=True)

# Display the first five rows
print(tesla_data.head())

# Save the dataframe to a file (e.g., CSV)
tesla_data.to_csv('tesla_stock_data.csv', index=False)
