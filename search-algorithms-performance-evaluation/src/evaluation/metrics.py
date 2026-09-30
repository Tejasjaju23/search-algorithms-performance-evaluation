"""Common result structures for experiments."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import time


@dataclass
class SearchResult:
    algorithm: str
    found: bool
    path: List[Any] = field(default_factory=list)
    cost: float = float("inf")
    nodes_expanded: int = 0
    nodes_generated: int = 0
    iterations: int = 0
    backtracks: int = 0
    assignments: int = 0
    constraint_checks: int = 0
    restarts: int = 0
    initial_cost: Optional[float] = None
    final_cost: Optional[float] = None
    execution_time: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "algorithm": self.algorithm,
            "found": self.found,
            "path_length": len(self.path) if self.path else 0,
            "cost": self.cost,
            "nodes_expanded": self.nodes_expanded,
            "nodes_generated": self.nodes_generated,
            "iterations": self.iterations,
            "backtracks": self.backtracks,
            "assignments": self.assignments,
            "constraint_checks": self.constraint_checks,
            "restarts": self.restarts,
            "initial_cost": self.initial_cost,
            "final_cost": self.final_cost,
            "execution_time": self.execution_time,
        }


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
