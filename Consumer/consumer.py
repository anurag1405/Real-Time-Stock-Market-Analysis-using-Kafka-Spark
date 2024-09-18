from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp, expr
from pyspark.sql.types import StructType, StringType, DoubleType
from config import url,properties

# Initialize SparkSession
spark = SparkSession \
    .builder \
    .appName("Real Time Stock Streaming") \
    .master("local[3]") \
    .config("spark.stream.stopGracefullyOnShutdown", "true") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2,org.postgresql:postgresql:42.7.4")\
    .getOrCreate()

# Define the schema for incoming Kafka messages
schema = StructType() \
    .add("ticker", StringType()) \
    .add("timestamp", StringType()) \
    .add("open", DoubleType()) \
    .add("high", DoubleType()) \
    .add("low", DoubleType()) \
    .add("close", DoubleType()) \
    .add("volume", DoubleType())

# Read stock data from Kafka
stock_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "stock_data") \
    .option("startingOffsets", "earliest") \
    .option("failOnDataLoss", "false") \
    .load()

# Cast Kafka messages to String and parse JSON
stock_json_df = stock_df.selectExpr("CAST(value AS STRING)")

# Parse JSON and select data fields
stock_parsed_df = stock_json_df \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .withColumn("timestamp", to_timestamp(expr("substring(timestamp, 1, 19)"), "yyyy-MM-dd HH:mm:ss"))



def write_to_postgres(batch_df, batch_id):
    batch_df.write.jdbc(url=url, table="stock_data", mode="append", properties=properties)

# Use foreachBatch to process and write each batch to PostgreSQL
query = stock_parsed_df.writeStream \
    .foreachBatch(write_to_postgres) \
    .option("checkpointLocation", "/tmp/checkpoints") \
    .start()


query.awaitTermination()
