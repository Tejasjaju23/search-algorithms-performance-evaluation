"""Uniform Cost Search."""

import heapq
import itertools
from src.evaluation.metrics import SearchResult, Timer


def ucs(problem):
    with Timer() as timer:
        counter = itertools.count()
        pq = [(0, next(counter), problem.start)]
        parent = {problem.start: None}
        best_cost = {problem.start: 0}
        expanded = 0
        generated = 1

        while pq:
            cost, _, current = heapq.heappop(pq)
            if cost != best_cost.get(current):
                continue

            expanded += 1
            if current == problem.goal:
                path = _reconstruct(parent, current)
                return SearchResult("UCS", True, path, cost,
                                    expanded, generated,
                                    execution_time=timer.elapsed)

            for nxt, step_cost in problem.neighbors(current):
                new_cost = cost + step_cost
                if new_cost < best_cost.get(nxt, float("inf")):
                    best_cost[nxt] = new_cost
                    parent[nxt] = current
                    heapq.heappush(pq, (new_cost, next(counter), nxt))
                    generated += 1

        return SearchResult("UCS", False, [], execution_time=timer.elapsed)


def _reconstruct(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]
