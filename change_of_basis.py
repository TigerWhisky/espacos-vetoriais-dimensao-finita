"""
Matriz de mudança de base
"""

from typing import List
import numpy as np
from .coordinates import coordinates_wrt_basis

def change_of_basis_matrix(basis_from: List[List[float]], basis_to: List[List[float]]) -> List[List[float]]:
    """
    Devolve a matriz de mudança de base P tal que:
    [x]_to = P @ [x]_from

    As colunas de P são as coordenadas dos vectores de basis_from
    escritas na base basis_to.
    """
    if len(basis_from) != len(basis_to):
        raise ValueError("As duas bases devem ter o mesmo número de vectores")

    P_cols = []
    for v in basis_from:
        coords = coordinates_wrt_basis(v, basis_to)
        P_cols.append(coords)

    # P tem as coordenadas como colunas
    P = np.array(P_cols, dtype=float).T
    return P.tolist()
