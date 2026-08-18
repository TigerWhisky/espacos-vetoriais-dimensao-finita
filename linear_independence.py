"""
Verificação da independência linear
"""

from typing import List
import numpy as np

def is_linearly_independent(vectors: List[List[float]], tol: float = 1e-10) -> bool:
    """
    Verifica se um conjunto de vetores é linearmente independente.
    Usa o cálculo do rank da matriz cujas colunas (ou linhas) são os vetores.
    """
    if not vectors:
        return True

    mat = np.array(vectors, dtype=float)

    # Se há mais vetores do que a dimensão do espaço, são dependentes
    if mat.shape[0] > mat.shape[1]:
        return False

    rank = np.linalg.matrix_rank(mat, tol=tol)
    return rank == len(vectors)
