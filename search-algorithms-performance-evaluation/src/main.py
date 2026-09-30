"""Interactive entry point."""

from src.problems.grid_problem import default_grid
from src.uninformed.bfs import bfs
from src.uninformed.dfs import dfs
from src.uninformed.ucs import ucs
from src.informed.greedy_best_first import greedy_best_first
from src.informed.astar import astar
from src.local_search.hill_climbing import hill_climbing
from src.local_search.simulated_annealing import simulated_annealing
from src.csp.backtracking import backtracking
from src.csp.forward_checking import forward_checking
from src.csp.mrv import mrv


def show_result(result):
    print(f"\nAlgorithm: {result.algorithm}")
    print(f"Solution Found: {result.found}")
    print(f"Execution Time: {result.execution_time:.6f} sec")
    print(f"Nodes Expanded: {result.nodes_expanded}")
    print(f"Nodes Generated: {result.nodes_generated}")
    print(f"Path Length: {len(result.path) if result.path else 0}")
    print(f"Cost: {result.cost}")
    print(f"Iterations: {result.iterations}")
    print(f"Assignments: {result.assignments}")
    print(f"Backtracks: {result.backtracks}")
    print(f"Constraint Checks: {result.constraint_checks}")
    print(f"Final Cost: {result.final_cost}")


def main():
    grid = default_grid()

    while True:
        print("\n" + "=" * 55)
        print(" SEARCH ALGORITHM PERFORMANCE EVALUATION")
        print("=" * 55)
        print("1. Run Uninformed Search")
        print("2. Run Informed Search")
        print("3. Run Local Search")
        print("4. Run CSP")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            for algorithm in [bfs, dfs, ucs]:
                show_result(algorithm(grid))
        elif choice == "2":
            for algorithm in [greedy_best_first, astar]:
                show_result(algorithm(grid))
        elif choice == "3":
            show_result(hill_climbing(n=8, seed=42))
            show_result(simulated_annealing(n=8, seed=42))
        elif choice == "4":
            for algorithm in [backtracking, forward_checking, mrv]:
                show_result(algorithm(8))
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
