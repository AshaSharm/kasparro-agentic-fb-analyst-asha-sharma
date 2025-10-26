Kasparro Agentic Facebook Performance Analyst

Overview

Kasparro Agentic FB Analyst is an AI-driven multi-agent system designed to analyze Facebook Ads performance. The system autonomously diagnoses causes behind Return On Ad Spend (ROAS) fluctuations, generates data-driven hypotheses, validates them quantitatively, and recommends optimized creative messaging to improve campaign results.

Features

Decomposes user queries into modular analytic subtasks

Loads and cleans Facebook Ads dataset with detailed preprocessing

Generates insights and hypotheses about performance trends

Validates hypotheses with rigorous quantitative metrics

Produces actionable creative recommendations for weak campaigns

Produces detailed markdown and JSON reports for easy consumption

Fully integrates with Groq LLM API for language-model powered reasoning

Modular LangChain-based architecture for flexible agent orchestration

Trace logs agent steps, reasoning, and outputs for reproducibility

Getting Started

Prerequisites

Python 3.10+

Groq API access and key

Synthetic Facebook Ads dataset (synthetic_fb_ads_undergarments.csv)

Installation
Clone this repository

Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Place the dataset file in the data/ directory.

Configuration
Edit config/config.yaml to specify:

groq_api_key: Your Groq API key

groq_model: Active Groq model name (verify in Groq console)

data_path: Path to dataset CSV

Other pipeline thresholds & parameters as needed

Usage
Run the full analysis pipeline from the command line by providing an analytic query:

python src/run.py "Analyze ROAS drop in last 7 days"
This triggers the intelligent multi-agent system that executes the following steps:

Planner Agent: Interprets your query and defines subtasks

Data Agent: Loads, cleans, preprocesses, and summarizes the dataset

Insight Agent: Generates hypotheses for performance shifts

Evaluator Agent: Validates hypotheses with confidence scores

Creative Generator: Recommends improved ad creatives

Report Generation: Outputs markdown & JSON insights + logs

Folder Structure

kasparro-agentic-fb-analyst/
│
├── README.md                # This document
├── requirements.txt         # Python dependencies
├── Makefile                # Shortcut for running the pipeline
│
├── config/
│   └── config.yaml         # Pipeline and API config
│
├── data/
│   ├── synthetic_fb_ads_undergarments.csv  # Ads dataset CSV
│   └── README.md            # Data schema and usage notes
│
├── src/
│   ├── run.py              # Main orchestrator
│   └── agents/             # Modular LangChain agents
│       ├── groq_llm.py     # Groq LLM wrapper
│       ├── planner.py
│       ├── data_agent.py
│       ├── insight_agent.py
│       ├── evaluator.py
│       └── creative_generator.py
│
├── prompts/                # LLM prompt templates
│
├── reports/                # Analysis outputs (md, json)
│
├── logs/                   # Execution traces
│
└── tests/                  # Unit tests


Outputs

After running the pipeline, outputs are generated in:

reports/report.md — Human-readable summary and analysis report

reports/insights.json — Validated hypotheses with confidence & evidence

reports/creatives.json — Campaign-specific creative recommendations

logs/trace.json — Workflow and agent execution trace for reproducibility

Interpretation
The system thoroughly analyzes your query using dataset summaries and LLM-powered reasoning.

Hypotheses about ROAS drops, CTR issues, or creative fatigue are generated and quantitatively validated.

Campaigns identified as underperforming receive personalized creative message suggestions.

Reports provide clear, actionable insights that support data-driven marketing decisions.


Notes

Ensure your Groq API key & chosen model are current and valid.

The system performs detailed preprocessing to ensure data integrity.

Modular agents can be individually updated or extended.

Designed for clarity, robustness, and production readiness.