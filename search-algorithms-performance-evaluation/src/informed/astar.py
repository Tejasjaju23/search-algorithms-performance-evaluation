"""A* Search."""

import heapq
import itertools
from src.evaluation.metrics import SearchResult, Timer


def astar(problem):
    with Timer() as timer:
        counter = itertools.count()
        start = problem.start
        pq = [(problem.heuristic(start), next(counter), start)]
        parent = {start: None}
        g_score = {start: 0}
        expanded = 0
        generated = 1

        while pq:
            _, _, current = heapq.heappop(pq)
            expanded += 1

            if current == problem.goal:
                path = _reconstruct(parent, current)
                return SearchResult("A*", True, path, g_score[current],
                                    expanded, generated,
                                    execution_time=timer.elapsed)

            for nxt, step_cost in problem.neighbors(current):
                tentative = g_score[current] + step_cost
                if tentative < g_score.get(nxt, float("inf")):
                    g_score[nxt] = tentative
                    parent[nxt] = current
                    f = tentative + problem.heuristic(nxt)
                    heapq.heappush(pq, (f, next(counter), nxt))
                    generated += 1

        return SearchResult("A*", False, [], execution_time=timer.elapsed)


def _reconstruct(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]
