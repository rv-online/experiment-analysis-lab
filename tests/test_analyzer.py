import json
import unittest
from pathlib import Path

from src.analyzer import build_report, run


class AnalyzerTests(unittest.TestCase):
    def test_build_report_counts_records(self) -> None:
        report = build_report([
            {"experiment_id": "exp_home", "variant": "control", "users": 1200, "conversion_rate": 0.084},
            {"experiment_id": "exp_home", "variant": "new-copy", "users": 1180, "conversion_rate": 0.101},
        ])
        self.assertEqual(report["record_count"], 2)

    def test_run_writes_output(self) -> None:
        output_path = Path("out/test-report.json")
        report = run(Path("data/experiments.ndjson"), output_path)
        on_disk = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(report["record_count"], 4)
        self.assertIn("winning_variants", on_disk)


if __name__ == "__main__":
    unittest.main()
