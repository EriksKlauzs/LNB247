import os
import requests
from requests_oauthlib import OAuth1

# Load your keys and tokens from the environment variables
API_KEY = os.environ['API_KEY']
API_KEY_SECRET = os.environ['API_KEY_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']  # New access token with read/write permissions
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']  # New access token secret with read/write permissions

# Function to post a tweet using OAuth 1.0a User Context Authentication
def post_tweet(tweet_text):
    tweet_url = "https://api.twitter.com/2/tweets"

    # Setup OAuth1 authentication
    auth = OAuth1(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Minimal tweet payload
    tweet_data = {
        "text": tweet_text
    }

    # POST request to send the tweet
    response = requests.post(tweet_url, auth=auth, json=tweet_data)

    if response.status_code == 201:
        print("Tweet sent successfully!")
    else:
        print(f"Error sending tweet: {response.status_code}")
        print(response.json())

# Example usage
if __name__ == "__main__":
    # Post a simple tweet using OAuth 1.0a
    post_tweet("Hello from my Twitter bot using OAuth 1.0a!")
