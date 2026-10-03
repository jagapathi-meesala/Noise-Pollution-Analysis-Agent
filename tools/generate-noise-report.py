import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(required=["location", "analysis", "classification"], properties={"location": str, "analysis": dict, "classification": str})

def report(payload):
    CONTRACT.validate(payload)
    a = payload["analysis"]
    return {"location": payload["location"], "summary": f"{a['count']} measurements; average {a['average_db']:.2f} dB; range {a['minimum_db']:.2f}-{a['maximum_db']:.2f} dB", "classification": payload["classification"]}
