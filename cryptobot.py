import requests
import nltk
import time
import ssl
import urllib3
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# Disable SSL warnings for development (remove in production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class CryptoChatbot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.crypto_data = {}
        self.last_update = None
        self.update_interval = timedelta(minutes=5)  # Refresh every 5 minutes
        
        # Enhanced sustainability scores based on consensus mechanisms
        self.sustainability_scores = {
            'bitcoin': 2,      # Proof of Work - high energy
            'ethereum': 7,     # Proof of Stake - much improved
            'cardano': 9,      # Proof of Stake - very efficient
            'solana': 8,       # Proof of History/Stake - efficient
            'polygon': 8,      # Layer 2 solution - efficient
            'algorand': 9,     # Pure Proof of Stake - carbon neutral
            'tezos': 8,        # Liquid Proof of Stake - efficient
            'stellar': 9,      # Stellar Consensus Protocol - very efficient
        }
        
        # Enhanced fallback data with realistic structure
        self.fallback_data = {
            'bitcoin': {
                'id': 'bitcoin',
                'name': 'Bitcoin',
                'symbol': 'btc',
                'current_price': 67420,
                'market_cap': 1330000000000,
                'price_change_percentage_24h': 1.2,
                'market_cap_rank': 1
            },
            'ethereum': {
                'id': 'ethereum',
                'name': 'Ethereum',
                'symbol': 'eth',
                'current_price': 3890,
                'market_cap': 467000000000,
                'price_change_percentage_24h': 2.8,
                'market_cap_rank': 2
            },
            'cardano': {
                'id': 'cardano',
                'name': 'Cardano',
                'symbol': 'ada',
                'current_price': 0.62,
                'market_cap': 21800000000,
                'price_change_percentage_24h': 3.1,
                'market_cap_rank': 7
            },
            'solana': {
                'id': 'solana',
                'name': 'Solana',
                'symbol': 'sol',
                'current_price': 189,
                'market_cap': 88900000000,
                'price_change_percentage_24h': 4.5,
                'market_cap_rank': 4
            },
            'polygon': {
                'id': 'polygon',
                'name': 'Polygon',
                'symbol': 'matic',
                'current_price': 0.72,
                'market_cap': 7200000000,
                'price_change_percentage_24h': 1.8,
                'market_cap_rank': 12
            },
            'algorand': {
                'id': 'algorand',
                'name': 'Algorand',
                'symbol': 'algo',
                'current_price': 0.34,
                'market_cap': 2800000000,
                'price_change_percentage_24h': 2.1,
                'market_cap_rank': 28
            }
        }

    def greet(self):
        print("🤖 Hi, I'm Cryptopal — your friendly crypto advisor! 🚀")
        print("I can help you with:")
        print("• 📈 Trending cryptocurrencies")
        print("• 🌱 Sustainable/eco-friendly options")
        print("• 💰 Price information and analysis")
        print("• 📊 Market cap rankings")
        print("\nTry asking: 'What's trending?' or 'Which crypto is most sustainable?'")

    def fetch_crypto_data(self) -> bool:
        """Fetch real-time crypto data from CoinGecko API"""
        try:
            url = "https://api.coingecko.com/api/v3/coins/markets"
            params = {
                'vs_currency': 'usd',
                'ids': 'bitcoin,ethereum,cardano,solana,polygon,algorand,tezos,stellar',
                'order': 'market_cap_desc',
                'per_page': 10,
                'page': 1,
                'sparkline': False,
                'price_change_percentage': '24h'
            }
            
            # Multiple approaches to handle SSL issues
            session = requests.Session()
            
            # Try with normal SSL verification first
            try:
                response = session.get(url, params=params, timeout=10)
                response.raise_for_status()
            except requests.exceptions.SSLError:
                # If SSL fails, try without verification (development only)
                print("🔒 SSL verification issue detected, trying alternative approach...")
                response = session.get(url, params=params, timeout=10, verify=False)
                response.raise_for_status()
            
            data = response.json()
            self.crypto_data = {coin['id']: coin for coin in data}
            self.last_update = datetime.now()
            
            print("✅ Live crypto data loaded successfully!")
            return True
            
        except requests.exceptions.RequestException as e:
            if "SSL" in str(e) or "certificate" in str(e).lower():
                print("🔒 SSL Certificate issue detected.")
                print("💡 This is common on some networks. Using reliable fallback data.")
            else:
                print(f"⚠️ API Error: {e}")
                print("📋 Using fallback data instead.")
            self.crypto_data = self.fallback_data
            return False
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            print("📋 Using fallback data instead.")
            self.crypto_data = self.fallback_data
            return False

    def should_refresh_data(self) -> bool:
        """Check if data needs refreshing"""
        if not self.last_update:
            return True
        return datetime.now() - self.last_update > self.update_interval

    def get_fresh_data(self):
        """Get fresh data if needed"""
        if self.should_refresh_data():
            self.fetch_crypto_data()

    def analyze_query(self, query: str) -> set:
        """Enhanced query analysis with better keyword detection"""
        tokens = word_tokenize(query.lower())
        lemmas = [self.lemmatizer.lemmatize(token) for token in tokens]
        
        keywords = set()
        
        # Greeting detection
        greeting_words = ['hi', 'hello', 'hey', 'good', 'morning', 'afternoon', 'evening']
        if any(word in lemmas for word in greeting_words):
            keywords.add('greeting')
        
        # Sustainability keywords
        sustainability_words = ['sustainable', 'sustainability', 'green', 'eco', 'environment', 'carbon', 'energy']
        if any(word in lemmas for word in sustainability_words):
            keywords.add('sustainable')
        
        # Trending keywords
        trend_words = ['trend', 'trending', 'hot', 'popular', 'rising', 'up', 'gaining']
        if any(word in lemmas for word in trend_words):
            keywords.add('trending')
        
        # Price keywords
        price_words = ['price', 'cost', 'value', 'worth', 'expensive', 'cheap']
        if any(word in lemmas for word in price_words):
            keywords.add('price')
        
        # Profit/investment keywords
        profit_words = ['profit', 'profitable', 'investment', 'invest', 'growth', 'gain', 'return']
        if any(word in lemmas for word in profit_words):
            keywords.add('profit')
        
        # Market cap keywords
        market_words = ['market', 'cap', 'capitalization', 'size', 'big', 'large', 'top']
        if any(word in lemmas for word in market_words):
            keywords.add('market')
        
        # Specific crypto mentions
        for crypto_id in self.crypto_data.keys():
            crypto_name = self.crypto_data[crypto_id]['name'].lower()
            crypto_symbol = self.crypto_data[crypto_id]['symbol'].lower()
            if crypto_id in query.lower() or crypto_name in query.lower() or crypto_symbol in query.lower():
                keywords.add(f'specific_{crypto_id}')
        
        return keywords

    def get_trending_cryptos(self) -> List[str]:
        """Get cryptocurrencies with positive 24h change"""
        trending = []
        for crypto_id, data in self.crypto_data.items():
            change = data.get('price_change_percentage_24h', 0)
            if change > 0:
                trending.append((crypto_id, change))
        
        # Sort by percentage change
        trending.sort(key=lambda x: x[1], reverse=True)
        return [crypto[0] for crypto in trending[:5]]

    def get_sustainable_cryptos(self) -> List[tuple]:
        """Get most sustainable cryptocurrencies"""
        sustainable = []
        for crypto_id in self.crypto_data.keys():
            score = self.sustainability_scores.get(crypto_id, 5)
            if score >= 7:  # Only show highly sustainable ones
                sustainable.append((crypto_id, score))
        
        sustainable.sort(key=lambda x: x[1], reverse=True)
        return sustainable

    def format_price(self, price: float) -> str:
        """Format price nicely"""
        if price >= 1:
            return f"${price:,.2f}"
        else:
            return f"${price:.4f}"

    def format_market_cap(self, market_cap: float) -> str:
        """Format market cap in billions/millions"""
        if market_cap >= 1_000_000_000:
            return f"${market_cap/1_000_000_000:.1f}B"
        elif market_cap >= 1_000_000:
            return f"${market_cap/1_000_000:.1f}M"
        else:
            return f"${market_cap:,.0f}"

    def respond_to_query(self, query: str) -> str:
        """Generate response based on query analysis"""
        self.get_fresh_data()
        keywords = self.analyze_query(query)

        # Handle specific crypto queries
        specific_crypto = None
        for keyword in keywords:
            if keyword.startswith('specific_'):
                specific_crypto = keyword.replace('specific_', '')
                break

        if specific_crypto and specific_crypto in self.crypto_data:
            data = self.crypto_data[specific_crypto]
            name = data['name']
            price = self.format_price(data['current_price'])
            change = data.get('price_change_percentage_24h', 0)
            change_emoji = "📈" if change > 0 else "📉" if change < 0 else "➡️"
            sustainability = self.sustainability_scores.get(specific_crypto, 5)
            
            return (f"💰 {name} ({data['symbol'].upper()})\n"
                   f"Price: {price} {change_emoji} {change:+.2f}% (24h)\n"
                   f"Market Cap: {self.format_market_cap(data['market_cap'])}\n"
                   f"🌱 Sustainability Score: {sustainability}/10")

        # Handle greeting
        if 'greeting' in keywords:
            return ("👋 Hello there! I'm here to help with crypto insights.\n"
                   "Ask me about trending coins, sustainable options, or specific prices!")

        # Handle sustainability queries
        if 'sustainable' in keywords:
            sustainable_cryptos = self.get_sustainable_cryptos()
            if sustainable_cryptos:
                response = "🌱 Most sustainable cryptocurrencies:\n"
                for crypto_id, score in sustainable_cryptos[:3]:
                    name = self.crypto_data[crypto_id]['name']
                    price = self.format_price(self.crypto_data[crypto_id]['current_price'])
                    response += f"• {name}: {score}/10 sustainability score (${price})\n"
                response += "\n💡 These use energy-efficient consensus mechanisms!"
                return response
            else:
                return "🌱 All tracked cryptos have sustainability considerations. Consider researching Proof-of-Stake coins!"

        # Handle trending queries
        if 'trending' in keywords:
            trending = self.get_trending_cryptos()
            if trending:
                response = "📈 Currently trending (24h gains):\n"
                for crypto_id in trending[:5]:
                    data = self.crypto_data[crypto_id]
                    name = data['name']
                    change = data.get('price_change_percentage_24h', 0)
                    price = self.format_price(data['current_price'])
                    response += f"• {name}: +{change:.2f}% ({price})\n"
                return response
            else:
                return "📉 No cryptos are showing strong upward trends right now. Market might be consolidating!"

        # Handle price queries
        if 'price' in keywords:
            response = "💰 Current crypto prices:\n"
            sorted_cryptos = sorted(self.crypto_data.items(), 
                                  key=lambda x: x[1]['market_cap_rank'])
            for crypto_id, data in sorted_cryptos[:5]:
                name = data['name']
                price = self.format_price(data['current_price'])
                change = data.get('price_change_percentage_24h', 0)
                change_emoji = "📈" if change > 0 else "📉" if change < 0 else "➡️"
                response += f"• {name}: {price} {change_emoji} {change:+.2f}%\n"
            return response

        # Handle market cap queries
        if 'market' in keywords:
            response = "📊 Top cryptocurrencies by market cap:\n"
            sorted_cryptos = sorted(self.crypto_data.items(), 
                                  key=lambda x: x[1]['market_cap'], reverse=True)
            for crypto_id, data in sorted_cryptos[:5]:
                name = data['name']
                market_cap = self.format_market_cap(data['market_cap'])
                rank = data['market_cap_rank']
                response += f"#{rank} {name}: {market_cap}\n"
            return response

        # Handle profit/investment queries
        if 'profit' in keywords:
            trending = self.get_trending_cryptos()
            sustainable = [crypto[0] for crypto in self.get_sustainable_cryptos()]
            
            # Find cryptos that are both trending and sustainable
            best_options = [crypto for crypto in trending if crypto in sustainable]
            
            if best_options:
                response = "💰 Potentially profitable & sustainable options:\n"
                for crypto_id in best_options[:3]:
                    data = self.crypto_data[crypto_id]
                    name = data['name']
                    change = data.get('price_change_percentage_24h', 0)
                    sustainability = self.sustainability_scores.get(crypto_id, 5)
                    response += f"• {name}: +{change:.2f}% today, {sustainability}/10 sustainability\n"
                response += "\n⚠️ Remember: All crypto investments are risky!"
                return response
            else:
                return ("💡 For investment ideas, consider:\n"
                       "• Check trending cryptos for momentum\n"
                       "• Look at sustainable options for long-term value\n"
                       "• Always do your own research!\n"
                       "⚠️ Crypto is highly volatile and risky!")

        # Default response
        return ("🤔 I can help you with:\n"
               "• 'What's trending?' - See rising cryptos\n"
               "• 'Most sustainable crypto?' - Eco-friendly options\n"
               "• 'Bitcoin price?' - Specific crypto info\n"
               "• 'Market leaders?' - Top cryptocurrencies\n"
               "• 'Investment advice?' - Profit potential analysis")

    def chat(self):
        """Main chat loop"""
        self.fetch_crypto_data()
        self.greet()
        
        print("\n" + "="*50)
        print("💬 Chat started! Type 'exit', 'quit', or 'bye' to end.")
        print("="*50)
        
        while True:
            try:
                user_input = input("\n🙋 You: ").strip()
                
                if not user_input:
                    print("Cryptopal: Please ask me something! 😊")
                    continue
                
                if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                    print("\nCryptopal: 👋 Thanks for chatting! Remember:")
                    print("• 🔍 Always do your own research")
                    print("• 💰 Never invest more than you can afford to lose")
                    print("• 📚 Keep learning about crypto!")
                    print("Goodbye! 🚀")
                    break
                
                response = self.respond_to_query(user_input)
                print(f"\nCryptopal: {response}")
                
            except KeyboardInterrupt:
                print("\n\nCryptopal: 👋 Goodbye! Stay safe in the crypto world!")
                break
            except Exception as e:
                print(f"\nCryptopal: 😅 Sorry, I encountered an error: {e}")
                print("Please try asking something else!")

def main():
    """Run the chatbot"""
    chatbot = CryptoChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main()