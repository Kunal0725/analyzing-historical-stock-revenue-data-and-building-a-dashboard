import pandas as pd
import matplotlib.pyplot as plt

# Function to make a graph (hypothetical example)
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'], marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price ($)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Load gme stock data from CSV file
gme_data = pd.read_csv('gme_stock_data.csv')

# Call make_graph function
make_graph(gme_data, 'gme Stock Prices')

# Save screenshot of the graph displayed
# Since I can't directly save screenshots, you'll need to manually capture the graph or use a screen capture tool
