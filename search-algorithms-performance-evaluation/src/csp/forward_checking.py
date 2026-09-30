from src.csp.n_queens_csp import solve_csp

def forward_checking(n=8):
    return solve_csp(n, "forward_checking")
