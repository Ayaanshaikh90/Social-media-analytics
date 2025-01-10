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

# Retrieve data from the "posts" table
try:
    # Use `fetch_all` for efficient data retrieval
    posts = client.fetch_all(collection="posts")
    print("Data retrieved successfully!")
except Exception as e:
    print(f"Error retrieving data: {e}")

# Process data and calculate averages
insights = {}
for post in posts:
    post_type = post["post_type"]
    if post_type not in insights:
        insights[post_type] = {"likes": [], "shares": [], "comments": []}
    insights[post_type]["likes"].append(post["likes"])
    insights[post_type]["shares"].append(post["shares"])
    insights[post_type]["comments"].append(post["comments"])

for post_type, metrics in insights.items():
    avg_likes = sum(metrics["likes"]) / len(metrics["likes"])
    avg_shares = sum(metrics["shares"]) / len(metrics["shares"])
    avg_comments = sum(metrics["comments"]) / len(metrics["comments"])
    print(f"{post_type.capitalize()}: Avg Likes: {avg_likes:.2f}, Avg Shares: {avg_shares:.2f}, Avg Comments: {avg_comments:.2f}")
