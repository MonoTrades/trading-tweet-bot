import tweepy
import random
import sys
import os
import json

# === Load credentials from sys.argv ===
if len(sys.argv) < 6:
    print("ERROR: Not enough arguments provided.")
    sys.exit(1)

API_KEY = sys.argv[1]
API_SECRET = sys.argv[2]
ACCESS_TOKEN = sys.argv[3]
ACCESS_TOKEN_SECRET = sys.argv[4]
BEARER_TOKEN = sys.argv[5]

# === Authenticate with Twitter API v2 ===
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# === 100 Day Trading Tips ===
tips = [
    "Always use a stop loss to protect your capital.",
    "Never risk more than 1-2% of your account on a single trade.",
    "Avoid trading during low liquidity hours.",
    "Stick to your trading plan — emotions kill profits.",
    "Don’t chase trades. Wait for confirmation.",
    "Use higher timeframes to confirm trends.",
    "News events can cause extreme volatility — trade cautiously.",
    "Overtrading is a fast way to drain your account.",
    "Keep a trading journal to review mistakes.",
    "Focus on risk management, not just profits.",
    "Support and resistance levels are key decision zones.",
    "Always check multiple timeframes before entering a trade.",
    "Avoid revenge trading after a loss.",
    "Patience is often more profitable than constant trading.",
    "Cut your losses early, let winners run.",
    "Use position sizing to manage risk properly.",
    "Avoid over-leveraging, it magnifies losses.",
    "Trading less can often mean making more.",
    "Protect capital first, profits second.",
    "Don’t rely on one strategy only — adapt.",
    "Markets trend only 20-30% of the time, range the rest.",
    "Keep charts clean — avoid indicator overload.",
    "Price action often gives the clearest signal.",
    "Avoid trading when you’re emotional or distracted.",
    "Don’t let FOMO control your trades.",
    "Scalping requires discipline and fast execution.",
    "Swing trading requires patience and wider stops.",
    "Backtest your strategy before using real money.",
    "Risk/reward ratio should always favor reward.",
    "Avoid trading against strong trends.",
    "Learn to identify fake breakouts.",
    "Volume confirms price action.",
    "Don’t marry your trades — be flexible.",
    "Avoid holding losing positions for hope.",
    "Discipline is more important than a perfect strategy.",
    "Trade the market you see, not what you think.",
    "Avoid trading right before major news releases.",
    "Be consistent with your strategy.",
    "Protecting profits is just as important as making them.",
    "Trade only liquid assets with tight spreads.",
    "Focus on quality setups, not quantity.",
    "Your edge comes from consistency and discipline.",
    "Journal both wins and losses for patterns.",
    "Trade small until you prove profitability.",
    "Avoid copying others blindly — develop your style.",
    "Markets are random in the short term, structured in the long term.",
    "Don’t add to a losing position (averaging down is dangerous).",
    "Learn from every trade, win or lose.",
    "The best traders are great risk managers.",
    "Break big goals into small, achievable steps.",
    "Wait for high-probability setups, don’t force trades.",
    "Trend is your friend, until it ends.",
    "Take partial profits when the market allows.",
    "Protecting your mindset is as important as capital.",
    "Stay updated with global economic events.",
    "Don’t let one trade ruin your account.",
    "Markets will be here tomorrow — don’t rush.",
    "Stick to pairs/coins you understand.",
    "Technical and fundamental analysis together are stronger.",
    "Don’t fight central bank policy in forex.",
    "Always know your exit before you enter.",
    "Consistency beats occasional big wins.",
    "Use alerts to avoid staring at charts all day.",
    "Don’t let greed push you to overtrade.",
    "Hedging requires skill — avoid until experienced.",
    "Risk small, but think big picture.",
    "Protect your account during choppy markets.",
    "Cutting losers quickly increases longevity.",
    "Journal emotions along with trades.",
    "Take breaks, avoid burnout.",
    "Don’t let early success make you careless.",
    "Each market has its own rhythm — learn it.",
    "Plan the trade, trade the plan.",
    "Every loss is tuition — learn from it.",
    "Focus on process, not outcome.",
    "Be patient with entries, aggressive with risk control.",
    "A missed trade is better than a bad trade.",
    "Avoid all-in bets — that’s gambling.",
    "Diversify strategies, not just assets.",
    "Never assume a trend will last forever.",
    "Trade with the market, not against it.",
    "Avoid trading under stress or fatigue.",
    "Don’t compare your journey to others.",
    "Overconfidence is dangerous after wins.",
    "Keep learning — markets evolve.",
    "Risk management is your survival tool.",
    "Focus on mastering one strategy first.",
    "Never double down on a bad trade.",
    "The market doesn’t owe you anything.",
    "Trading is a marathon, not a sprint.",
    "Take small consistent gains over big risks.",
    "Don’t let losses shake your discipline.",
    "Risk comes first, profit comes second.",
    "Be humble — markets punish arrogance.",
    "Patience separates traders from gamblers.",
    "Don’t confuse luck with skill.",
    "Follow trends, don’t fight them.",
    "Stay flexible — markets change daily.",
    "Protect capital so you can trade tomorrow.",
    "Only trade when conditions are clear.",
    "Discipline + Patience = Long-term success."
]

# === Fixed hashtags (always included) ===
fixed_tags = "#trading #crypto #btc"

# === Extra hashtags for variety ===
extra_hashtags = [
    "#stocks", "#forex", "#daytrading", "#investing", "#marketnews",
    "#technicalanalysis", "#stockmarket", "#altcoins", "#charting"
]

# === State file to track unused tips ===
state_file = "tips_state.json"

def load_state():
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            return json.load(f)
    else:
        # Start with all tips shuffled
        shuffled = tips.copy()
        random.shuffle(shuffled)
        return {"remaining": shuffled}

def save_state(state):
    with open(state_file, "w") as f:
        json.dump(state, f)

def generate_tip_tweet():
    state = load_state()
    remaining = state["remaining"]

    if not remaining:  # if empty, reshuffle
        remaining = tips.copy()
        random.shuffle(remaining)

    tip = remaining.pop(0)  # get next tip
    state["remaining"] = remaining
    save_state(state)

    chosen_tags = ""
    if len(extra_hashtags) >= 2:
        chosen_tags = " ".join(random.sample(extra_hashtags, 2))

    return f"💡 Trading Tip: {tip}\n\n{fixed_tags} {chosen_tags}"

def post_tweet():
    try:
        tweet_content = generate_tip_tweet()
        client.create_tweet(text=tweet_content)
        print("Tweet posted successfully:", tweet_content)
    except Exception as e:
        print("Error posting tweet:", e)

if __name__ == "__main__":
    post_tweet()
