# 🧠 AI Web Scraper with Summarization

An AI-powered web scraper that extracts content from websites and uses open-source large language models to generate concise, context-aware summaries. Built for ease of use and real-time insights.

## 🚀 Technologies Used

- [Streamlit](https://streamlit.io/) – For interactive UI
- [Selenium](https://www.selenium.dev/) – For dynamic webpage automation
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) – For parsing HTML content
- [LangChain](https://www.langchain.com/) – For managing LLM workflows
- [Groq API](https://console.groq.com/) – To run open-source LLMs like **LLaMA3-70B-8192**

> **Note**: This project uses **ChromeDriver** (Version: 135.0.7049.84 (r1427262)) for Selenium.
> If you already have Google Chrome installed and up-to-date — you're good to go!  

## 🛠️ How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-web-scraper.git
   cd ai-web-scraper
2. (Optional but recommended) Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Set up your Groq API Key
   1. Go to Groq Console
   2. Create a new API key
   3. Open parse.py and paste the key into the open_api_key variable:
      ```bash
      open_api_key = "your_api_key_here"
4. Install Dependencies
   ```bash
   pip install -r requirements.txt
5. Run the app
   ```bash
   streamlit run main.py
6. Start Scraping!
   
A web interface will open in your browser where you can enter URLs and get summarized content powered by LLaMA3.
Feel free to contribute or raise issues. Happy scraping! 🕷️🧠
