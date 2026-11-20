# Contrôles numériques reproductibles pour l'examen du Bloc 1.
# Dépendances : R de base uniquement.
# Ce script vérifie des valeurs de référence ; il ne remplace pas les preuves.

check_close <- function(actual, expected, tolerance = 1e-10) {
  if (length(actual) != length(expected) ||
      any(abs(actual - expected) > tolerance * pmax(1, abs(expected)))) {
    stop(sprintf("Attendu %s ; obtenu %s",
                 paste(expected, collapse = ", "),
                 paste(actual, collapse = ", ")))
  }
  invisible(TRUE)
}

# A — Intervalles et précision
absolute_error_bound <- 0.4
relative_error_bound <- 0.4 / 99.6
check_close(absolute_error_bound, 0.4)
check_close(relative_error_bound, 0.004016064257028112)

# B — Ratios et coûts moyens
check_close(96 / 1600, 0.06)
check_close(96 / 2000, 0.048)
check_close((120 + 2.4 * 20) / 20, 8.4)
check_close((120 + 2.4 * 200) / 200, 3.0)

# C — Variations composées et indices
global_factor <- 1.08 * 0.95 * 1.03
check_close(global_factor, 1.05678)
check_close(250 * global_factor, 264.195)
check_close(global_factor^(1 / 3) - 1, 0.0185793370886167)
check_close(100 * 120 / 96, 125)

# D — Exponentielle et logarithme
years_threshold <- log(1.25) / log(1.032)
stopifnot(1.032^7 < 1.25, 1.25 <= 1.032^8)
check_close(log(1.032), 0.031498667059371016)
stopifnot(1.03^13 < 1.5, 1.5 <= 1.03^14)
stopifnot(1.025^10 < 1.30, 1.30 <= 1.025^11)

# E — Racine et système
candidates <- c(3, -1)
valid_roots <- candidates[candidates >= 0 &
                            abs(sqrt(2 * candidates + 3) - candidates) < 1e-10]
stopifnot(identical(valid_roots, 3))
a <- 7.4
b <- 4.2
check_close(2 * a + b, 19)
check_close(a - 2 * b, -1)

# F — Composition
composed_tariff <- function(x) 6 + 0.8 * (1.25 * x)
check_close(composed_tariff(20), 26)

# G — Cas portefeuille
frequency_1 <- 48 / 800
frequency_2 <- 65 / 1000
check_close(c(frequency_1, frequency_2), c(0.06, 0.065))
check_close(frequency_2 / frequency_1 - 1, 0.08333333333333348)

charge_1 <- 48 * 500
charge_2 <- 65 * 520
check_close(c(charge_1, charge_2), c(24000, 33800))
check_close(charge_2 / charge_1 - 1, 0.40833333333333344)

effect_count <- (65 - 48) * 500
effect_average_cost <- 65 * (520 - 500)
check_close(c(effect_count, effect_average_cost), c(8500, 1300))
check_close(effect_count + effect_average_cost, charge_2 - charge_1)
check_close(100 * charge_2 / charge_1, 140.83333333333334)

cat("OK — tous les contrôles numériques du Bloc 1 ont réussi.\n")
