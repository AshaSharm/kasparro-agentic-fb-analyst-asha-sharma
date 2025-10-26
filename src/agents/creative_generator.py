from langchain_core.runnables import RunnableLambda
from .groq_llm import GroqLLM
from pathlib import Path

def get_creative_generator(config):
    llm = GroqLLM(config['groq_model'], config['groq_api_key'])
    creative_prompt = Path('prompts/creative_generator_prompt.md').read_text()

    def generate(inputs):
        # Accepts a single argument, a dict with at least 'data_summary' and 'validated'
        data_summary = inputs.get("data_summary", {})
        validated = inputs.get("validated", {})
        
        # Construct LLM prompt, passing creative and validation context.
        prompt = creative_prompt.replace("{low_ctr_campaigns}", str(data_summary.get("low_ctr_campaigns", [])))
        prompt += "\n\nValidated Insights:\n" + str(validated.get("validated_hypotheses", []))
        
        llm_output = llm.call(prompt)
        
        # Fallback/postprocessing for recommendations:
        recs = []
        for campaign in data_summary.get('low_ctr_campaigns', [])[:10]:
            campaign_name = campaign.get('campaign_name', 'unknown campaign')
            new_msg = f"Now try our improved {campaign_name} comfort range!"
            recs.append({
                "campaign_name": campaign_name,
                "current_ctr": campaign.get('mean_ctr', 0),
                "original_message": campaign.get("creative_message", ""),
                "new_message": new_msg,
                "strategy": "Add urgency",
                "reasoning": "Automated creative optimization based on analytic insights"
            })
        return {
            "recommendations": recs,
            "llm_output": llm_output
        }
    return RunnableLambda(generate)
