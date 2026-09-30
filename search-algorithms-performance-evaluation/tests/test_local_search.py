from src.local_search.hill_climbing import hill_climbing
from src.local_search.simulated_annealing import simulated_annealing


def test_hill_climbing_runs():
    result = hill_climbing(n=8, seed=1)
    assert result.execution_time >= 0


def test_simulated_annealing_runs():
    result = simulated_annealing(n=8, seed=1)
    assert result.execution_time >= 0
