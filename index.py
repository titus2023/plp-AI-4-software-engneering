# Step 1: Define Crypto Database
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

# Step 2: Define Chatbot Personality
def greet_user():
    print("👋 Hey there! I'm CryptoBuddy, your AI-powered financial sidekick! 💰🌱")
    print("Ask me about trending, profitable, or sustainable cryptocurrencies!")

# Step 3: Define Chatbot Logic
def process_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌿 Go with {recommend}! It scores high on sustainability and uses less energy."

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"📈 The cryptos on the rise: {', '.join(trending)}."

    elif "profitable" in user_query or "growth" in user_query or "long-term" in user_query:
        profitable = [coin for coin in crypto_db if
                      crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"]
        if profitable:
            return f"💸 {profitable[0]} looks profitable with a strong trend and market cap!"
        else:
            return "🤔 Hmm, no high market cap cryptos are rising right now."

    elif "energy" in user_query:
        efficient = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        return f"⚡ Energy-efficient coins: {', '.join(efficient)}."

    elif "help" in user_query or "options" in user_query:
        return ("📝 You can ask me things like:\n"
                "- Which crypto is trending up?\n"
                "- What’s the most sustainable coin?\n"
                "- Which coin should I buy for growth?\n"
                "- Which uses the least energy?")

    else:
        return "🤖 I'm not sure how to help with that. Try asking about trends, sustainability, or profitability."

# Step 4: Chat Loop
def chat():
    greet_user()
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("CryptoBuddy: Goodbye! Invest smartly! 🚀")
            break
        response = process_query(user_input)
        print("CryptoBuddy:", response)

# Run the Chatbot
chat()
