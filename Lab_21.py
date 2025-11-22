import requests

class SimpleAPIClient:
    def __init__(self):
        # Base URL of the API
        self.base_url = "https://jsonplaceholder.typicode.com"

    # Method to fetch posts (GET request)
    def get_posts(self):
        response = requests.get(f"{self.base_url}/posts")

        if response.status_code == 200:
            return response.json()   # return list of posts
        else:
            print("Failed to fetch posts")
            return None

    # Method to create a new post (POST request)
    def create_post(self, title, body, user_id):
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(f"{self.base_url}/posts", json=data)

        if response.status_code == 201:
            return response.json()   # return the created post
        else:
            print("Failed to create post")
            return None

client = SimpleAPIClient()

# Fetch posts
posts = client.get_posts()
if posts:
    print("First 3 Posts:")
    for p in posts[:3]:
        print(p["title"])

# Create a new post
new_post = client.create_post("My New Post", "This is content", 1)
print("Created Post:", new_post)
