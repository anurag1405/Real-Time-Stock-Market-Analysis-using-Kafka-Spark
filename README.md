**Real-Time Market Data Analysis Pipeline**

**Project Overview**


This project demonstrates a real-time market data analysis pipeline that fetches financial data from yfinance and processes it in real-time using Kafka, Spark Streaming, PostgreSQL, and Grafana. The system collects and processes market data with 1-minute intervals, stores it in a database, and visualizes the results in a dynamic dashboard.

**Tech Stack**
- yfinance: Fetching real-time stock market data.
- Kafka: Streaming the market data.
- Spark Streaming: Processing the streamed data in real-time.
- PostgreSQL: Storing the processed data for long-term use and analysis.
- Grafana: Visualizing the data in real-time through an interactive dashboard.

  
**Pipeline Architecture**
- Data Collection:
The pipeline uses yfinance to fetch real-time stock market data at 1-minute intervals.
- Kafka:
Kafka acts as the message broker to stream the market data continuously to consumers (Spark).
- Spark Streaming:
Spark ingests data from Kafka, processes it in real-time, and applies any necessary transformations.
- PostgreSQL:
The processed data is stored in a PostgreSQL database for persistence and query-based analysis.
- Grafana Dashboard:
Grafana connects to the PostgreSQL database to provide real-time visualizations of the stock data, updating every minute.
**Key Features**
- Real-Time Data Streaming: The system updates the data every 1 minute, providing a live feed of stock prices, volume, and other metrics.
- Data Persistence: The data is stored in a PostgreSQL database, allowing for historical analysis.
- Dynamic Dashboards: Grafana provides interactive, real-time visualizations for monitoring stock performance over the past hour.
