from langchain_core.runnables import RunnableLambda
from .groq_llm import GroqLLM
from pathlib import Path

def get_planner_agent(config):
    llm = GroqLLM(config['groq_model'], config['groq_api_key'])
    planner_prompt = Path('prompts/planner_prompt.md').read_text()
    def planner(query):
        prompt = planner_prompt.replace("{query}", query)
        plan_text = llm.call(prompt)
        return {
            "subtasks": [
                {"id": 1, "task": "summarize data", "agent": "data_agent"},
                {"id": 2, "task": "find ROAS/CTR trends", "agent": "insight_agent"},
                {"id": 3, "task": "validate hypotheses", "agent": "evaluator"},
                {"id": 4, "task": "recommend creatives", "agent": "creative_generator"},
            ],
            "llm_plan_explanation": plan_text
        }
    return RunnableLambda(planner)
