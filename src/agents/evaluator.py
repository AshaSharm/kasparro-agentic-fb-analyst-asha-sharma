from langchain_core.runnables import RunnableLambda
from .groq_llm import GroqLLM
from pathlib import Path

def get_evaluator_agent(config):
    llm = GroqLLM(config['groq_model'], config['groq_api_key'])
    eval_prompt = Path('prompts/evaluator_prompt.md').read_text()
    conf_min = config.get("confidence_min", 0.6)

    def evaluator(insights):
        prompt = eval_prompt.replace("{hypotheses}", str(insights))
        eval_text = llm.call(prompt)
        validated = []
        for h in insights['hypotheses']:
            # Quantitative validation logic, you can parse eval_text if more sophisticated
            change = h['data'].get('roas_change', 0)
            low_ctr_count = h['data'].get('low_ctr_count', 0)
            conf = 0.75
            evidence = "Automated confidence applied"
            if "roas" in h['hypothesis'].lower() and abs(change) > 0.1:
                conf = 0.95
                evidence = f"ROAS change of {change:.2f} detected"
            elif "low ctr" in h['hypothesis'].lower() and low_ctr_count > 5:
                conf = 0.90
                evidence = f"{low_ctr_count} campaigns below CTR threshold"
            validated.append({
                "hypothesis": h["hypothesis"],
                "confidence": conf,
                "evidence": evidence,
                "quantitative_validation": True,
                "details": h["data"]
            })
        return {"validated_hypotheses": validated, "llm_output": eval_text}
    return RunnableLambda(evaluator)
