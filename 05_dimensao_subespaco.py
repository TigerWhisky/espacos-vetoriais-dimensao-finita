from src.basis import dimension

# Subespaço de R³ gerado por estes vetores
geradores = [
    [1, 2, 0],
    [2, 4, 0],
    [0, 0, 3],
    [1, 2, 3],
]

print("Dimensão do subespaço:", dimension(geradores))
