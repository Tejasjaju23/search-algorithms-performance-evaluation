"""Grid pathfinding problem and utilities."""

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

Position = Tuple[int, int]


@dataclass
class GridProblem:
    grid: List[List[int]]
    start: Position
    goal: Position

    @property
    def rows(self) -> int:
        return len(self.grid)

    @property
    def cols(self) -> int:
        return len(self.grid[0])

    def neighbors(self, state: Position) -> Iterable[Tuple[Position, int]]:
        r, c = state
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                yield (nr, nc), 1

    def heuristic(self, state: Position) -> int:
        return abs(state[0] - self.goal[0]) + abs(state[1] - self.goal[1])

    def valid(self, state: Position) -> bool:
        r, c = state
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0


def default_grid() -> GridProblem:
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    ]
    return GridProblem(grid, (0, 0), (9, 9))
