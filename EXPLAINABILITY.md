# Explainability

## Inputs and Data Sources

The agent accepts only user- or system-supplied sound-level measurements in decibels (dB). It does not collect external sensor data.

## Decision and Reasoning

Classification uses explicit thresholds supplied to the tool or its documented defaults. Analysis reports minimum, maximum, average, and count from the supplied measurements.

## Limits and Constraints

The agent does not diagnose health effects, determine legal compliance, infer missing measurements, or access live monitoring systems. Threshold-based labels are analytical categories, not medical or legal conclusions.

## Tool Behavior

Each tool validates required fields and rejects unexpected fields. Failures return explicit validation errors rather than fabricated results.
