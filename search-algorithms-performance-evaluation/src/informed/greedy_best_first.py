"""Greedy Best-First Search."""

import heapq
import itertools
from src.evaluation.metrics import SearchResult, Timer


def greedy_best_first(problem):
    with Timer() as timer:
        counter = itertools.count()
        pq = [(problem.heuristic(problem.start), next(counter), problem.start)]
        parent = {problem.start: None}
        visited = set()
        expanded = 0
        generated = 1

        while pq:
            _, _, current = heapq.heappop(pq)
            if current in visited:
                continue
            visited.add(current)
            expanded += 1

            if current == problem.goal:
                path = _reconstruct(parent, current)
                return SearchResult("Greedy Best-First", True, path,
                                    len(path) - 1, expanded, generated,
                                    execution_time=timer.elapsed)

            for nxt, _ in problem.neighbors(current):
                if nxt not in visited:
                    parent.setdefault(nxt, current)
                    heapq.heappush(pq, (problem.heuristic(nxt), next(counter), nxt))
                    generated += 1

        return SearchResult("Greedy Best-First", False, [], execution_time=timer.elapsed)


def _reconstruct(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]
