import tweepy
import random
from datetime import datetime
import sys

print("=== Starting Trading Tweet Bot ===")

# Load API keys from command-line arguments
try:
    API_KEY = sys.argv[1]
    API_SECRET = sys.argv[2]
    ACCESS_TOKEN = sys.argv[3]
    ACCESS_TOKEN_SECRET = sys.argv[4]
    BEARER_TOKEN = sys.argv[5]
except IndexError:
    print("ERROR: API keys not provided via command-line arguments. Exiting.")
    exit(1)

# Debug: confirm keys are loaded
print("API_KEY loaded:", bool(API_KEY))
print("ACCESS_TOKEN loaded:", bool(ACCESS_TOKEN))

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
