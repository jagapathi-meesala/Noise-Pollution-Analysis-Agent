import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(required=["measurements"], properties={"measurements": list})

def analyze(payload):
    CONTRACT.validate(payload)
    values = payload["measurements"]
    if not values or any(not isinstance(v, (int, float)) or isinstance(v, bool) for v in values):
        raise ValueError("measurements must be a non-empty list of numbers")
    return {"count": len(values), "minimum_db": min(values), "maximum_db": max(values), "average_db": sum(values) / len(values)}
