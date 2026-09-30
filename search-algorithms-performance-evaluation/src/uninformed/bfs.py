"""Breadth-First Search."""

from collections import deque
from src.evaluation.metrics import SearchResult, Timer


def bfs(problem):
    with Timer() as timer:
        queue = deque([problem.start])
        parent = {problem.start: None}
        nodes_generated = 1
        expanded = 0

        while queue:
            current = queue.popleft()
            expanded += 1

            if current == problem.goal:
                path = _reconstruct(parent, current)
                return SearchResult("BFS", True, path, len(path) - 1,
                                    expanded, nodes_generated,
                                    execution_time=timer.elapsed)

            for nxt, _ in problem.neighbors(current):
                if nxt not in parent:
                    parent[nxt] = current
                    queue.append(nxt)
                    nodes_generated += 1

        return SearchResult("BFS", False, [], execution_time=timer.elapsed)


def _reconstruct(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]
