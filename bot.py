import tweepy
import random
import sys
import yfinance as yf

# === Load credentials from sys.argv ===
if len(sys.argv) < 6:
    print("ERROR: Not enough arguments provided.")
    sys.exit(1)

API_KEY = sys.argv[1]
API_SECRET = sys.argv[2]
ACCESS_TOKEN = sys.argv[3]
ACCESS_TOKEN_SECRET = sys.argv[4]
BEARER_TOKEN = sys.argv[5]

# Authenticate with X API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# List of coins to analyze (Top 10 + Meme coins)
coins = [
    "BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "XRP-USD",
    "ADA-USD", "DOGE-USD", "AVAX-USD", "TRX-USD", "DOT-USD",
    "SHIB-USD", "PEPE-USD", "FLOKI-USD", "BONK-USD", "WIF-USD",
    "TURBO-USD", "MEME-USD", "DOG-USD", "CATE-USD", "BABYDOGE-USD"
]

def analyze_coin(symbol):
    try:
        data = yf.download(symbol, period="2d", interval="1h")
        if data.empty:
            return None

        last_close = data["Close"].iloc[-1]
        prev_close = data["Close"].iloc[-2]
        change = (last_close - prev_close) / prev_close * 100

        if change > 2:
            sentiment = "bullish momentum building 🚀"
        elif change < -2:
            sentiment = "showing weakness, possible correction 📉"
        else:
            sentiment = "moving sideways, waiting for a breakout ⏳"

        return f"{symbol.replace('-USD','')} is {sentiment} (last close: ${last_close:.2f}, {change:+.2f}%)"
    except Exception as e:
        return None

def generate_trading_tweet():
    random.shuffle(coins)
    analyses = []
    for coin in coins[:3]:  # Pick 3 random coins for each tweet
        result = analyze_coin(coin)
        if result:
            analyses.append(result)

    if not analyses:
        return "Markets are quiet right now. Waiting for a clearer trend. 🕒"
    
    return " | ".join(analyses)

def post_tweet():
    try:
        tweet_content = generate_trading_tweet()
        response = client.create_tweet(text=tweet_content)
        print("Tweet posted successfully: " + tweet_content)
        return response
    except Exception as e:
        print("Error posting tweet: " + str(e))
        return None

if __name__ == "__main__":
    post_tweet()
