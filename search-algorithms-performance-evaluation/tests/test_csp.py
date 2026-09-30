from src.csp.backtracking import backtracking
from src.csp.forward_checking import forward_checking
from src.csp.mrv import mrv


def test_backtracking():
    assert backtracking(8).found


def test_forward_checking():
    assert forward_checking(8).found


def test_mrv():
    assert mrv(8).found
