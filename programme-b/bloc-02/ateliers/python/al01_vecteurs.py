"""Atelier AL01 — vecteurs dans R^n (bibliothèque standard uniquement)."""
from math import sqrt, acos, pi, isclose

def add(u, v):
    assert len(u) == len(v), "Dimensions incompatibles"
    return tuple(a + b for a, b in zip(u, v))

def scale(alpha, u):
    return tuple(alpha * a for a in u)

def dot(u, v):
    assert len(u) == len(v), "Dimensions incompatibles"
    return sum(a * b for a, b in zip(u, v))

def norm(u):
    return sqrt(dot(u, u))

def distance(u, v):
    return norm(add(u, scale(-1, v)))

def angle(u, v):
    nu, nv = norm(u), norm(v)
    if isclose(nu, 0.0) or isclose(nv, 0.0):
        raise ValueError("L'angle n'est pas défini pour un vecteur nul")
    c = max(-1.0, min(1.0, dot(u, v) / (nu * nv)))
    return acos(c)

if __name__ == "__main__":
    u, v = (1, 2, 2), (4, 6, 2)
    assert add((1, 2), (3, 4)) == (4, 6)
    assert isclose(norm((3, 4)), 5.0)
    assert isclose(distance(u, v), 5.0)
    assert dot((2, 1, -1), (1, -1, 1)) == 0
    assert isclose(angle((1, 0), (1, sqrt(3))), pi / 3)
    try:
        dot((1, 2), (1,))
    except AssertionError:
        pass
    else:
        raise AssertionError("Le contrôle de dimension aurait dû échouer")
    print("AL01 — tous les tests sont réussis.")
