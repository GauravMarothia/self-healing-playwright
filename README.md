# 🚀 AI-Powered Self-Healing Playwright Framework

[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stack: Python &
Playwright](https://img.shields.io/badge/Stack-Python%20%7C%20Playwright-blue)](https://playwright.dev/python/)
[![AI: OpenRouter
Enabled](https://img.shields.io/badge/AI-OpenRouter%20%7C%20GPT--4o--mini-orange)](https://openrouter.ai/)


## 📈 Strategic Overview

Modern Agile teams spend significant time fixing broken UI locators.\
This framework introduces an AI-driven self-healing engine that detects
locator failures and automatically recovers using LLMs via OpenRouter.

Instead of failing tests immediately, the framework: - Intercepts
locator failures - Sends DOM + context to LLM - Identifies updated
element - Applies new locator - Resumes execution automatically


## 💼 Business Value & ROI

-   Reduce maintenance effort by up to 70%
-   Faster CI/CD stability
-   AI triggered only on failures (cost optimized)
-   Vendor flexibility via OpenRouter
-   Healing logs for tech debt cleanup


## 🛠 Tech Stack

-   Python 3.10+
-   Playwright
-   PyTest
-   OpenRouter API
-   Docker & GitHub Actions


## 🧠 How It Works

1.  Failure interception via BasePage wrapper
2.  DOM + failed selector captured
3.  Sent to OpenRouter LLM
4.  New locator returned
5.  Test resumes automatically


## 🔧 Installation

Clone repo:

    git clone https://github.com/yourusername/self-healing-playwright.git
    cd self-healing-playwright

Create venv:

    python -m venv venv

Activate: Windows:

    venv\Scripts\activate

Mac/Linux:

    source venv/bin/activate

Install:

    pip install -r requirements.txt
    playwright install chromium

Create .env:

    OPENAI_API_KEY=your_openrouter_key_here

Run tests:

    python -m pytest -s tests/test_dynamic_ui.py


## 📁 Project Structure

```
self-healing-playwright/
│
├── .github/                # CI/CD workflows (GitHub Actions)
│   └── workflows/
│       └── main.yml
│
├── config/                 # Global configuration settings
│   └── settings.py         # Model selection, timeouts, and API endpoints
│
├── src/
│   │── core/               # The "Brain" of the framework
│   │    ├── __init__.py
│   │    └── healer.py           # AI/OpenRouter interaction logic
│   │
│   └── pages/                  # Page Object Model (POM) classes
│        ├── __init__.py
│        ├── base_page.py        # Smart wrapper with self-healing click/type
│        └── login_page.py       # Example application page objects
│
├── tests/                  # Test suites
│   ├── __init__.py
│   ├── conftest.py         # PyTest fixtures for browser setup
│   └── test_dynamic_ui.py  # Self-healing demonstration tests
│
├── utils/                  # Helper functions
│   ├── logger.py           # Custom logging for healing events
│   └── dom_parser.py       # HTML truncation and cleaning for AI
│
├── test_data/              # Mock data or JSON blueprints
│   └── element_registry.json
│
├── reports/                # AI Healing reports and PyTest results
│   └── healing_logs.json
│
├── docker/                 # Containerization
│   └── Dockerfile
│
├── .env                    # Private API keys (git-ignored!)
├── .gitignore              # Files to exclude from GitHub
├── README.md               # Project documentation & strategy
└── requirements.txt        # Python dependencies
```


## ⚙️ Example Healing Flow
    
    ❌ Original locator fails
    ⬇
    🧠 LLM analyzes DOM
    ⬇
    🔁 New locator generated
    ⬇
    ✅ Test resumes automatically


## 🐳 Docker Support

Build container:

    docker build -t ai-self-healing-tests .

Run tests:

    docker run ai-self-healing-tests


## 🔐 Security & Cost Control

-   AI triggered only on failure
-   DOM truncated to reduce token usage
-   No sensitive test data sent externally (configurable masking)
-   Vendor-agnostic via OpenRouter


## 🛠 Troubleshooting

| Issue | Cause | Solution |
|---------|------|---------|
| ModuleNotFoundError: src | Python path issue | Run using python -m pytest |
| 401 Invalid API Key | Wrong OpenRouter key | Ensure key starts with sk-or- |
| Tests not healing | DOM too large | Use specific parent locators |
| venv not activating | Environment inactive | Activate using OS command |


## 📊 Roadmap

Completed
- [x]  Self-healing locator engine
- [x]  OpenRouter multi-model support
- [x]  Fail-only AI trigger
- [x]  CI-ready execution

Upcoming
- [ ]  Auto-PR generation for healed locators
- [ ]  Visual validation via computer vision
- [ ]  Selector learning database (persistence layer)
- [ ]  Dashboard for healing analytics
- [ ]  Slack/Jira healing notifications


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📜 License

MIT License — free to use and modify.


## ⭐ Why This Project Matters

UI automation maintenance is one of the biggest hidden costs in QA.
This framework demonstrates how AI can shift QA from reactive to autonomous.

If you're building next-gen QA systems or exploring AI in testing — this project is a strong foundation.


## 📞 Contact

**Your Name** - [hire.gauravmarothia@gmail.com](mailto:your.email@example.com)

**Project Link:** [https://github.com/GauravMarothia/self-healing-playwright.git](https://github.com/GauravMarothia/self-healing-playwright.git)

**⭐ If you find this framework useful, please consider giving it a star!**

