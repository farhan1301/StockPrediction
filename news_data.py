import requests
import json

api_key = 'LOFJ46CQ1HDPYDE4'  # Replace with your actual API key
url = 'https://www.alphavantage.co/query'  # Replace with the API URL

params = {
    'function': 'NEWS_SENTIMENT',
    'time_from': '20180101T0000',
    'time_to': '20220307T0730',
    'sort': 'LATEST',
    'limit': '200',
    'tickers': 'IBM',
    'apikey': api_key
}

response = requests.get(url, params=params)
data = response.json()

# Format the data for better readability
formatted_data = json.dumps(data, indent=4)

# Save the formatted data to a separate file
with open('news_data6.json', 'w') as file:
    file.write(formatted_data)

print("Data saved to 'news_data.json' file.")
