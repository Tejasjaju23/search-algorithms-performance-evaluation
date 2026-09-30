from src.problems.grid_problem import default_grid
from src.uninformed.bfs import bfs
from src.uninformed.dfs import dfs
from src.uninformed.ucs import ucs
from src.informed.astar import astar
from src.informed.greedy_best_first import greedy_best_first


def test_bfs_finds_solution():
    assert bfs(default_grid()).found


def test_dfs_finds_solution():
    assert dfs(default_grid()).found


def test_ucs_finds_solution():
    assert ucs(default_grid()).found


def test_greedy_finds_solution():
    assert greedy_best_first(default_grid()).found


def test_astar_finds_solution():
    assert astar(default_grid()).found


def test_astar_cost_matches_bfs_on_unit_grid():
    assert astar(default_grid()).cost == bfs(default_grid()).cost
