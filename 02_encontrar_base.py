from src.basis import find_basis, dimension

vetores = [
    [1, 2, 3],
    [2, 4, 6],          # múltiplo do primeiro
    [1, 0, 1],
    [0, 1, 1],
]

base = find_basis(vetores)
print("Base encontrada:")
for v in base:
    print(" ", v)

print("Dimensão do subespaço:", dimension(vetores))
