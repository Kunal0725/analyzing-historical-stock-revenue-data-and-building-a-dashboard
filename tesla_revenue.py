import pandas as pd

# Load stock data from CSV file
tesla_data = pd.read_csv('tesla_stock_data.csv')

# Display first five rows to verify data
print(tesla_data.head())

# Optionally, reset index if needed
tesla_data.reset_index(drop=True, inplace=True)

# Optionally, perform further analysis or processing on the data
# For example, calculate some statistics or visualize the data

# Example: Calculate mean of 'Close' prices
mean_close_price = tesla_data['Close'].mean()
print(f"Mean Close Price: ${mean_close_price:.2f}")

# Example: Visualize 'Close' prices over time (requires matplotlib or other plotting libraries)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(tesla_data['Date'], tesla_data['Close'], marker='o', linestyle='-')
plt.title('Tesla Stock Close Prices')
plt.xlabel('Date')
plt.ylabel('Close Price ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
