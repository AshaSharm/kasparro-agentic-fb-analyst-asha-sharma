### 🧠 Kasparro Agentic Facebook Performance Analyst
### 🚀 Overview

Kasparro Agentic FB Analyst is an AI-driven multi-agent system designed to analyze Facebook Ads performance.
It autonomously diagnoses causes behind Return On Ad Spend (ROAS) fluctuations, generates data-driven hypotheses, validates them quantitatively, and recommends optimized creative messaging to improve campaign results.

![image alt](https://github.com/AshaSharm/kasparro-agentic-fb-analyst-asha-sharma/blob/main/flowchart.png?raw=true)

### 🖼️ System Architecture

### ✨ Key Features

🧩 Decomposes user queries into modular analytic subtasks

🧹 Loads and cleans Facebook Ads dataset with detailed preprocessing

📊 Generates insights and hypotheses about performance trends

📈 Validates hypotheses using rigorous quantitative metrics

💡 Produces actionable creative recommendations for weak campaigns

📝 Outputs detailed markdown and JSON reports for easy consumption

🤖 Integrates Groq LLM API for language-model powered reasoning

⚙️ LangChain-based modular architecture for flexible agent orchestration

🧾 Trace logs all agent steps, reasoning, and outputs for reproducibility

### ⚙️ Getting Started
### ✅ Prerequisites

Python 3.10+

Groq API access and key

Synthetic Facebook Ads dataset (synthetic_fb_ads_undergarments.csv)

### 🧩 Installation

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

### 💻 Usage

Run the full analysis pipeline by providing an analytic query:

python src/run.py "Analyze ROAS drop in last 7 days"

### 🔁 What Happens Next

The intelligent multi-agent system executes these steps:

Planner Agent → Interprets your query and defines subtasks

Data Agent → Loads, cleans, and summarizes the dataset

Insight Agent → Generates hypotheses for performance shifts

Evaluator Agent → Validates hypotheses with confidence scores

Creative Generator → Suggests optimized ad creatives

Report Generator → Produces markdown, JSON, and trace logs

### 📂 Folder Structure
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

### 📊 Outputs

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

### Reflection Loop Example
The evaluator checks each hypothesis against a confidence threshold (e.g., 0.6). If any fall below, it would retry with a revised plan or data. In the example below, both hypotheses met threshold on the first attempt so only one attempt is logged.
{
  "attempt": 1,
  "validated": [
    {
      "hypothesis": "ROAS dropped in the last period",
      "confidence": 0.95,
      "evidence": "ROAS change of 3.79 detected",
      "quantitative_validation": true,
      "details": {
        "roas_change": 3.7935774557877355
      }
    },
    {
      "hypothesis": "Several campaigns have low CTR needing creative refresh",
      "confidence": 0.9,
      "evidence": "10 campaigns below CTR threshold",
      "quantitative_validation": true,
      "details": {
        "low_ctr_count": 10
      }
    }
  ]
}

### Evaluator Pass Example
"hypothesis": "ROAS dropped in the last period",
      "confidence": 0.95,
      "evidence": "ROAS change of 3.79 detected",
      "quantitative_validation": true,
      "details": {
        "roas_change": 3.7935774557877355}

### 📝 Notes

To comply with data policy, only a small sample dataset (sample_fb_ads.csv) is included. For full analysis, update data_path in config.yaml to your complete dataset location.

✅ Ensure your Groq API key and model name are valid.

🧼 The system performs robust preprocessing to ensure data integrity.

🧠 Agents are modular — you can independently update or extend them.

🧩 Designed for clarity, robustness, and production readiness.
