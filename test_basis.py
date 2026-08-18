from src.basis import find_basis, dimension

def test_find_basis():
    vecs = [[1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1]]
    base = find_basis(vecs)
    assert len(base) == 3

def test_dimension():
    assert dimension([[1, 0], [0, 1], [1, 1]]) == 2
