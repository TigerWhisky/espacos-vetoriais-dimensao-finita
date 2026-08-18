"""
Cálculo das coordenadas relativamente a uma base
"""

from typing import List
import numpy as np

def coordinates_wrt_basis(vector: List[float], basis: List[List[float]]) -> List[float]:
    """
    Calcula as coordenadas do vector relativamente à base dada.
    Resolve o sistema Bc = v, onde as colunas de B são os vectores da base.
    """
    if not basis:
        raise ValueError("A base não pode ser vazia")

    B = np.array(basis, dtype=float).T   # colunas = vectores da base
    v = np.array(vector, dtype=float)

    if B.shape[0] != v.shape[0]:
        raise ValueError("Dimensão do vector incompatível com a base")

    try:
        coords = np.linalg.solve(B, v)
    except np.linalg.LinAlgError:
        # Base pode não ser ortogonal / mal condicionada → usar least squares
        coords, _, _, _ = np.linalg.lstsq(B, v, rcond=None)

    return coords.tolist()
