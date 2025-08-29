import tweepy
import random
import sys
import time

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

# === 100 Day Trading Tips ===
day_trading_tips = [
    "Always use a stop loss. Protecting capital is the #1 rule of trading.",
    "Never risk more than 1-2% of your account on a single trade.",
    "Patience is a trader’s superpower. Don’t chase setups.",
    "The trend is your friend until it ends. Trade with momentum.",
    "Volume confirms price action. Pay attention to spikes.",
    "Overtrading destroys accounts. Focus on quality setups only.",
    "Cut losers fast, let winners run. Discipline beats emotion.",
    "Don’t marry a trade. If it’s wrong, exit quickly.",
    "Keep a trading journal. Reviewing trades improves performance.",
    "Plan your trade and trade your plan — emotions are costly.",
    "Avoid revenge trading. Step away after a big loss.",
    "Trade with a clear mind. Don’t trade when emotional.",
    "Set alerts to avoid staring at charts all day.",
    "Focus on one or two strategies and master them.",
    "Risk management is more important than winning rate.",
    "Protecting capital is your first job as a trader.",
    "Don’t add to losing trades hoping they’ll recover.",
    "Good entries matter, but risk management matters more.",
    "Use higher timeframes to confirm lower timeframe setups.",
    "Avoid trading low-volume markets — liquidity matters.",
    "Stick to your plan, not your feelings.",
    "Discipline turns an average strategy into a profitable one.",
    "Never chase price after a breakout. Wait for a retest.",
    "Sideways markets can be dangerous. Wait for momentum.",
    "News can create volatility — manage your risk during events.",
    "Trading fewer setups often leads to better results.",
    "Scalping requires precision. If unsure, step aside.",
    "Don’t risk money you can’t afford to lose.",
    "Stay consistent with your trading routine.",
    "Don’t blindly follow others — trust your own analysis.",
    "One big loss can erase weeks of gains. Protect capital.",
    "Position sizing is as important as entries and exits.",
    "Keep your charts clean. Too many indicators create noise.",
    "Price action often tells you more than indicators.",
    "Don’t overcomplicate your strategy. Simplicity wins.",
    "Don’t let FOMO push you into bad trades.",
    "Risk small, grow steady. Compounding wins over time.",
    "Markets don’t owe you anything. Stay humble.",
    "A missed trade is better than a forced trade.",
    "Don’t double down on emotions — detach from results.",
    "Small consistent gains compound into big profits.",
    "Avoid trading out of boredom.",
    "Treat trading like a business, not a lottery ticket.",
    "Avoid trading during extremely low liquidity times.",
    "Stick to your trading hours. Don’t chase after hours.",
    "Understand the risk before thinking about the reward.",
    "Don’t try to catch every move in the market.",
    "Avoid trading when you’re tired or distracted.",
    "Have both entry and exit rules before taking a trade.",
    "The market will be there tomorrow. Don’t force today.",
    "Master risk before chasing profits.",
    "Focus on setups with a clear edge.",
    "Every trade is just one of many — don’t get attached.",
    "Don’t move your stop loss further away. Respect it.",
    "Your edge comes from discipline, not prediction.",
    "Learn to sit on your hands — no trade is a position too.",
    "Don’t scale up too quickly. Build consistency first.",
    "Avoid trading based on emotions like fear or greed.",
    "Never average down a losing trade without a solid reason.",
    "Trade less, think more.",
    "Your first loss is your best loss. Don’t hold and hope.",
    "Let the market come to you. Don’t chase.",
    "The best setups usually feel the hardest to take.",
    "Never assume the market will act rationally.",
    "Avoid trading during major economic uncertainty if unprepared.",
    "Adapt to market conditions — no single strategy works always.",
    "When in doubt, stay out.",
    "Patience is profitable. Wait for confirmation.",
    "The market rewards discipline and punishes impatience.",
    "Every trade should have a reason. No guessing.",
    "Don’t get emotional over wins either. Stay balanced.",
    "Take breaks. Clear mind = better trading.",
    "Trading more doesn’t equal earning more.",
    "Always know your risk-to-reward before entering a trade.",
    "Don’t aim for perfection. Aim for consistency.",
    "Follow your rules strictly. They exist to protect you.",
    "Don’t let greed override logic.",
    "If you break your rules, you break your edge.",
    "Be comfortable with missing trades.",
    "Focus on learning, not just earning, early on.",
    "Don’t try to predict — react to what’s shown.",
    "Review both winning and losing trades equally.",
    "Avoid sudden emotional decisions during live trades.",
    "The market is a marathon, not a sprint.",
    "Be selective. Fewer trades, higher quality.",
    "Don’t let a losing streak shake your confidence.",
    "Trading is about probabilities, not certainties.",
    "Stick to your stop loss no matter what.",
    "Take partial profits if unsure.",
    "Focus on process, not profits.",
    "Avoid trading impulsively after big news.",
    "Don’t let one bad day turn into a bad week.",
    "Always know where you’re wrong before entering.",
    "Respect risk first. Profits follow.",
    "Trading success is built on consistency and discipline.",
    "Think long term. A single trade won’t define you.",
    "Keep your emotions out of position sizing.",
    "Never let a winning trade turn into a losing one.",
    "Stay disciplined when things are going well.",
    "Never stop learning. Markets evolve, so should you."
]

# === Hashtags to rotate ===
hashtags = [
    "#trading", "#daytrading", "#priceaction", "#markets",
    "#stocks", "#crypto", "#forex", "#riskmanagement", "#technicalanalysis"
]

# Shuffle tips so they’re unique each run
remaining_tips = random.sample(day_trading_tips, len(day_trading_tips))

def generate_tip_tweet():
    global remaining_tips
    if not remaining_tips:  # Refill when exhausted
        remaining_tips = random.sample(day_trading_tips, len(day_trading_tips))
    tip = remaining_tips.pop()
    tags = " ".join(random.sample(hashtags, 2))
    return f"Day Trading Tip: {tip} {tags}"

def post_tweet():
    try:
        tweet_content = generate_tip_tweet()
        response = client.create_tweet(text=tweet_content)
        print("Tweet posted successfully:", tweet_content)
        return response
    except Exception as e:
        print("Error posting tweet:", str(e))
        return None

# === Auto post every 3 hours ===
if __name__ == "__main__":
    while True:
        post_tweet()
        time.sleep(3 * 60 * 60)  # 3 hours
