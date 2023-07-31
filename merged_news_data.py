import json

# Read data from the first JSON file
with open('merged_news_data.json', 'r') as file1:
    json_data_1 = file1.read()

# Read data from the second JSON file
with open('news_data6.json', 'r') as file2:
    json_data_2 = file2.read()

# Parse JSON data
data_1 = json.loads(json_data_1)
data_2 = json.loads(json_data_2)

# Extract relevant data from each file
items = data_1['items']
sentiment_score_definition = data_1['sentiment_score_definition']
relevance_score_definition = data_1['relevance_score_definition']
feed_1 = data_1['feed']
feed_2 = data_2['feed']

# Combine the extracted data into a single data structure
merged_data = {
    'items': items,
    'sentiment_score_definition': sentiment_score_definition,
    'relevance_score_definition': relevance_score_definition,
    'feed': feed_1 + feed_2
}

# Save the merged data to a new JSON file
with open('merged_news_data.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)

print("Data merged and saved to merged_news_data.json")
