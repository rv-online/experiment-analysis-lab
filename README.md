# Experiment Analysis Lab

Python analytics project for A/B test result summarization. It packages a small but reviewable workflow with deterministic scoring, JSON outputs, and unit tests.

## What It Shows

- product analytics, experimentation rigor, and decision support
- clear ingestion and summarization logic
- CLI entrypoint and test coverage

## Run

```bash
python -m src.analyzer --input data/experiments.ndjson --output out/report.json
```

## Test

```bash
python -m unittest discover -s tests
```
