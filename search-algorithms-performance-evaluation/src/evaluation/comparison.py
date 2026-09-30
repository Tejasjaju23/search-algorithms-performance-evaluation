"""Generate summary tables and plots from benchmark results."""

import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_reports(csv_path="experiments/results/benchmark_results.csv",
                     output_dir="outputs/plots"):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(csv_path)

    summary = (
        df.groupby(["problem", "algorithm"], dropna=False)
        .agg(
            average_time=("execution_time", "mean"),
            average_nodes=("nodes_expanded", "mean"),
            average_cost=("cost", "mean"),
            success_rate=("found", "mean"),
        )
        .reset_index()
    )

    summary.to_csv("experiments/results/summary.csv", index=False)

    for problem, group in summary.groupby("problem"):
        safe_name = problem.lower().replace(" ", "_").replace("-", "_")
        plt.figure(figsize=(9, 5))
        plt.bar(group["algorithm"], group["average_time"])
        plt.ylabel("Average Execution Time (seconds)")
        plt.xlabel("Algorithm")
        plt.title(f"Execution Time - {problem}")
        plt.xticks(rotation=25, ha="right")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"{safe_name}_time.png"), dpi=160)
        plt.close()

    return summary
