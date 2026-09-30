"""N-Queens CSP solvers: Backtracking, Forward Checking and MRV."""

from src.evaluation.metrics import SearchResult, Timer


def solve_csp(n=8, mode="backtracking"):
    with Timer() as timer:
        domains = {c: set(range(n)) for c in range(n)}
        assignment = {}
        stats = {"assignments": 0, "backtracks": 0, "checks": 0}

        use_fc = mode in ("forward_checking", "mrv")
        use_mrv = mode == "mrv"

        solution = _search(
            n, domains, assignment, stats,
            use_fc=use_fc, use_mrv=use_mrv
        )

        names = {
            "backtracking": "Backtracking",
            "forward_checking": "Forward Checking",
            "mrv": "MRV + Forward Checking",
        }

        return SearchResult(
            names[mode],
            solution is not None,
            assignments=stats["assignments"],
            backtracks=stats["backtracks"],
            constraint_checks=stats["checks"],
            execution_time=timer.elapsed,
        )


def _consistent(var, value, assignment, stats):
    for other, other_value in assignment.items():
        stats["checks"] += 1
        if value == other_value or abs(value - other_value) == abs(var - other):
            return False
    return True


def _select_variable(domains, assignment, use_mrv):
    unassigned = [v for v in domains if v not in assignment]
    if use_mrv:
        return min(unassigned, key=lambda v: len(domains[v]))
    return min(unassigned)


def _search(n, domains, assignment, stats, use_fc, use_mrv):
    if len(assignment) == n:
        return assignment.copy()

    var = _select_variable(domains, assignment, use_mrv)

    for value in sorted(domains[var]):
        if not _consistent(var, value, assignment, stats):
            continue

        stats["assignments"] += 1
        assignment[var] = value

        new_domains = {v: set(vals) for v, vals in domains.items()}
        new_domains[var] = {value}

        feasible = True
        if use_fc:
            for other in new_domains:
                if other == var or other in assignment:
                    continue
                filtered = {
                    x for x in new_domains[other]
                    if _consistent(other, x, assignment, stats)
                }
                new_domains[other] = filtered
                if not filtered:
                    feasible = False
                    break

        if feasible:
            result = _search(n, new_domains, assignment, stats, use_fc, use_mrv)
            if result is not None:
                return result

        del assignment[var]
        stats["backtracks"] += 1

    return None
