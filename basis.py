"""
Calculo da base e dimmensão
"""

from typing import List, Tuple
import numpy as np
from .linear_independence import is_linearly_independent

def find_basis(vectors: List[List[float]], tol: float = 1e-10) -> List[List[float]]:
    """
    A partir de um conjunto de vetores, retornae uma base do subespaço gerado
    (saca um subconjunto linearmente independente maximal).
    """
    if not vectors:
        return []

    basis = []
    for v in vectors:
        candidate = basis + [v]
        if is_linearly_independent(candidate, tol=tol):
            basis.append(v)
    return basis

def dimension(vectors: List[List[float]], tol: float = 1e-10) -> int:
    """Retorna a dimensão do subespaço gerado pelos vetores."""
    return len(find_basis(vectors, tol=tol))
