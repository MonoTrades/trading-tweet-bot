import tweepy
import random
import requests
import os
from datetime import datetime

# === X API credentials from GitHub Secrets ===
API_KEY = os.getenv("cWJJjZDOIzHfOGaIzuMq4uAtB")
API_SECRET = os.getenv("ydSXJ8c3WjFOhnp2Yjf99Hd0cgFlPZxIQbgUcf7e6rQb6DzFQM")
ACCESS_TOKEN = os.getenv("112135868-gOiEnrwm2RHnTdkUie95hoHMPOmcAYX2MembnQTb")
ACCESS_TOKEN_SECRET = os.getenv("lMFqn040P95Q6PzHu7XlQZxwo3jWLC74vbmG3HuVYiLW5")
BEARER_TOKEN = os.getenv("AAAAAAAAAAAAAAAAAAAAADBr3gEAAAAAtWkNuj9uHiea8Iy67YCHLQm44uA%3DP0KgD8RgDYJtAw7BT4C0DNsfqV5h9xWTLcCXnDNVnvgKkqJJyZ")

print("API_KEY:", API_KEY[:4] if API_KEY else "None")
print("ACCESS_TOKEN:", ACCESS_TOKEN[:4] if ACCESS_TOKEN else "None")

# Authenticate with X API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Trading content pools
topics = [
    "Price Action", "Risk Management", "Market Psychology",
    "Fibonacci Retracements", "Support & Resistance",
    "Breakouts", "Moving Averages", "Trend Reversals",
    "Crypto Volatility", "Stock Market Flows"
]

insights = [
    "Don’t chase every move. Wait for confirmation.",
    "Discipline beats prediction every time.",
    "Manage risk first, profits second.",
    "The best traders know when NOT to trade.",
    "Volume confirms the trend — ignore it at your own risk.",
    "Stop-losses are like seatbelts — you only regret not using them.",
    "Markets reward patience, not overtrading.",
    "When in doubt, zoom out.",
    "Never let one trade define you.",
    "Protect your capital — it’s your ammo."
]

hashtags = [
    "#Trading", "#Crypto", "#Stocks", "#Investing", "#DayTrading",
    "#SwingTrading", "#Forex", "#TradingTips", "#Markets"
]

# === Fetch market data (CoinGecko + Yahoo Finance API) ===
def get_market_snapshot():
    try:
        # Crypto from CoinGecko
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
        response = requests.get(url, params=params).json()
        
        btc = response["bitcoin"]["usd"]
        eth = response["ethereum"]["usd"]

        # S&P500 from Yahoo Finance
        sp_url = "https://query1.finance.yahoo.com/v8/finance/chart/^GSPC"
        sp_data = requests.get(sp_url).json()
        sp500 = sp_data["chart"]["result"][0]["meta"]["regularMarketPrice"]

        return {
            "BTC": round(btc, 2),
            "ETH": round(eth, 2),
            "S&P500": round(sp500, 2)
        }
    except Exception as e:
        print("Market data error:", e)
        return None

# === Generate tweet ===
def generate_trading_tweet():
    today = datetime.now().strftime('%Y-%m-%d')

    if random.random() > 0.5:
        topic = random.choice(topics)
        insight = random.choice(insights)
        tag1, tag2 = random.sample(hashtags, 2)
        tweet = f"{topic} Insight: {insight} {tag1} {tag2} {today}"
    else:
        data = get_market_snapshot()
        if data:
            insight = random.choice(insights)
            tweet = (
                f"Market Check {today} 📊\n"
                f"BTC: ${data['BTC']:,}\n"
                f"ETH: ${data['ETH']:,}\n"
                f"S&P500: {data['S&P500']:,}\n\n"
                f"{insight} #Markets #Trading"
            )
        else:
            topic = random.choice(topics)
            insight = random.choice(insights)
            tweet = f"{topic} Tip: {insight} {random.choice(hashtags)} {today}"

    return tweet[:280]

# === Post tweet ===
def post_tweet():
    try:
        tweet_content = generate_trading_tweet()
        response = client.create_tweet(text=tweet_content)
        print("Tweet posted successfully: " + tweet_content)
        return response
    except Exception as e:
        print("Error posting tweet: " + str(e))
        return None

# Run once
post_tweet()
