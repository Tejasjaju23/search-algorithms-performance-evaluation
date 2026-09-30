"""Depth-First Search."""

from src.evaluation.metrics import SearchResult, Timer


def dfs(problem):
    with Timer() as timer:
        stack = [problem.start]
        parent = {problem.start: None}
        expanded = 0
        generated = 1

        while stack:
            current = stack.pop()
            expanded += 1

            if current == problem.goal:
                path = _reconstruct(parent, current)
                return SearchResult("DFS", True, path, len(path) - 1,
                                    expanded, generated,
                                    execution_time=timer.elapsed)

            neighbors = list(problem.neighbors(current))
            for nxt, _ in reversed(neighbors):
                if nxt not in parent:
                    parent[nxt] = current
                    stack.append(nxt)
                    generated += 1

        return SearchResult("DFS", False, [], execution_time=timer.elapsed)


def _reconstruct(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]
