import sys
import tweepy
import yfinance as yf
import random

# === Get credentials from sys.argv ===
API_KEY = sys.argv[1]
API_SECRET = sys.argv[2]
ACCESS_TOKEN = sys.argv[3]
ACCESS_TOKEN_SECRET = sys.argv[4]
BEARER_TOKEN = sys.argv[5]

# === Auth with Tweepy ===
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# === Coins to cover ===
coins = {
    "BTC-USD": "Bitcoin",
    "ETH-USD": "Ethereum",
    "BNB-USD": "BNB",
    "XRP-USD": "XRP",
    "SOL-USD": "Solana",
    "ADA-USD": "Cardano",
    "DOGE-USD": "Dogecoin",
    "AVAX-USD": "Avalanche",
    "DOT-USD": "Polkadot",
    "MATIC-USD": "Polygon",
    # Meme coins
    "SHIB-USD": "Shiba Inu",
    "PEPE-USD": "Pepe",
    "FLOKI-USD": "Floki",
    "BONK-USD": "Bonk",
    "WIF-USD": "Dogwifhat",
    "TURBO-USD": "Turbo",
    "DOG-USD": "The Dog",
    "HOGE-USD": "Hoge Finance",
    "ELON-USD": "Dogelon Mars",
    "KISHU-USD": "Kishu Inu",
}

# === Track which coin was last used (saved in a file) ===
def get_next_coin():
    try:
        with open("last_coin.txt", "r") as f:
            last = f.read().strip()
    except FileNotFoundError:
        last = None

    keys = list(coins.keys())
    if last in keys:
        idx = (keys.index(last) + 1) % len(keys)
    else:
        idx = 0

    next_coin = keys[idx]

    with open("last_coin.txt", "w") as f:
        f.write(next_coin)

    return next_coin

# === Build analysis tweet ===
def make_tweet(symbol, name):
    data = yf.download(symbol, period="5d", interval="1h")
    if data.empty:
        return f"{name} ({symbol}) data unavailable right now. 📉"

    latest = data.iloc[-1]
    prev = data.iloc[-2]

    price = round(latest["Close"], 2)
    change = ((latest["Close"] - prev["Close"]) / prev["Close"]) * 100

    if change > 2:
        outlook = f"{name} is looking bullish, up {change:.2f}% in the last hour. Buyers showing strength."
    elif change < -2:
        outlook = f"{name} is under pressure, down {change:.2f}% in the last hour. Bears taking control."
    else:
        outlook = f"{name} is pretty flat around ${price}, waiting for a bigger move."

    hashtags = ["#crypto", "#trading", "#markets", "#altcoins", "#bitcoin", "#blockchain"]
    tags = " ".join(random.sample(hashtags, 2))

    return f"{outlook}\n\nPrice: ${price}\n{tags}"

# === Run bot ===
def run():
    coin = get_next_coin()
    tweet = make_tweet(coin, coins[coin])

    try:
        api.update_status(tweet)
        print("Tweet posted:", tweet)
    except Exception as e:
        print("Error posting tweet:", e)

if __name__ == "__main__":
    run()
