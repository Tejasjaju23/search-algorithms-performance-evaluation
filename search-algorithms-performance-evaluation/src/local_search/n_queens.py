"""N-Queens state utilities."""


def conflicts(state):
    total = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            same_row = state[i] == state[j]
            same_diag = abs(state[i] - state[j]) == abs(i - j)
            if same_row or same_diag:
                total += 1
    return total


def neighbors(state):
    n = len(state)
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                candidate = state.copy()
                candidate[col] = row
                yield candidate
