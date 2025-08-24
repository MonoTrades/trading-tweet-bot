import sys
import random
import tweepy
import yfinance as yf

# === Load API Keys from sys.argv ===
API_KEY = sys.argv[1]
API_SECRET = sys.argv[2]
ACCESS_TOKEN = sys.argv[3]
ACCESS_TOKEN_SECRET = sys.argv[4]
BEARER_TOKEN = sys.argv[5]

# === Authenticate with Twitter/X ===
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# === Coins to track ===
coins = {
    "BTC-USD": "#BTC",
    "ETH-USD": "#ETH",
    "BNB-USD": "#BNB",
    "SOL-USD": "#SOL",
    "XRP-USD": "#XRP",
    "ADA-USD": "#ADA",
    "DOGE-USD": "#DOGE",
    "TRX-USD": "#TRX",
    "AVAX-USD": "#AVAX",
    "TON-USD": "#TON",

    # Meme coins
    "SHIB-USD": "#SHIB",
    "PEPE-USD": "#PEPE",
    "FLOKI-USD": "#FLOKI",
    "WIF-USD": "#WIF",
    "BONK-USD": "#BONK",
    "TURBO-USD": "#TURBO",
    "DOG-USD": "#DOG",
    "MYRO-USD": "#MYRO",
    "MOG-USD": "#MOG",
    "HOSKY-USD": "#HOSKY"
}

# === Phrases ===
bullish_phrases = [
    "Bulls stepping in.",
    "Momentum looks strong.",
    "Buyers pushing higher.",
    "Upside pressure building.",
    "Price holding firm after the bounce.",
    "Buyers defending key levels.",
    "Trend is pointing upward.",
    "Demand outweighing supply here.",
    "Market leaning bullish.",
    "Buyers keeping control."
]

bearish_phrases = [
    "Bears in control.",
    "Momentum fading.",
    "Sellers taking charge.",
    "Downside pressure building.",
    "Price losing steam.",
    "Resistance holding strong.",
    "Supply outweighing demand here.",
    "Market leaning bearish.",
    "Sellers pressing lower.",
    "Weakness showing in the trend."
]

neutral_phrases = [
    "Waiting for a breakout.",
    "Range-bound price action.",
    "Market is indecisive.",
    "Still consolidating.",
    "No clear direction yet.",
    "Price chopping sideways.",
    "Tight range forming.",
    "Traders on the sidelines.",
    "Lack of momentum for now.",
    "Stuck between levels."
]

# === Hashtags ===
generic_tags = [
    "#Crypto", "#Trading", "#PriceAction", "#CryptoAnalysis", "#Markets",
    "#Investing", "#CryptoTrading", "#Altcoins", "#CryptoMarket", "#TA"
]

# === Pick 1 random coin each run ===
coin, tag = random.choice(list(coins.items()))
ticker = yf.Ticker(coin)
hist = ticker.history(period="1d", interval="1h")

if len(hist) > 2:
    close_now = hist["Close"].iloc[-1]
    close_prev = hist["Close"].iloc[-2]
    change = ((close_now - close_prev) / close_prev) * 100

    # Decide sentiment
    if change > 1:
        phrase = random.choice(bullish_phrases)
    elif change < -1:
        phrase = random.choice(bearish_phrases)
    else:
        phrase = random.choice(neutral_phrases)

    # Build tweet
    tags = " ".join(random.sample(generic_tags, 3)) + " " + tag
    tweet = f"{coin.replace('-USD','')}: ${close_now:.2f} ({change:+.2f}%)\n{phrase}\n{tags}"

    try:
        api.update_status(tweet)
        print("Tweet posted:", tweet)
    except Exception as e:
        print("Error posting tweet:", e)
else:
    print(f"Not enough data for {coin}")
