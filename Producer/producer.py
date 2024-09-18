import yfinance as yf
import json
from kafka import KafkaProducer
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka broker location
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize data to JSON
)

# Function to stream stock data
def stream_stock_data(ticker, topic):
    stock_data = yf.download(ticker, period='1d', interval='1m')  # 1 day, 1-minute intervals
    for index, row in stock_data.iterrows():
        message = {
            'ticker': ticker,
            'timestamp': str(index),
            'open': row['Open'],
            'high': row['High'],
            'low': row['Low'],
            'close': row['Close'],
            'volume': row['Volume']
        }
        print(f"Sending message: {message}")
        producer.send(topic, value=message)
        time.sleep(60)  # Wait for a second before sending the next message

# Stream stock data for Apple (AAPL) to Kafka topic 'stock_data'
if __name__ == "__main__":
    stream_stock_data('RELIANCE.NS', 'stock_data')
