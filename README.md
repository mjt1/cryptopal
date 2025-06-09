# 🤖 CryptoPal - Cryptocurrency Chatbot

A friendly, intelligent cryptocurrency advisor chatbot that provides real-time market data, sustainability insights, and investment guidance through natural language conversations.

## 🚀 Features

### 💬 Natural Language Processing
- Advanced query understanding using NLTK
- Keyword extraction and intent recognition
- Support for casual conversation and specific crypto queries

### 📊 Real-Time Market Data
- Live cryptocurrency prices from CoinGecko API
- 24-hour price change tracking
- Market capitalization rankings
- Automatic data refresh every 5 minutes

### 🌱 Sustainability Analysis
- Eco-friendly cryptocurrency recommendations
- Sustainability scoring based on consensus mechanisms
- Focus on energy-efficient Proof-of-Stake coins

### 📈 Market Intelligence
- Trending cryptocurrency identification
- Investment potential analysis
- Price trend monitoring
- Market cap comparisons

### 🛡️ Robust Error Handling
- Graceful API failure recovery
- SSL certificate issue resolution
- Comprehensive fallback data system
- Network timeout protection

## 🎯 What CryptoPal Can Help With

- **"What's trending?"** - Shows cryptocurrencies with positive 24h gains
- **"Most sustainable crypto?"** - Recommends eco-friendly options
- **"Bitcoin price?"** - Provides specific cryptocurrency information
- **"Market leaders?"** - Displays top cryptocurrencies by market cap
- **"Investment advice?"** - Analyzes profit potential with risk warnings

## 📋 Requirements

### System Requirements
- Python 3.7 or higher
- Internet connection (for live data)
- 50MB+ free space

### Python Dependencies
```
requests>=2.25.0
nltk>=3.6
urllib3>=1.26.0
```

## 🔧 Installation

### 1. Clone or Download
```bash
git clone https://github.com/yourusername/crypto-chatbot.git
cd crypto-chatbot
```

### 2. Install Dependencies
```bash
pip install requests nltk urllib3
```

### 3. Run the Chatbot
```bash
python crypto_chatbot.py
```

### 4. First-Time Setup
The chatbot will automatically:
- Download required NLTK data packages
- Attempt to fetch live cryptocurrency data
- Set up fallback data if API is unavailable

## 🎮 Usage Examples

### Basic Queries
```
You: hi
CryptoPal: 👋 Hello there! I'm here to help with crypto insights.
         Ask me about trending coins, sustainable options, or specific prices!

You: what's trending?
CryptoPal: 📈 Currently trending (24h gains):
         • Solana: +4.50% ($189.00)
         • Cardano: +3.10% ($0.6200)
         • Ethereum: +2.80% ($3,890.00)
```

### Sustainability Focus
```
You: which crypto is most sustainable?
CryptoPal: 🌱 Most sustainable cryptocurrencies:
         • Cardano: 9/10 sustainability score ($0.6200)
         • Algorand: 9/10 sustainability score ($0.3400)
         • Solana: 8/10 sustainability score ($189.00)
         
         💡 These use energy-efficient consensus mechanisms!
```

### Specific Cryptocurrency Info
```
You: tell me about ethereum
CryptoPal: 💰 Ethereum (ETH)
         Price: $3,890.00 📈 +2.80% (24h)
         Market Cap: $467.0B
         🌱 Sustainability Score: 7/10
```

## 🏗️ Architecture

### Class Structure
```
CryptoChatbot
├── __init__()           # Initialize chatbot with settings
├── fetch_crypto_data()  # Get real-time API data
├── analyze_query()      # Process natural language input
├── respond_to_query()   # Generate intelligent responses
└── chat()              # Main conversation loop
```

### Data Sources
- **Primary**: CoinGecko API (live market data)
- **Fallback**: Built-in cryptocurrency dataset
- **Sustainability**: Research-based consensus mechanism scores

### Key Components
- **NLTK**: Natural language processing and tokenization
- **Requests**: HTTP API communication with error handling
- **DateTime**: Data freshness management and caching
- **SSL Handling**: Certificate verification and fallback methods

## 🔐 Security & Privacy

### Data Handling
- No personal data storage or transmission
- No financial transaction capabilities
- Read-only market data access
- Local conversation processing

