# 🧠 Cryptopal — A Rule-Based Crypto Investment Chatbot
# Assignment: Analyzing profitability and sustainability of cryptocurrencies using rule-based AI

print("👋 Hey there! I'm Cryptopal – your guide to smart and sustainable crypto picks! 🚀")
print("Ask me things like:\n- Which crypto is trending up?\n- What’s the most sustainable coin?\n- Which crypto should I buy for long-term growth?\n(Type 'exit' to quit.)\n")

# === Step 2: Predefined Crypto Data ===
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8  
    }  
}

# === Step 3 & 4: Chatbot Logic + Advice Rules ===
def get_most_sustainable():
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

def get_trending_cryptos():
    return [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]

def get_profitable_and_sustainable():
    options = []
    for coin, data in crypto_db.items():
        if (data["price_trend"] == "rising" 
            and data["market_cap"] in ["high", "medium"] 
            and data["energy_use"] == "low"
            and data["sustainability_score"] > 7):
            options.append(coin)
    return options

# === Step 5: User Interaction ===
while True:
    user_query = input("You: ").lower()

    if "exit" in user_query:
        print("Cryptopal: Catch you later! 🚀 Remember—crypto is risky. Always do your own research! 📚")
        break

    elif "sustainable" in user_query or "eco" in user_query:
        coin = get_most_sustainable()
        print(f"Cryptopal: Invest in {coin}! 🌱 It’s eco-friendly and has long-term potential!")

    elif "trending" in user_query or "rising" in user_query:
        trending = get_trending_cryptos()
        if trending:
            print(f"Cryptopal: These cryptos are on the rise: {', '.join(trending)} 📈")
        else:
            print("Cryptopal: Hmm... nothing's rising right now. Markets can be moody! 📉")

    elif "long-term" in user_query or "growth" in user_query or "should i buy" in user_query:
        good_picks = get_profitable_and_sustainable()
        if good_picks:
            print(f"Cryptopal: {good_picks[0]} is a smart pick for growth – trending up and super sustainable! 💰🌿")
        else:
            print("Cryptopal: No perfect match right now. Consider checking again later! ⏳")

    else:
        print("Cryptopal: I'm not sure how to help with that. Try asking about trending or sustainable cryptos! 💬")
