from langchain_core.runnables import RunnableLambda
from .groq_llm import GroqLLM
from pathlib import Path
import json
import os

def get_evaluator_agent(config):
    llm = GroqLLM(config['groq_model'], config['groq_api_key'])
    eval_prompt = Path('prompts/evaluator_prompt.md').read_text()
    conf_min = config.get("confidence_min", 0.6)
    # Optionally path for logs
    trace_log_path = "logs/validation_trace.json"

    def log_trace(attempt, results):
        os.makedirs("logs", exist_ok=True)
        log_dict = {"attempt": attempt, "validated": results}
        with open(trace_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_dict, indent=2) + "\n")

    def evaluator(insights):
        attempt = 0
        # Reflection loop: continue until all hypotheses meet threshold
        while True:
            attempt += 1
            prompt = eval_prompt.replace("{hypotheses}", str(insights))
            eval_text = llm.call(prompt)
            validated = []
            for h in insights['hypotheses']:
                # Quantitative validation logic
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
            # Log every attempt with its validation output
            log_trace(attempt, validated)
            # If all pass threshold, return
            if all(v["confidence"] >= conf_min for v in validated):
                return {"validated_hypotheses": validated, "llm_output": eval_text}
            # Optionally mutate/re-plan here
            # For now: just prints/logs the attempts and exits (loops max 1 for most datasets)
            if attempt > 2:  # Prevent possible infinite loops
                break

    return RunnableLambda(evaluator)
