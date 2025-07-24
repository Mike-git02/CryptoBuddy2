# chatbot.py

from crypto_data import crypto_db

def greet():
    print("🤖 CryptoBuddy: Hey there! Ready to explore the crypto world? 🌍")
    print("Ask me things like:")
    print("- Which crypto is trending up?")
    print("- What’s the most sustainable coin?")
    print("- Which coin should I buy for long-term growth?\n")

def get_user_input():
    return input("You: ").lower()

def handle_query(query):
    if "sustainable" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: 🌱 You should check out {recommend}! It's eco-friendly and future-ready.")
    
    elif "trending" in query or "rising" in query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"CryptoBuddy: 🚀 These coins are trending up: {', '.join(trending)}")
    
    elif "long-term" in query or "growth" in query:
        options = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7
        ]
        if options:
            print(f"CryptoBuddy: 📈 Consider {options[0]} — it’s growing and sustainable!")
        else:
            print("CryptoBuddy: Hmm, I couldn't find a perfect match right now.")
    
    elif "energy" in query:
        low_energy = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
        print(f"CryptoBuddy: ⚡ These use low energy: {', '.join(low_energy)}")
    
    elif "help" in query:
        greet()
    
    elif "bye" in query or "exit" in query:
        print("CryptoBuddy: 👋 Bye for now! Remember to do your own research (DYOR)!")
        return False
    
    else:
        print("CryptoBuddy: 🤔 I didn't quite get that. Try asking about trending, sustainable, or long-term coins.")
    
    return True

def run_chatbot():
    greet()
    active = True
    while active:
        query = get_user_input()
        active = handle_query(query)

if __name__ == "__main__":
    run_chatbot()
