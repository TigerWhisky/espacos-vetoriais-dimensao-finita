from src.change_of_basis import change_of_basis_matrix
from src.coordinates import coordinates_wrt_basis
import numpy as np

# Base B (canónica)
B = [[1, 0], [0, 1]]

# Base C
C = [[2, 1], [1, 1]]

P = change_of_basis_matrix(B, C)   # de B para C
print("Matriz de mudança de base (B → C):")
print(np.array(P))

# Exemplo de conversão de coordenadas
x = [3, 4]
coords_B = coordinates_wrt_basis(x, B)
coords_C = np.array(P) @ np.array(coords_B)
print("\nCoordenadas de", x, "em B:", coords_B)
print("Coordenadas de", x, "em C:", coords_C.tolist())
