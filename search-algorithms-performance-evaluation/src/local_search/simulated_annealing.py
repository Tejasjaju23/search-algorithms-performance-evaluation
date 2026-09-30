"""Simulated Annealing for N-Queens."""

import math
import random
from src.evaluation.metrics import SearchResult, Timer
from src.local_search.n_queens import conflicts


def simulated_annealing(n=8, max_iterations=10000, initial_temp=10.0,
                        cooling=0.995, seed=None):
    rng = random.Random(seed)
    with Timer() as timer:
        state = [rng.randrange(n) for _ in range(n)]
        current = conflicts(state)
        initial = current
        best = current
        temp = initial_temp

        for iteration in range(1, max_iterations + 1):
            if current == 0:
                return SearchResult(
                    "Simulated Annealing", True, [],
                    iterations=iteration,
                    initial_cost=initial,
                    final_cost=current,
                    execution_time=timer.elapsed,
                )

            col = rng.randrange(n)
            row = rng.randrange(n)
            candidate = state.copy()
            candidate[col] = row
            candidate_cost = conflicts(candidate)
            delta = candidate_cost - current

            if delta <= 0 or rng.random() < math.exp(-delta / max(temp, 1e-12)):
                state = candidate
                current = candidate_cost
                best = min(best, current)

            temp *= cooling

        return SearchResult(
            "Simulated Annealing", best == 0, [],
            iterations=max_iterations,
            initial_cost=initial,
            final_cost=best,
            execution_time=timer.elapsed,
        )
