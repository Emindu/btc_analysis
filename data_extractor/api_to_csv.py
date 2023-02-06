import requests
import csv

btc_url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h"
ethbtc = "https://api.binance.com/api/v3/klines?symbol=ETHBTC&interval=1h"

start_epoc_time = 1514772000000
epoc_hour_epoc_time = 3600000000
number_of_itr = 44

btc_url_start_url = "https://api.binance.com/api/v3/klines?symbol=ETHBTC&interval=1h&limit=1000&startTime="
saved_data = []

for i in range(number_of_itr):
    print(i)
    req_url = btc_url_start_url + str(start_epoc_time)
    print(req_url)
    response = requests.get(req_url)
    if response.status_code == 200:
        market_data = response.json()
        print(type(market_data))
        saved_data.extend(market_data)
    start_epoc_time = start_epoc_time  + (epoc_hour_epoc_time)

print("completed")
print(len(saved_data))

with open("../market_data_eth_btc.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(
        ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades",
         "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"])
    # Write the market data
    for row in saved_data:
        writer.writerow(row)

#
#
# #https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=1000 - endpoit for funding rate
# #https://fapi.binance.com/fapi/v1/klines?symbol=BTCUSDT&interval=1d&startTime=1580836177000 - endpoit  for future data
#
# # Make the API request
# response = requests.get(url)
#
# # Check if the request was successful
# if response.status_code == 200:
#     # Convert the API response to a list of lists
#     market_data = response.json()
#     # Create a new CSV file

