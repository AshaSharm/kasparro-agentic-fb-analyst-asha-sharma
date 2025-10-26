import sys
import yaml
import json
from pathlib import Path

from agents.planner import get_planner_agent
from agents.data_agent import get_data_agent
from agents.insight_agent import get_insight_agent
from agents.evaluator import get_evaluator_agent
from agents.creative_generator import get_creative_generator

def load_config():
    with open('config/config.yaml', 'r') as f:
        return yaml.safe_load(f)

def save_json(obj, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as fp:
        json.dump(obj, fp, indent=2)

def save_md(text, path):
    from pathlib import Path
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fp:
        fp.write(text)


def main(query):
    config = load_config()
    planner = get_planner_agent(config)
    data_agent = get_data_agent(config)
    insight_agent = get_insight_agent(config)
    evaluator = get_evaluator_agent(config)
    creative_gen = get_creative_generator(config)

    plan = planner.invoke(query)
    data_summary = data_agent.invoke(plan)
    insights = insight_agent.invoke(data_summary)
    validated = evaluator.invoke(insights)
    creatives = creative_gen.invoke({
    "data_summary": data_summary,
    "validated": validated
    })

    save_json(validated, 'reports/insights.json')
    save_json(creatives, 'reports/creatives.json')
    save_json({'query': query, 'steps': plan}, 'logs/trace.json')

    report = f"# Facebook Ads Report\n\nQuery: {query}\n\n"
    for hyp in validated['validated_hypotheses']:
        report += f"- {hyp['hypothesis']} (Confidence {hyp['confidence']})\n"
    for rec in creatives['recommendations']:
        report += f"\n- {rec['campaign_name']} → \"{rec['new_message']}\" ({rec['strategy']})"
    save_md(report, 'reports/report.md')
    print("✓ Outputs generated in reports/ and logs/")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python src/run.py 'your query here'")
        sys.exit(1)
    main(' '.join(sys.argv[1:]))
