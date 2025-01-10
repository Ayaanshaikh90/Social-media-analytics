import random

# Sample data structure (modify as needed)
post_data = []  # Initialize an empty list to store data
for _ in range(100):  # Generate 100 data points
    post_type = random.choice(["carousel", "reel", "image"])
    likes = random.randint(100, 500)
    shares = random.randint(10, 100)
    comments = random.randint(5, 50)
    post_data.append({"post_type": post_type, "likes": likes, "shares": shares, "comments": comments})

# Print sample data for verification
print(post_data[:5])