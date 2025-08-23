import tweepy
import random
import requests
import os
from datetime import datetime

print("=== Starting Trading Tweet Bot ===")

# === Load secrets from environment variables ===
API_KEY = os.environ.get("cWJJjZDOIzHfOGaIzuMq4uAtB")
API_SECRET = os.environ.get("ydSXJ8c3WjFOhnp2Yjf99Hd0cgFlPZxIQbgUcf7e6rQb6DzFQM")
ACCESS_TOKEN = os.environ.get("112135868-gOiEnrwm2RHnTdkUie95hoHMPOmcAYX2MembnQTb")
ACCESS_TOKEN_SECRET = os.environ.get("lMFqn040P95Q6PzHu7XlQZxwo3jWLC74vbmG3HuVYiLW5")
BEARER_TOKEN = os.environ.get("AAAAAAAAAAAAAAAAAAAAADBr3gEAAAAAtWkNuj9uHiea8Iy67YCHLQm44uA%3DP0KgD8RgDYJtAw7BT4C0DNsfqV5h9xWTLcCXnDNVnvgKkqJJyZ")

# Debug: confirm secrets are loaded
print("API_KEY loaded:", bool(API_KEY))
print("API_SECRET loaded:", bool(API_SECRET))
print("ACCESS_TOKEN loaded:", bool(ACCESS_TOKEN))
print("ACCESS_TOKEN_SECRET loaded:", bool(ACCESS_TOKEN_SECRET))
print("BEARER_TOKEN loaded:", bool(BEARER_TOKEN))

# Stop if any secret is missing
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN]):
    print("ERROR: One or more API keys are missing. Exiting.")
    exit(1)

# Authenticate with X API v2
try:
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    print("Authentication successful.")
except Exception as e:
    print("ERROR during authentication:", e)
    exit(1)

# Trading content
topics = ["Price Action", "Risk Management", "Market Psychology", "Fibonacci Retracements", "Support & Resistance"]
insights = [
    "Discipline beats prediction every time.",
    "Manage risk first, profits second.",
    "Never let one trade define you.",
]
hashtags = ["#Trading", "#Crypto", "#Markets"]

# Generate tweet
def generate_trading_tweet():
    today = datetime.now().strftime('%Y-%m-%d')
    topic = random.choice(topics)
    insight = random.choice(insights)
    tags = " ".join(random.sample(hashtags, 2))
    tweet = f"{topic} Tip: {insight} {tags} {today}"
    print("Generated tweet:", tweet)
    return tweet[:280]

# Post tweet
def post_tweet():
    tweet_content = generate_trading_tweet()
    try:
        response = client.create_tweet(text=tweet_content)
        print("Tweet posted successfully!")
        return response
    except Exception as e:
        print("Error posting tweet:", e)
        return None

post_tweet()
print("=== Bot Finished ===")
