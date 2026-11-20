"""Atelier Python — Bloc 1 : fondations mathématiques.
Bibliothèque standard uniquement. Exécuter : python fondations.py
"""
from fractions import Fraction
from math import isclose, log, exp, sqrt, isfinite


def ratio(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("Le dénominateur doit être non nul.")
    return numerator / denominator


def relative_change(initial: float, final: float) -> float:
    if initial == 0:
        raise ValueError("Le taux relatif n'est pas défini si la valeur initiale est nulle.")
    return final / initial - 1


def chained_change(*rates: float) -> float:
    """Taux global à partir de taux décimaux signés : 0.05 = +5 %."""
    coefficient = 1.0
    for rate in rates:
        if rate <= -1:
            raise ValueError("Un taux inférieur ou égal à -100 % n'est pas admissible ici.")
        coefficient *= 1 + rate
    return coefficient - 1


def weighted_allocation(total: float, weights: list[float]) -> list[float]:
    if not weights or any(w < 0 for w in weights) or sum(weights) <= 0:
        raise ValueError("Les poids doivent être non négatifs et leur somme positive.")
    return [total * w / sum(weights) for w in weights]


def quadratic_roots(a: float, b: float, c: float):
    if a == 0:
        raise ValueError("Ce calcul exige une équation du second degré : a doit être non nul.")
    delta = b * b - 4 * a * c
    if delta < 0:
        return ()
    if isclose(delta, 0.0, abs_tol=1e-12):
        return (-b / (2 * a),)
    root_delta = sqrt(delta)
    return ((-b - root_delta) / (2 * a), (-b + root_delta) / (2 * a))


def scientific_notation(x: float) -> tuple[float, int]:
    if not isfinite(x):
        raise ValueError("Le nombre doit être fini.")
    if x == 0:
        return 0.0, 0
    exponent = 0
    mantissa = abs(x)
    while mantissa >= 10:
        mantissa /= 10
        exponent += 1
    while mantissa < 1:
        mantissa *= 10
        exponent -= 1
    return (mantissa if x > 0 else -mantissa), exponent


def main():
    # F01 — exactitude, bases et flottants
    assert Fraction(1, 3) + Fraction(1, 6) == Fraction(1, 2)
    assert int("11010", 2) == 26
    assert isclose(0.1 + 0.2, 0.3, rel_tol=0, abs_tol=1e-12)

    # F02 — fractions et proportions
    assert Fraction(42, 56) == Fraction(3, 4)
    assert weighted_allocation(900, [1, 2, 3]) == [150, 300, 450]

    # F03 — taux et composition
    assert isclose(relative_change(80, 100), 0.25)
    assert isclose(chained_change(0.10, -0.10), -0.01)

    # F04 — puissances, racines et logarithmes
    assert isclose(exp(log(7)), 7)
    assert sqrt(81) == 9

    # F05/F06 — algèbre et résolution
    roots = quadratic_roots(1, -5, 6)
    assert roots == (2.0, 3.0)
    assert isclose(3 * 6 - 7, 11)

    # F07/F08 — fonction affine, pente, notation scientifique
    f = lambda x: 3 * x - 2
    assert f(5) == 13
    slope = (13 - 5) / (6 - 2)
    assert slope == 2
    mantissa, exponent = scientific_notation(0.00000456)
    assert isclose(mantissa, 4.56) and exponent == -6

    print("Tous les contrôles de l'atelier Python sont réussis.")
    print("Variation composée (+10 %, -10 %) :", f"{100 * chained_change(0.10, -0.10):.2f} %")
    print("Racines de x² - 5x + 6 :", roots)
    print("Notation scientifique de 0.00000456 :", f"{mantissa} × 10^{exponent}")


if __name__ == "__main__":
    main()
