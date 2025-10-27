🧠 Kasparro Agentic Facebook Performance Analyst
🚀 Overview

Kasparro Agentic FB Analyst is an AI-driven multi-agent system designed to analyze Facebook Ads performance.
It autonomously diagnoses causes behind Return On Ad Spend (ROAS) fluctuations, generates data-driven hypotheses, validates them quantitatively, and recommends optimized creative messaging to improve campaign results.



🖼️ System Architecture

✨ Key Features

🧩 Decomposes user queries into modular analytic subtasks

🧹 Loads and cleans Facebook Ads dataset with detailed preprocessing

📊 Generates insights and hypotheses about performance trends

📈 Validates hypotheses using rigorous quantitative metrics

💡 Produces actionable creative recommendations for weak campaigns

📝 Outputs detailed markdown and JSON reports for easy consumption

🤖 Integrates Groq LLM API for language-model powered reasoning

⚙️ LangChain-based modular architecture for flexible agent orchestration

🧾 Trace logs all agent steps, reasoning, and outputs for reproducibility

⚙️ Getting Started
✅ Prerequisites

Python 3.10+

Groq API access and key

Synthetic Facebook Ads dataset (synthetic_fb_ads_undergarments.csv)

🧩 Installation

1. Clone this repository

git clone https://github.com/<your-username>/kasparro-agentic-fb-analyst.git
cd kasparro-agentic-fb-analyst


2. Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate


3. Install dependencies

pip install -r requirements.txt


4. Place the dataset file in the data/ directory.

⚙️ Configuration

Edit the configuration file at:

config/config.yaml


Specify the following fields:

groq_api_key: your_groq_api_key_here
groq_model: your_active_groq_model_name
data_path: data/synthetic_fb_ads_undergarments.csv


You can also modify pipeline thresholds and parameters as needed.

💻 Usage

Run the full analysis pipeline by providing an analytic query:

python src/run.py "Analyze ROAS drop in last 7 days"

🔁 What Happens Next

The intelligent multi-agent system executes these steps:

Planner Agent → Interprets your query and defines subtasks

Data Agent → Loads, cleans, and summarizes the dataset

Insight Agent → Generates hypotheses for performance shifts

Evaluator Agent → Validates hypotheses with confidence scores

Creative Generator → Suggests optimized ad creatives

Report Generator → Produces markdown, JSON, and trace logs

📂 Folder Structure
kasparro-agentic-fb-analyst/
│
├── README.md                     # This document
├── requirements.txt              # Python dependencies
│
├── config/
│   └── config.yaml               # Pipeline and API configuration
│
├── data/
│   ├── synthetic_fb_ads_undergarments.csv  # Ads dataset
│   └── README.md                 # Data schema & usage notes
│
├── src/
│   ├── run.py                    # Main orchestrator
│   └── agents/                   # Modular LangChain agents
│       ├── groq_llm.py
│       ├── planner.py
│       ├── data_agent.py
│       ├── insight_agent.py
│       ├── evaluator.py
│       └── creative_generator.py
│
├── prompts/                      # LLM prompt templates
├── reports/                      # Analysis outputs (md, json)
├── logs/                         # Execution traces
└── tests/                        # Unit tests

📊 Outputs

After running the pipeline, you’ll get:

File	Description
reports/report.md	Human-readable summary and analysis report
reports/insights.json	Validated hypotheses with confidence and evidence
reports/creatives.json	Campaign-specific creative recommendations
logs/trace.json	Workflow and agent execution trace for reproducibility
🧩 Interpretation

The system analyzes your query using dataset summaries and LLM-powered reasoning.

Hypotheses about ROAS drops, CTR issues, or creative fatigue are generated and quantitatively validated.

Underperforming campaigns receive personalized creative message suggestions.

Reports deliver clear, actionable insights for data-driven marketing decisions.

📝 Notes

✅ Ensure your Groq API key and model name are valid.

🧼 The system performs robust preprocessing to ensure data integrity.

🧠 Agents are modular — you can independently update or extend them.

🧩 Designed for clarity, robustness, and production readiness.
