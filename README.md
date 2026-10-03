# Noise Pollution Analysis Agent

A portable OpenGAP-compatible agent for analyzing supplied environmental noise measurements.

## Tools

- `analyze-noise-level`: validates and summarizes sound-level measurements.
- `classify-noise-exposure`: classifies measurements using explicit configurable thresholds.
- `generate-noise-report`: produces a deterministic summary report.

## Validation

```bash
pytest -q
python3 verification/readiness_audit.py
opengap validate
```
