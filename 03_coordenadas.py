from src.coordinates import coordinates_wrt_basis

base = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
vetor = [3, -2, 5]

coords = coordinates_wrt_basis(vetor, base)
print("Coordenadas de", vetor, "relativamente à base canónica:", coords)
