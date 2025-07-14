# 📈 Crypto Market Sentiment Analyzer (VIBE)

This project is a Python-based tool that fetches real-time cryptocurrency data (prices, volume) and combines it with sentiment analysis from recent news headlines. It generates a comprehensive HTML report to give traders a quick overview of market sentiment for Bitcoin, Ethereum, and Solana.

## ✨ Features
- **Real-Time Data**: Fetches current prices, 24h % change, and volume from the CoinGecko API.
- **News Aggregation**: Gathers the latest news for each crypto using the NewsAPI.
- **Offline Sentiment Analysis**: Analyzes news headlines using a combination of **VADER** and **TextBlob** for a good average and robust sentiment score. No external LLM APIs are needed for this step.
- **Dynamic HTML Reports**: Generates a clean, easy-to-read HTML report with all the consolidated data.

---

## 🛠️ Setup and Installation

Follow these steps to get the project running on your local machine.

### **1. Clone the Repository**
```bash
git clone [https://github.com/YOUR_USERNAME/crypto-sentiment-analyzer.git](https://github.com/YOUR_USERNAME/crypto-sentiment-analyzer.git)
cd crypto-sentiment-analyzer
```

### **2. Create and Activate a Python Virtual Environment**
- On macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### **3. Install Dependencies**
Install all the required libraries from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### **4. Set Up API Key**
This project requires a free API key from [NewsAPI](https://newsapi.org/).
1. Get your API key from the NewsAPI website.
2. Create a file named `.env` in the root of the project directory.
3. Add your API key to the `.env` file like this:
   ```
   NEWS_API_KEY="YOUR_NEWS_API_KEY_HERE"
   ```

---

## 🚀 How to Run

With the setup complete, run the main script from the root directory:

```bash
python main.py
```

The script will fetch the latest data, perform the analysis, and generate a report named `crypto_report.html` in the project folder. Open this file in your browser to see the results.

---

## 🤖 History and Use of LLMs

While this project uses offline libraries (VADER, TextBlob) for the rough sentiment analysis to meet the requirements, LLMs were instrumental in the development process. Here is a simulated history of prompts used:

1.  **Initial Planning:** *"Act as a senior software architect. Design a modular Python application for a crypto sentiment analyzer. The components should be: data collection, sentiment analysis, and report generation. What would the file structure and key functions look like?"*
2.  **API Selection:** *"Compare public, free-to-use APIs for cryptocurrency prices. I need price, 24h volume, and 24h % change for Bitcoin, Ethereum, and Solana in a single call. Provide Python code examples for CoinGecko vs. CoinCap."*
3.  **Sentiment Logic:** *"I need to calculate a sentiment score for news headlines in Python, offline. Compare VADER and TextBlob. How can I combine their scores into a single, normalized 0-10 rating? Provide a function that does this."*
4.  **Report Templating:** *"Show me how to use Jinja2 in Python to generate an HTML file from a list of dictionaries. The template should include a table and a loop to create summary cards for each item."*
5.  **Error Handling:** *"Refactor this Python script that calls a web API to include robust error handling for network issues, HTTP 4xx/5xx errors, and missing JSON keys."*

---

## ⚠️ Known Limitations
- **API Rate Limits**: The free tiers of CoinGecko and NewsAPI have rate limits. Frequent execution of the script might lead to temporary blocking.
- **Sentiment Accuracy**: VADER and TextBlob are powerful but not infallible. Their analysis is based on pre-defined lexicons and may not capture complex sarcasm, irony, or crypto-specific jargon perfectly.
- **News Relevance**: The quality of the sentiment analysis is highly dependent on the relevance of the news articles returned by the NewsAPI.