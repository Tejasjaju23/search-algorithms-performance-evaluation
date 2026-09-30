# Project Report

## Title
Performance Evaluation of Search-Based Problem Solving Algorithms

## 1. Introduction
Artificial Intelligence problems can often be formulated as search problems. Different search strategies trade off completeness, optimality, memory usage, computational cost and solution quality.

## 2. Problem Statement
Evaluate the performance of various algorithms belonging to Uninformed Search, Informed Search, Local Search and Constraint Satisfaction.

## 3. Objectives
- Implement representative algorithms.
- Apply algorithms to suitable benchmark problems.
- Measure computational performance.
- Compare the resulting measurements.
- Analyze strengths and limitations.
- Identify suitable applications.

## 4. Algorithms
BFS, DFS, UCS, Greedy Best-First Search, A*, Hill Climbing, Simulated Annealing, Backtracking, Forward Checking and MRV.

## 5. Experimental Setup
Language: Python

Problems:
- Grid Pathfinding
- N-Queens

Metrics:
- Execution time
- Nodes expanded/generated
- Solution cost
- Iterations
- Assignments
- Backtracks
- Constraint checks
- Success rate

## 6. Results
Insert the generated tables and plots from `experiments/results/` and `outputs/plots/`.

## 7. Critical Analysis
Use the measured results to compare algorithm behavior. Discuss completeness, optimality, heuristic effectiveness, local minima, stochastic behavior, pruning and scalability.

## 8. Ethical Considerations
Search algorithms can influence automated decisions and resource allocation. Results must be reproducible and honestly reported. Applications involving people should consider fairness, transparency, privacy and the consequences of incorrect decisions.

## 9. Future Scope
Explore additional search algorithms, heuristics, CSP problems, larger datasets, visualization and parallel experimentation.

## 10. Conclusion
The experimental study demonstrates that there is no single search strategy that is optimal for every problem. Algorithm selection should be based on the structure of the problem, available information, solution requirements and computational constraints.
