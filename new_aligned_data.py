import json
from datetime import datetime

# Read data from data.json
with open('stock_data.json', 'r') as file:
    json_data_1 = file.read()

# Read data from data1.json
with open('news_data.json', 'r') as file:
    json_data_2 = file.read()
    
# Parse JSON data 1
data_1 = json.loads(json_data_1)

# Parse JSON data 2
data_2 = json.loads(json_data_2)

# Initialize a dictionary to store the aligned data for IBM
aligned_data = {}

# Iterate over each time series data point
for date, time_series_data in data_1["Time Series (Daily)"].items():
    # Check if the date exists in the second dataset
    formatted_date = datetime.strptime(date, "%Y-%m-%d")
    formatted_date_str = formatted_date.strftime("%Y%m%d")

    # Find the IBM sentiment data for the corresponding date and ticker
    ibm_sentiment_data = next(
        (item for item in data_2["feed"] if item["time_published"].startswith(formatted_date_str)
         for ticker in item.get("ticker_sentiment", []) if ticker["ticker"] == "IBM"), None
    )

    if ibm_sentiment_data is not None:
        # Extract relevant information from data 1
        open_price = time_series_data["1. open"]
        high_price = time_series_data["2. high"]
        low_price = time_series_data["3. low"]
        close_price = time_series_data["4. close"]
        volume = time_series_data["6. volume"]

        # Calculate overall sentiment score
        sentiment_scores = [ticker["ticker_sentiment_score"] for ticker in ibm_sentiment_data.get("ticker_sentiment", []) if ticker["ticker"] == "IBM"]
        sentiment_weights = [float(ticker["relevance_score"]) for ticker in ibm_sentiment_data.get("ticker_sentiment", []) if ticker["ticker"] == "IBM"]

        if sentiment_scores and sentiment_weights:
            # Calculate weighted average of sentiment scores
            weighted_score = sum(float(score) * float(weight) for score, weight in zip(sentiment_scores, sentiment_weights))
            overall_sentiment_score = weighted_score / sum(sentiment_weights)

            # Create a dictionary to store the aligned data for the current date
            aligned_data[date] = {
                "Open Price": open_price,
                "High Price": high_price,
                "Low Price": low_price,
                "Close Price": close_price,
                "Volume": volume,
                "Overall Sentiment Score": overall_sentiment_score
            }

# Save the aligned data to a JSON file
with open('new_aligned_data.json', 'w') as file:
    json.dump(aligned_data, file, indent=4)
    
print("Aligned data saved to new_aligned_data.json")
