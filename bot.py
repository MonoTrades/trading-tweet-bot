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

# Map coin symbols to hashtag names
coin_hashtags = {
    "BTC-USD": "#BTC",
    "ETH-USD": "#ETH",
    "BNB-USD": "#BNB",
    "SOL-USD": "#SOL",
    "XRP-USD": "#XRP",
    "ADA-USD": "#ADA",
    "DOGE-USD": "#DOGE",
    "AVAX-USD": "#AVAX",
    "TRX-USD": "#TRX",
    "DOT-USD": "#DOT",
    "SHIB-USD": "#SHIB",
    "PEPE-USD": "#PEPE",
    "FLOKI-USD": "#FLOKI",
    "BONK-USD": "#BONK",
    "WIF-USD": "#WIF",
    "TURBO-USD": "#TURBO",
    "MEME-USD": "#MEME",
    "DOG-USD": "#DOG",
    "CATE-USD": "#CATE",
    "BABYDOGE-USD": "#BABYDOGE"
}

# Sentence templates for each sentiment
bullish_phrases = [
    "showing strong bullish momentum",
    "buyers are in control",
    "uptrend gaining steam",
    "momentum is building",
    "rallying higher",
    "moving upward with strength",
    "bouncing off support with buyers",
    "upside pressure increasing",
    "buyers pushing the price higher",
    "trend is looking positive"
]

bearish_phrases = [
    "showing weakness, possible correction",
    "sellers taking control",
    "downtrend continuing",
    "pressure from bears",
    "sliding lower",
    "losing ground",
    "resistance holding strong",
    "falling back from highs",
    "market leaning bearish",
    "momentum fading"
]

neutral_phrases = [
    "moving sideways, waiting for a breakout",
    "trading in a tight range",
    "consolidating",
    "no clear direction yet",
    "market is indecisive",
    "price holding steady",
    "choppy price action",
    "waiting for a trend to form",
    "bouncing between levels",
    "range-bound movement"
]

# Generic hashtags to rotate
generic_hashtags = ["#crypto", "#trading", "#markets", "#altcoins", "#blockchain", "#priceaction"]

def analyze_coin(symbol):
    try:
        data = yf.download(symbol, period="2d", interval="1h", auto_adjust=True)
        if data.empty or len(data) < 2:
            return None

        last_close = float(data["Close"].iloc[-1])
        prev_close = float(data["Close"].iloc[-2])
        change = (last_close - prev_close) / prev_close * 100

        if change > 2:
            sentiment = random.choice(bullish_phrases)
        elif change < -2:
            sentiment = random.choice(bearish_phrases)
        else:
            sentiment = random.choice(neutral_phrases)

        coin_tag = coin_hashtags.get(symbol, "")
        tags = " ".join(random.sample(generic_hashtags, 2)) + f" {coin_tag}"

        return f"{symbol.replace('-USD','')} is {sentiment} (last close: ${last_close:.2f}, {change:+.2f}%) | {tags}"
    except Exception:
        return None

def generate_trading_tweet():
    random.shuffle(coins)
    analyses = []
    for coin in coins[:3]:  # Pick 3 random coins per tweet
        result = analyze_coin(coin)
        if result:
            analyses.append(result)

    if not analyses:
        return "Markets are quiet right now. Waiting for a clearer trend."

    return " || ".join(analyses)

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
