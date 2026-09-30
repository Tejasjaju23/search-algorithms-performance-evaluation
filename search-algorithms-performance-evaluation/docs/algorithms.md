# Algorithms

## Uninformed Search

### BFS
Uses a FIFO queue and expands the shallowest states first.

### DFS
Uses a stack and explores one branch deeply before backtracking.

### Uniform Cost Search
Expands the state with the smallest accumulated path cost.

## Informed Search

### Greedy Best-First Search
Uses only the heuristic estimate `h(n)`.

### A*
Uses:

`f(n) = g(n) + h(n)`

For the grid problem, Manhattan distance is used as the heuristic.

## Local Search

### Hill Climbing
Repeatedly moves to a neighboring state with a lower conflict count.

### Simulated Annealing
Allows occasional uphill moves according to a temperature-controlled probability.

## Constraint Satisfaction

### Backtracking
Assigns variables recursively and backtracks when a constraint is violated.

### Forward Checking
After an assignment, removes values that can no longer satisfy constraints.

### MRV
Selects the unassigned variable with the smallest remaining domain. In this project MRV is combined with forward checking.
