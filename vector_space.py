"""
Utilitários para espaços vectoriais
"""

from typing import List
import numpy as np

def is_in_span(vector: List[float], generators: List[List[float]], tol: float = 1e-10) -> bool:
    """Verifica se um vector pertence ao range de um conjunto de geradores."""
    if not generators:
        return np.allclose(vector, 0, atol=tol)

    A = np.array(generators, dtype=float).T
    v = np.array(vector, dtype=float)

    # Resolve Ac = v em least squares e verifica residual
    coords, residuals, _, _ = np.linalg.lstsq(A, v, rcond=None)
    if residuals.size == 0:
        residual = np.linalg.norm(A @ coords - v)
    else:
        residual = np.sqrt(residuals[0])

    return residual < tol
