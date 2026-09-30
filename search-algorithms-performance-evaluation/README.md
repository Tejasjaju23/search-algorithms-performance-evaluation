# Search Algorithms Performance Evaluation

## Problem Statement

> Evaluate the performance of various algorithms (Uninformed, Informed, Local Search and Constraint Satisfaction) for problem solving through Search.

## Objective

This project implements and experimentally evaluates representative AI search techniques:

- **Uninformed Search:** BFS, DFS, Uniform Cost Search
- **Informed Search:** Greedy Best-First Search, A*
- **Local Search:** Hill Climbing, Simulated Annealing
- **Constraint Satisfaction:** Backtracking, Forward Checking, MRV

The project measures execution time, nodes expanded/generated, solution cost, iterations, backtracks, assignments and success rate.

## Problems Used

1. **Grid Pathfinding** for BFS, DFS, UCS, Greedy Best-First Search and A*.
2. **N-Queens** for Hill Climbing, Simulated Annealing and CSP algorithms.

## Repository Structure

```text
search-algorithms-performance-evaluation/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── src/
│   ├── main.py
│   ├── uninformed/
│   ├── informed/
│   ├── local_search/
│   ├── csp/
│   ├── problems/
│   └── evaluation/
├── experiments/
│   ├── run_experiments.py
│   ├── datasets/
│   └── results/
├── outputs/
│   ├── tables/
│   └── plots/
├── tests/
└── docs/
```

## Installation

```bash
git clone <your-repository-url>
cd search-algorithms-performance-evaluation
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Interactive Demo

```bash
python src/main.py
```

## Run Complete Benchmark

```bash
python experiments/run_experiments.py
```

The benchmark creates CSV files in `experiments/results/` and charts in `outputs/plots/`.

## Evaluation Metrics

### Pathfinding

- Execution time
- Nodes expanded
- Nodes generated
- Path length
- Path cost
- Success/failure

### Local Search

- Execution time
- Iterations
- Initial conflicts
- Final conflicts
- Success rate
- Restarts

### CSP

- Execution time
- Assignments
- Backtracks
- Constraint checks
- Solution status

## Experimental Methodology

Each algorithm is tested on increasing problem sizes. Stochastic local-search algorithms are executed multiple times and their success rates are reported.

The project does not hard-code performance claims. Results are generated from actual runs and saved as CSV files.

## Algorithm Summary

| Category | Algorithm | Main Idea |
|---|---|---|
| Uninformed | BFS | Expands shallowest states first |
| Uninformed | DFS | Expands deepest state first |
| Uninformed | UCS | Expands lowest path-cost state |
| Informed | Greedy | Uses heuristic estimate |
| Informed | A* | Uses `f(n)=g(n)+h(n)` |
| Local | Hill Climbing | Moves to a better neighboring state |
| Local | Simulated Annealing | Occasionally accepts worse states |
| CSP | Backtracking | Assigns variables recursively |
| CSP | Forward Checking | Prunes inconsistent domains |
| CSP | MRV | Selects variable with minimum remaining values |

## Critical Analysis

The generated results should be used to compare:

- Search efficiency
- Solution quality
- Scalability
- Effect of heuristic information
- Local-search success rates
- CSP search-space reduction

Do not report fabricated measurements. Run the benchmark and use the generated CSV files and graphs as experimental evidence.

## Ethical and Societal Considerations

Search algorithms are used in route planning, scheduling, robotics, games and automated decision systems. Incorrect algorithm selection can increase computational cost or produce undesirable solutions. Experimental results should be reported honestly and reproducibly. Applications affecting people should additionally consider fairness, transparency, privacy and the consequences of incorrect decisions.

## Future Scope

- Bidirectional Search
- Iterative Deepening DFS
- More heuristic functions
- Weighted graphs
- Sudoku CSP
- Genetic Algorithms
- Interactive visualization
- Memory-consumption benchmarking
- Parallel benchmark execution

## Learning Outcomes

After completing this project, the learner should be able to:

1. Classify AI search algorithms.
2. Implement search algorithms using modular code.
3. Select suitable algorithms for different problem types.
4. Measure algorithmic performance experimentally.
5. Interpret quantitative results.
6. Compare completeness, optimality and efficiency.
7. Explain the effect of heuristics and CSP heuristics.
