"""Hill Climbing for N-Queens."""

import random
from src.evaluation.metrics import SearchResult, Timer
from src.local_search.n_queens import conflicts, neighbors


def hill_climbing(n=8, max_restarts=30, max_iterations=500, seed=None):
    rng = random.Random(seed)
    with Timer() as timer:
        total_iterations = 0

        for restart in range(max_restarts + 1):
            state = [rng.randrange(n) for _ in range(n)]
            current = conflicts(state)

            for iteration in range(max_iterations):
                total_iterations += 1
                if current == 0:
                    return SearchResult(
                        "Hill Climbing", True, [],
                        iterations=total_iterations,
                        restarts=restart,
                        initial_cost=None,
                        final_cost=current,
                        execution_time=timer.elapsed,
                    )

                best_cost = current
                best_state = state

                for candidate in neighbors(state):
                    score = conflicts(candidate)
                    if score < best_cost:
                        best_cost = score
                        best_state = candidate

                if best_cost >= current:
                    break

                state, current = best_state, best_cost

        return SearchResult(
            "Hill Climbing", False, [],
            iterations=total_iterations,
            restarts=max_restarts,
            final_cost=current,
            execution_time=timer.elapsed,
        )
