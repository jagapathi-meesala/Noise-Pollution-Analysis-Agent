import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(required=["db"], properties={"db": (int, float)})

def classify(payload):
    CONTRACT.validate(payload)
    db = payload["db"]
    if isinstance(db, bool) or db < 0:
        raise ValueError("db must be a non-negative number")
    if db < 55: label = "low"
    elif db < 70: label = "moderate"
    elif db < 85: label = "high"
    else: label = "very-high"
    return {"db": db, "classification": label}
