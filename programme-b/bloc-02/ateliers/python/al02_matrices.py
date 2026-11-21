"""Atelier AL02 — opérations matricielles et élimination de Gauss."""
from math import isclose

def matmul(A, B):
    if not A or not B or len(A[0]) != len(B):
        raise ValueError("Dimensions incompatibles ou matrice vide")
    if any(len(row) != len(A[0]) for row in A) or any(len(row) != len(B[0]) for row in B):
        raise ValueError("Matrice non rectangulaire")
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def gauss_solve(A, b, tol=1e-12):
    """Résout un système carré A x = b avec pivot partiel.
    Retourne une solution unique ; signale singularité/incompatibilité.
    """
    n = len(A)
    if n == 0 or len(b) != n or any(len(row) != n for row in A):
        raise ValueError("A doit être carrée et compatible avec b")
    M = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda i: abs(M[i][col]))
        if abs(M[pivot][col]) <= tol:
            raise ValueError("Matrice singulière ou système non unique")
        M[col], M[pivot] = M[pivot], M[col]
        for row in range(col + 1, n):
            factor = M[row][col] / M[col][col]
            for j in range(col, n + 1):
                M[row][j] -= factor * M[col][j]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x

if __name__ == "__main__":
    A = [[2, 1], [1, -1]]
    B = [[1, 0], [0, 1]]
    assert matmul(A, B) == A
    x = gauss_solve(A, [5, 1])
    assert isclose(x[0], 2.0) and isclose(x[1], 1.0)
    try:
        matmul([[1, 2]], [[1, 2]])
    except ValueError:
        pass
    else:
        raise AssertionError("Contrôle de dimensions non déclenché")
    print("AL02 — tests de base réussis.")
