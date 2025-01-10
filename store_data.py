from astrapy import DataAPIClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
# Initialize Astra Client
client = DataAPIClient(application_token=ASTRA_DB_APPLICATION_TOKEN, keyspace=ASTRA_DB_KEYSPACE)

print("Client initialized successfully!")

# Sample data (modify as needed)
post_data = [
    {"post_type": "reel", "likes": 491, "shares": 35, "comments": 25},
    {"post_type": "carousel", "likes": 291, "shares": 82, "comments": 14},
    # Add more posts here
]

# Insert data into the "posts" table
try:
    # Use `insert_documents` for bulk data insertion
    client.insert_documents(collection="posts", documents=post_data)
    print("Data inserted successfully!")
except Exception as e:
    print(f"Error inserting data: {e}")
