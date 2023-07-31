import requests
import json

api_key = 'LOFJ46CQ1HDPYDE4'  # Replace with your actual API key
url = 'https://www.alphavantage.co/query'  # Replace with the API URL

params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'IBM',
    'outputsize': 'full',
    'datatype': 'json',
    'apikey': api_key
}

response = requests.get(url, params=params)
data = response.json()

# Format the data for better readability
formatted_data = json.dumps(data, indent=4)

# Save the formatted data to a separate file
with open('stock_data.json', 'w') as file:
    file.write(formatted_data)

print("Data saved to 'stock_data.json' file.")