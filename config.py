import os
from dotenv import load_dotenv

load_dotenv()

USER=os.getenv("USER") 
PASSWORD=os.getenv("PASSWORD")

# Define postgres URL
url = "jdbc:postgresql://localhost:5432/stockdata"  
properties = {
    "user": USER,
    "password": PASSWORD,
    "driver": "org.postgresql.Driver"
}