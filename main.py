import os
import requests
from requests_oauthlib import OAuth1
from datetime import datetime

# Load your keys and tokens from the environment variables
API_KEY = os.environ['API_KEY']
API_KEY_SECRET = os.environ['API_KEY_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

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

# Function to calculate the day count based on the hardcoded start date
def calculate_day_count(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    current_date = datetime.now()
    delta = current_date - start_date
    return delta.days

if __name__ == "__main__":
    # Hardcode the start date directly into the Python script
    start_date_str = "2024-10-13"  # Change this to the actual start date

    # Calculate the current day count based on the start date
    day = calculate_day_count(start_date_str)

    # Compose the tweet message with the current day
    tweet_text = f"Diena {day}: Bibliotēka vēl nav atvērta 24/7"
    
    # Post the tweet
    post_tweet(tweet_text)
