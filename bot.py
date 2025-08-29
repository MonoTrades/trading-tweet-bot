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

# === 100 Day trading tips ===
day_trading_tips = [
    "Always set a stop loss before entering a trade. Risk management keeps you in the game.",
    "Never risk more than 1-2% of your account on a single trade. Protect your capital.",
    "The trend is your friend until it ends. Avoid fighting strong momentum.",
    "Volume confirms price action. Watch for spikes to validate breakouts.",
    "Don’t chase trades. Wait for the setup to come to you.",
    "Use higher timeframes to confirm entries on lower timeframes.",
    "Avoid trading during low liquidity hours — spreads can widen and volatility drops.",
    "Journal every trade. Reviewing past trades sharpens future decisions.",
    "Focus on quality setups, not quantity. Overtrading kills accounts.",
    "Stick to your trading plan. Emotions are your biggest enemy.",
    "Patience pays. Sometimes the best trade is no trade at all.",
    "Manage position size carefully — leverage magnifies both gains and losses.",
    "Breakouts with no volume often fail. Wait for confirmation.",
    "Support and resistance levels matter — respect them.",
    "Compounding small consistent wins beats gambling on big trades.",
    "News events create volatility. Avoid entering right before announcements.",
    "Don’t marry a trade. Be flexible when the market proves you wrong.",
    "Risk-to-reward ratio of at least 1:2 keeps you profitable long term.",
    "Indicators lag, price action leads. Read the chart first.",
    "Discipline beats strategy. Most traders lose because they can’t follow rules.",
    "Trade with the trend, not against it. Counter-trend trades are riskier.",
    "Don’t overcomplicate charts with too many indicators.",
    "Protect your capital first. Profits come second.",
    "Red days happen. Don’t revenge trade to make it back quickly.",
    "Scalping requires speed, discipline, and a clear exit plan.",
    "Swing traders and day traders need different mindsets. Know your style.",
    "Stick to a few assets. Master them instead of trading everything.",
    "Every trade should have a reason — don’t trade out of boredom.",
    "Flat markets often trap traders. Be patient.",
    "Big moves often start from consolidation zones.",
    "A strong opening move can set the tone for the day.",
    "Cut losses fast. Small losses are tuition, big losses are killers.",
    "Winning streaks breed overconfidence. Stay disciplined.",
    "Losing streaks happen. Reduce size, not discipline.",
    "Don’t average down losers. That’s hope, not strategy.",
    "Risk small, scale when proven right.",
    "Markets can stay irrational longer than you can stay solvent.",
    "Price gaps often fill — but not always. Manage risk.",
    "Avoid holding positions overnight unless it’s part of your plan.",
    "Check the economic calendar before trading.",
    "Liquidity matters. Thinly traded assets are harder to exit safely.",
    "Keep charts clean and simple. Clarity beats clutter.",
    "Use alerts to avoid staring at screens all day.",
    "Don’t follow the crowd blindly. Herds get trapped.",
    "Have multiple exit strategies, not just one.",
    "Small consistent profits compound into big gains.",
    "Fear of missing out (FOMO) is a trader’s biggest enemy.",
    "Trading is a business. Treat it like one.",
    "Don’t risk rent money. Only trade what you can afford to lose.",
    "Patience and discipline separate pros from amateurs.",
    "Revenge trading destroys accounts. Walk away after losses.",
    "Greed makes traders stay too long in winning trades.",
    "Markets reward preparation. Do your homework.",
    "Adapt strategies to market conditions. No one strategy fits all.",
    "Capital preservation is more important than capital growth.",
    "Journal emotions as well as trades. Psychology matters.",
    "Trade less, observe more.",
    "If you don’t know why you’re in a trade, get out.",
    "Big profits often come from sitting on your hands.",
    "Risk small, but think big in the long run.",
    "Don’t use leverage without experience. It cuts both ways.",
    "Set alerts for key levels and wait.",
    "Never stop learning. Markets evolve constantly.",
    "Losing money is part of trading. Learn from it.",
    "Don’t blindly copy others’ trades. Understand the reasoning.",
    "Emotions cloud judgment. Stay objective.",
    "Trade what you see, not what you hope.",
    "Keep drawdowns small so you can recover quickly.",
    "Focus on process, not outcome. Good processes bring results.",
    "Markets punish impatience.",
    "Avoid overconfidence after a big win.",
    "Plan your trade, then trade your plan.",
    "Know where you’ll exit before you enter.",
    "Let winners run, cut losers quickly.",
    "Never add to a losing trade without a strong plan.",
    "Scalps should be quick. Don’t turn them into swings.",
    "Sideways markets chop impatient traders.",
    "Focus on setups that repeat consistently.",
    "Respect stop losses — they exist for a reason.",
    "Trading less often can mean higher accuracy.",
    "Don’t let a winning trade turn into a losing trade.",
    "Check spreads before entering fast-moving markets.",
    "Volatility is both opportunity and risk. Manage it.",
    "Record screen replays of your trading sessions for review.",
    "Test strategies on demo before going live.",
    "Use risk-reward ratios to filter trades.",
    "Stack odds in your favor by combining multiple confirmations.",
    "Trade with patience, not impulse.",
    "News-driven trades can be unpredictable. Manage carefully.",
    "Focus on setups you understand deeply.",
    "Don’t rely solely on luck. Build skill.",
    "Always prepare for both scenarios: winning and losing.",
    "Take profits along the way instead of aiming for perfection.",
    "Small consistent wins build confidence.",
    "Avoid trading when distracted or emotional.",
    "Check correlation between assets before entering multiple trades.",
    "Diversify strategies, but don’t overdo it.",
    "Simplicity works better than complexity in trading.",
    "Respect market conditions. Adapt instead of forcing trades.",
    "Never risk everything on one trade — protect longevity.",
    "Trading success is survival first, profits second."
]

# Hashtags to rotate
hashtags = ["#trading", "#daytrading", "#priceaction", "#markets", "#stocks", "#crypto", "#forex", "#riskmanagement", "#technicalanalysis"]

def generate_tip_tweet():
    tip = random.choice(day_trading_tips)
    tags = " ".join(random.sample(hashtags, 2))
    return f"Day Trading Tip: {tip} | {tags}"

def post_tweet():
    try:
        tweet_content = generate_tip_tweet()
        response = client.create_tweet(text=tweet_content)
        print("Tweet posted successfully: " + tweet_content)
        return response
    except Exception as e:
        print("Error posting tweet: " + str(e))
        return None

# === Auto post every 3 hours ===
if __name__ == "__main__":
    while True:
        post_tweet()
        time.sleep(3 * 60 * 60)  # 3 hours
