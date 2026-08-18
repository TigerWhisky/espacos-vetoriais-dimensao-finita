from src.linear_independence import is_linearly_independent

def test_independent():
    assert is_linearly_independent([[1, 0], [0, 1]]) is True

def test_dependent():
    assert is_linearly_independent([[1, 2], [2, 4]]) is False

def test_empty():
    assert is_linearly_independent([]) is True
