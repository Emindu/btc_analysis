import requests
import csv

url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the API response to a list of lists
    market_data = response.json()
    # Create a new CSV file
    with open("market_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"])
        # Write the market data
        for row in market_data:
            writer.writerow(row)
