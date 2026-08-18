from src.coordinates import coordinates_wrt_basis

def test_coordinates_canonical():
    base = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    coords = coordinates_wrt_basis([4, 5, 6], base)
    assert coords == [4.0, 5.0, 6.0]
