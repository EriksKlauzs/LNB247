import os
import requests
from requests_oauthlib import OAuth1

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

# Function to read the current day count from a file
def read_day_count():
    try:
        with open("day_counter.txt", "r") as file:
            day = int(file.read().strip())
    except FileNotFoundError:
        # If the file doesn't exist, start at day 0
        day = 0
    return day

# Function to write the updated day count to the file
def write_day_count(day):
    with open("day_counter.txt", "w") as file:
        file.write(str(day))

if __name__ == "__main__":
    # Read the current day count
    day = read_day_count()

    # Compose the tweet message with the current day
    tweet_text = f"Diena {day}: Bibliotēka vēl nav atvērta 24/7"
    
    # Post the tweet
    post_tweet(tweet_text)

    # Increment the day count
    day += 1

    # Save the updated day count back to the file
    write_day_count(day)
