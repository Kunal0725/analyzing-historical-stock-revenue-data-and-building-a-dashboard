import pandas as pd

# Load Tesla stock data from CSV file
tesla_data = pd.read_csv('gme_stock_data.csv')

# Display last five rows using tail function
last_five_rows = tesla_data.tail()

# Print the last five rows to console
print(last_five_rows)

# Save a screenshot of the console output
# Since I can't directly save screenshots, you'll need to manually capture the output or use a screen capture tool

# Example: Saving the last five rows to a new CSV file (optional)
last_five_rows.to_csv('gme_last_five_rows.csv', index=False)
