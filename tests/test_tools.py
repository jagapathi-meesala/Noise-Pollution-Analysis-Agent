import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    p = ROOT / "tools" / f"{name}.py"; s = importlib.util.spec_from_file_location(name.replace('-','_'), p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_analysis():
    m=load("analyze-noise-level"); r=m.analyze({"measurements":[50,60,70]}); assert r["count"]==3 and r["average_db"]==60

def test_classification():
    m=load("classify-noise-exposure"); assert m.classify({"db":72})["classification"]=="high"

def test_report():
    m=load("generate-noise-report"); r=m.report({"location":"Zone A","analysis":{"count":2,"average_db":65,"minimum_db":60,"maximum_db":70},"classification":"moderate"}); assert "Zone A" in r["summary"] or r["location"]=="Zone A"

def test_reject_unexpected():
    m=load("classify-noise-exposure")
    try: m.classify({"db":50,"x":1}); assert False
    except ValueError: pass
