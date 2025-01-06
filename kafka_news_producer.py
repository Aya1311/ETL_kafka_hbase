from kafka import KafkaProducer
from newsapi import NewsApiClient
import json
from time import sleep
from datetime import datetime

# Initialize the Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')  # Encoding the JSON string as bytes
)

# Initialize the News API Client
newsapi = NewsApiClient(api_key='.......')

# Get top headlines
top_headlines = newsapi.get_top_headlines()

try:
    # Process each article
    for article in top_headlines['articles']:
        # Check for essential fields and skip if any are missing
        if not all(article.get(field) for field in ['author', 'title', 'description', 'url', 'publishedAt']):
            continue

        # Transform the article data to match the Flink schema
        transformed_data = {
            'author': article['author'],
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'urlToImage': article.get('urlToImage', 'No Image URL'),
            'publishedAt': datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S"),
            'content': article.get('content', 'No Content')
        }

        # Convert the transformed data to JSON
        json_data = json.dumps(transformed_data)

        # Print the data (for debugging)
        print(json_data)

        # Send the data to the Kafka topic
        producer.send('topic_aya', value=json_data)

        # Sleep for a second to avoid rate limiting
        sleep(1)

    producer.flush()
finally:
    producer.close()

print("Done sending messages to Kafka.")


