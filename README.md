# Experiment Analysis Lab

Python experimentation project for comparing variants, summarizing lift, and packaging analyst-friendly outputs.

## Why This Exists

Built to resemble the kind of A/B analysis tooling product analytics teams use when they want reproducible experiment summaries.

## What This Demonstrates

- variant comparison and compact KPI summaries
- repeatable analysis flow instead of notebook-only logic
- reviewable outputs that fit product experimentation work

## Architecture

1. raw experiment observations are loaded into a repeatable analysis path
1. metrics are grouped by variant and summarized into lift-style outputs
1. results are serialized for downstream reporting and decision support

## Run It

```bash
python -m unittest
```

## Verification

Run `python -m unittest` to confirm experiment calculations and reporting behavior.
