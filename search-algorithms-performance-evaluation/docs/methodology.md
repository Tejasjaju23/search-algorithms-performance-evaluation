# Experimental Methodology

## 1. Benchmark Design

The project uses two representative problem classes:

- Grid pathfinding for graph-search algorithms.
- N-Queens for local-search and CSP algorithms.

## 2. Independent Variables

- Search algorithm
- Problem type
- Problem size
- Heuristic strategy
- Local-search parameters

## 3. Dependent Variables

- Execution time
- Nodes expanded
- Nodes generated
- Solution cost
- Iterations
- Assignments
- Backtracks
- Constraint checks
- Success rate

## 4. Repetition

Local-search methods are stochastic, so multiple runs are performed using different random seeds.

## 5. Reproducibility

The benchmark stores random seeds and saves generated measurements to CSV. This allows the experiment to be repeated.

## 6. Fair Comparison

Algorithms within the same problem family use the same input instance and termination conditions wherever applicable.
