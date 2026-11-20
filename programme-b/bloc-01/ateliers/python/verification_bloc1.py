"""Contrôles numériques reproductibles pour l'examen du Bloc 1.

Usage:
    python verification_bloc1.py

Dépendances: bibliothèque standard uniquement.
Ce script vérifie des résultats de référence ; il ne corrige pas une copie
et ne remplace pas la justification mathématique.
"""
from math import isclose, log

def close(actual, expected, *, rel_tol=1e-10, abs_tol=1e-12):
    assert isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol), (
        f"Attendu {expected}, obtenu {actual}"
    )

# A — Intervalle admissible et précision
candidate_values = (79.9, 80, 100, 120, 120.1)
admissible = [x for x in candidate_values
              if 0 <= x <= 200 and x > 40 and abs(x - 100) <= 20]
assert admissible == [80, 100, 120]
absolute_error_bound = 0.4
relative_error_bound = 0.4 / 99.6
close(absolute_error_bound, 0.4)
close(relative_error_bound, 0.004016064257028112)

# B — Ratios, unités et coût moyen
close(96 / 1600, 0.06)
close(96 / 2000, 0.048)
close((120 + 2.4 * 20) / 20, 8.4)
close((120 + 2.4 * 200) / 200, 3.0)

# C — Variations composées et moyenne géométrique
global_factor = 1.08 * 0.95 * 1.03
close(global_factor, 1.05678)
close(250 * global_factor, 264.195)
close(global_factor ** (1 / 3) - 1, 0.0185793370886167)
close(100 * 120 / 96, 125.0)

# D — Croissance exponentielle et logarithme
years_threshold = log(1.25) / log(1.032)
assert 1.032 ** 7 < 1.25 <= 1.032 ** 8
assert int(years_threshold) == 7  # partie entière du seuil réel
close(log(1.032), 0.031498667059371016)
assert 1.03 ** 13 < 1.5 <= 1.03 ** 14
assert 1.025 ** 10 < 1.30 <= 1.025 ** 11

# E — Équation avec racine et système
root_candidates = (3, -1)
valid_roots = [x for x in root_candidates
               if x >= 0 and isclose((2*x + 3) ** 0.5, x)]
assert valid_roots == [3]
a, b = 7.4, 4.2
close(2*a + b, 19)
close(a - 2*b, -1)

# F — Composition de fonctions
def composed_tariff(x):
    return 6 + 0.8 * (1.25 * x)

close(composed_tariff(20), 26)
close(26 - 6, 20)

# G — Cas portefeuille
frequency_1 = 48 / 800
frequency_2 = 65 / 1000
close(frequency_1, 0.06)
close(frequency_2, 0.065)
close(frequency_2 / frequency_1 - 1, 0.08333333333333348)

charge_1 = 48 * 500
charge_2 = 65 * 520
close(charge_1, 24000)
close(charge_2, 33800)
close(charge_2 / charge_1 - 1, 0.40833333333333344)

effect_count = (65 - 48) * 500
effect_average_cost = 65 * (520 - 500)
close(effect_count, 8500)
close(effect_average_cost, 1300)
close(effect_count + effect_average_cost, charge_2 - charge_1)
close(100 * charge_2 / charge_1, 140.83333333333334)

print("OK — tous les contrôles numériques du Bloc 1 ont réussi.")
