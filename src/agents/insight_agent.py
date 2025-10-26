from langchain_core.runnables import RunnableLambda
from .groq_llm import GroqLLM
from pathlib import Path

def get_insight_agent(config):
    llm = GroqLLM(config['groq_model'], config['groq_api_key'])
    insight_prompt = Path('prompts/insight_agent_prompt.md').read_text()

    def insights(data_summary):
        prompt = insight_prompt.replace("{data_summary}", str(data_summary))
        llm_output = llm.call(prompt)
        # Example/fallback logic, extend so parse llm_output into structured hypotheses if desired.
        hypotheses = [
            {
                'id': 'H1',
                'hypothesis': 'ROAS dropped in the last period',
                'data': {'roas_change': data_summary["recent_7_days"]["mean_roas"] - data_summary["previous_7_days"]["mean_roas"]}
            },
            {
                'id': 'H2',
                'hypothesis': 'Several campaigns have low CTR needing creative refresh',
                'data': {'low_ctr_count': len(data_summary["low_ctr_campaigns"])}
            }
        ]
        return {"hypotheses": hypotheses, "llm_output": llm_output}
    return RunnableLambda(insights)
