"""Run the full benchmark and generate charts."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.evaluation.benchmark import run_benchmark
from src.evaluation.comparison import generate_reports


if __name__ == "__main__":
    csv_path = run_benchmark()
    summary = generate_reports(csv_path)
    print(f"\nBenchmark complete: {csv_path}")
    print("\nSummary:")
    print(summary.to_string(index=False))
    print("\nPlots generated in outputs/plots/")