### Network Security
- SSL/TLS encryption for API communications
- Certificate verification with fallback options
- Timeout protection against hanging requests
- No sensitive credential requirements

## 🛠️ Configuration

### API Settings
```python
# Modify these in the CryptoChatbot class
update_interval = timedelta(minutes=5)  # Data refresh frequency
api_timeout = 10                        # Request timeout in seconds
```

### Cryptocurrency Selection
```python
# Add/remove cryptocurrencies in the API params
'ids': 'bitcoin,ethereum,cardano,solana,polygon,algorand,tezos,stellar'
```

### Sustainability Scores
```python
# Customize sustainability ratings (1-10 scale)
self.sustainability_scores = {
    'bitcoin': 2,      # Proof of Work - high energy
    'ethereum': 7,     # Proof of Stake - improved
    'cardano': 9,      # Proof of Stake - very efficient
    # Add more cryptocurrencies...
}
```

## 🚨 Troubleshooting

### Common Issues

#### SSL Certificate Errors
```
⚠️ SSL Certificate issue detected.
💡 This is common on some networks. Using reliable fallback data.
```

**Solutions:**
1. **Update certificates** (macOS):
   ```bash
   /Applications/Python\ 3.x/Install\ Certificates.command
   ```

2. **Update packages**:
   ```bash
   pip install --upgrade requests urllib3 certifi
   ```

3. **Corporate networks**: The chatbot automatically falls back to offline data

#### API Rate Limiting
- CoinGecko allows 10-50 requests/minute for free tier
- Chatbot includes 5-minute caching to stay within limits
- Fallback data ensures continuous operation

#### NLTK Data Missing
```
LookupError: Resource punkt not found
```
**Solution**: The chatbot auto-downloads required NLTK data on first run

### Performance Tips
- First startup may take 10-20 seconds (downloading NLTK data)
- Subsequent runs are faster with cached data
- Internet connection required only for live prices
- Fallback mode works completely offline

## 🔮 Future Enhancements

### Planned Features
- [ ] Technical analysis indicators (RSI, moving averages)
- [ ] Portfolio tracking and performance analysis
- [ ] News sentiment analysis integration
- [ ] Price alert notifications
- [ ] Historical price chart generation
- [ ] DeFi protocol information
- [ ] NFT market insights

### Advanced Integrations
- [ ] Multiple exchange price comparison
- [ ] Social media sentiment tracking
- [ ] Regulatory news monitoring
- [ ] Staking rewards calculator
- [ ] Carbon footprint tracking

## 📚 Educational Resources

### Cryptocurrency Basics
- **Blockchain**: Distributed ledger technology
- **Consensus Mechanisms**: Proof of Work vs Proof of Stake
- **Market Cap**: Total value of all coins in circulation
- **Volatility**: Price fluctuation characteristics

### Investment Considerations
- **Risk Management**: Never invest more than you can afford to lose
- **Research**: Always conduct thorough due diligence
- **Diversification**: Don't put all funds in a single cryptocurrency
- **Regulation**: Stay informed about legal requirements in your jurisdiction

## 📞 Support & Contributing

### Getting Help
- Create an issue on GitHub for bugs or feature requests
- Check existing issues for known problems
- Provide error messages and system information

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Add comprehensive docstrings for new functions
- Include error handling for all API interactions
- Test with both live and fallback data scenarios

## ⚠️ Disclaimer

**Important Notice**: This chatbot is for educational and informational purposes only.

- **Not Financial Advice**: Responses are not professional investment advice
- **High Risk**: Cryptocurrency investments are highly volatile and risky
- **Do Your Research**: Always conduct independent research before investing
- **Regulatory Compliance**: Ensure compliance with local laws and regulations
- **No Guarantees**: Past performance does not indicate future results

The developers are not responsible for any financial losses incurred through the use of this software.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CoinGecko**: For providing free cryptocurrency market data API
- **NLTK Team**: For natural language processing capabilities
- **Python Community**: For excellent libraries and documentation
- **Cryptocurrency Community**: For open-source collaboration and education
- **PLP Team for the opportunity

---
## Screenshot

![image](https://github.com/user-attachments/assets/316db203-5550-47cb-9327-d64374927192)



**Built with ❤️ for the crypto community by Mercylyne Jepleting**

*Remember: The best investment is in your education. Keep learning! 🚀*
