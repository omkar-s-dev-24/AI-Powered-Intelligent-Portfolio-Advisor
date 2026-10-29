<div align="center">

# 📈 AI-Powered Intelligent Portfolio Advisor

### A full-stack quantitative dashboard for analyzing Indian stock market equities

**Python** • **Django** • **Pandas** • **NumPy** • **yfinance** • **feedparser** • **Bootstrap 5** • **Chart.js** • **SQLite3**

</div>

---

## 📖 Description

**AI-Powered Intelligent Portfolio Advisor** is a full-stack web application that brings institutional-style quantitative analysis to Indian equity investors. It pulls live market data, applies statistical and risk models with **Pandas** and **NumPy**, and presents the results in a responsive dashboard with interactive **Chart.js** visualizations.

Instead of showing raw price charts, the platform answers the questions that matter: *How risky is this stock? How does it behave relative to the market? How does it compare with its peers? What is the overall outlook?* All of it is distilled into a single, explainable **AI Confidence Score**.

The application is deliberately **stateless**. Market data is fetched live on demand, so analysis always reflects current conditions and no stale data is stored.

---

## ✨ Core Features

### 📊 1. Live Market Dashboard
Tracks real-time movements of India's benchmark indices, **NIFTY 50**, **SENSEX** and **BANK NIFTY**, giving an at-a-glance view of overall market sentiment.

### 🤖 2. AI Stock Analyzer
Evaluates any listed equity across four dimensions and combines them into a single **AI Confidence Score**:

| Dimension | What it captures |
|-----------|------------------|
| 📉 **Technical Trends** | Price momentum and trend behavior |
| ⚠️ **Risk Profile** | Volatility and downside characteristics |
| 💬 **Sentiment** | Market perception and news-driven outlook |
| 🏦 **Financial Strength** | Fundamental health of the company |

> 🛡️ **Robust by design:** the analyzer handles missing or incomplete API data (`NaN` values) gracefully, so one absent field never breaks the analysis.

### 🧮 3. Advanced Risk Metrics
Computes industry-standard risk measures over rolling historical windows using Pandas and NumPy:

- **Volatility**: dispersion of returns
- **Beta**: sensitivity relative to the broader market
- **Sharpe Ratio**: risk-adjusted return
- **Maximum Drawdown**: worst peak-to-trough decline

### ⚖️ 4. Stock Comparison Engine
Compare multiple equities side by side with:

- **1-year rebased performance**, with every stock normalized to a common starting point for a fair comparison
- **Correlation analysis**, quantifying how closely stocks move together, which is essential for diversification

### 📰 5. Live Financial News
An RSS-driven news aggregator built on `feedparser` that streams real-time market headlines and keeps users informed alongside the numbers.

### ⚡ 6. Asynchronous, Reload-Free UI
Vanilla JavaScript (`fetch` API) calls the Django backend asynchronously and renders heavy financial computations as interactive **Chart.js** graphs, with **no page reloads** and no front-end framework overhead.

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Backend** | Python, Django |
| **Data Science & Math** | Pandas, NumPy, yfinance, feedparser |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript, Bootstrap 5 |
| **Visualization** | Chart.js |
| **Database** | SQLite3 (stateless architecture for live API fetching) |

---

## 🚀 Installation

### Prerequisites
- Python 3.9+
- `pip` and `git`

### Setup

**1️⃣ Clone the repository**
```bash
git clone https://github.com/<your-username>/AI-Powered-Intelligent-Portfolio-Advisor.git
cd AI-Powered-Intelligent-Portfolio-Advisor
```

**2️⃣ Create and activate a virtual environment**
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS / Linux)
source venv/bin/activate
```

**3️⃣ Install dependencies**
```bash
pip install django yfinance pandas numpy feedparser
```

**4️⃣ Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5️⃣ Run the development server**
```bash
python manage.py runserver
```

🎉 Open **http://127.0.0.1:8000/** in your browser to start exploring.

---

## 📂 Project Structure

```text
AI-Powered-Intelligent-Portfolio-Advisor/
│
├── advisor/                    # Main Django Application
│   ├── templates/              # HTML frontend templates (analyzer, compare, risk, etc.)
│   ├── views.py                # Core Python logic (yfinance integration, Pandas math)
│   ├── urls.py                 # API and View routing
│   └── models.py               # Database schemas
│
├── portfolio_project/          # Django Project Configuration
│   ├── settings.py             # Global settings
│   └── urls.py                 # Root URL routing
│
├── manage.py                   # Django execution script
├── db.sqlite3                  # Local database
└── README.md                   # Project documentation
```

---

## 🔮 Future Enhancements

- [ ] 🎯 **Modern Portfolio Theory (MPT) optimization**: compute optimal stock weights along the efficient frontier
- [ ] ⚡ **Django-Cache / Redis**: cache responses to bypass third-party API rate limits and cut latency
- [ ] 🔐 **User authentication**: personalized, persistent watchlists for each user

---

## ⚠️ Disclaimer

This project is built for **educational and analytical purposes only**. It does not constitute financial advice. Always conduct your own research or consult a licensed financial advisor before making investment decisions.

---

<div align="center">

⭐ If you found this project useful, consider giving it a star!

</div>
