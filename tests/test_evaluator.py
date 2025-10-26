from agents.evaluator import get_evaluator_agent

def test_eval():
    mock_config = {"confidence_min": 0.6, "groq_model": "llama3-8b-8192", "groq_api_key": "demo"}
    agent = get_evaluator_agent(mock_config)
    sample = {'hypotheses': [
        {'hypothesis': 'ROAS dropped in the last period', 'data': {'roas_change': -0.22}},
        {'hypothesis': 'Low CTR detected', 'data': {'low_ctr_count': 7}}
    ]}
    results = agent.invoke(sample)
    assert len(results['validated_hypotheses']) == 2

print("✓ Evaluator agent test passed.")
