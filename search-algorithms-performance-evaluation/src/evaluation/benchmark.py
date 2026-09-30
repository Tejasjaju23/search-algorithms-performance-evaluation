"""Benchmark runner for all algorithm families."""

import csv
import os
import statistics

from src.problems.grid_problem import default_grid
from src.uninformed.bfs import bfs
from src.uninformed.dfs import dfs
from src.uninformed.ucs import ucs
from src.informed.greedy_best_first import greedy_best_first
from src.informed.astar import astar
from src.local_search.hill_climbing import hill_climbing
from src.local_search.simulated_annealing import simulated_annealing
from src.csp.backtracking import backtracking
from src.csp.forward_checking import forward_checking
from src.csp.mrv import mrv


def run_benchmark(output_dir="experiments/results", local_runs=10):
    os.makedirs(output_dir, exist_ok=True)
    grid = default_grid()

    records = []

    path_algorithms = [bfs, dfs, ucs, greedy_best_first, astar]
    for algorithm in path_algorithms:
        result = algorithm(grid)
        row = result.to_dict()
        row["problem"] = "Grid Pathfinding"
        row["problem_size"] = f"{grid.rows}x{grid.cols}"
        records.append(row)

    for algorithm in [hill_climbing, simulated_annealing]:
        for run in range(local_runs):
            result = algorithm(n=8, seed=run)
            row = result.to_dict()
            row["problem"] = "N-Queens Local Search"
            row["problem_size"] = "8"
            row["run"] = run + 1
            records.append(row)

    for name, algorithm in [
        ("Backtracking", backtracking),
        ("Forward Checking", forward_checking),
        ("MRV + Forward Checking", mrv),
    ]:
        result = algorithm(8)
        row = result.to_dict()
        row["problem"] = "N-Queens CSP"
        row["problem_size"] = "8"
        records.append(row)

    path = os.path.join(output_dir, "benchmark_results.csv")
    fieldnames = sorted({key for record in records for key in record})
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    return path


if __name__ == "__main__":
    print(run_benchmark())
