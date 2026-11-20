# Atelier R — Bloc 1 : fondations mathématiques
# Exécuter : Rscript fondations.R

ratio <- function(numerator, denominator) {
  if (denominator == 0) stop("Le dénominateur doit être non nul.")
  numerator / denominator
}

relative_change <- function(initial, final) {
  if (initial == 0) stop("Le taux relatif n'est pas défini si l'initial vaut zéro.")
  final / initial - 1
}

chained_change <- function(...) {
  rates <- c(...)
  if (any(rates <= -1)) stop("Taux inférieur ou égal à -100 %.")
  prod(1 + rates) - 1
}

weighted_allocation <- function(total, weights) {
  if (length(weights) == 0 || any(weights < 0) || sum(weights) <= 0) {
    stop("Les poids doivent être non négatifs et leur somme positive.")
  }
  total * weights / sum(weights)
}

# F01 — représentation exacte rationnelle via fractions en double entrée
# R base ne possède pas de type rationnel exact natif.
stopifnot(isTRUE(all.equal(1/3 + 1/6, 1/2)))
stopifnot(strtoi("11010", base = 2) == 26L)

# F02 — rapports et partage pondéré
stopifnot(isTRUE(all.equal(weighted_allocation(900, c(1, 2, 3)), c(150, 300, 450))))

# F03 — variations
stopifnot(isTRUE(all.equal(relative_change(80, 100), 0.25)))
stopifnot(isTRUE(all.equal(chained_change(0.10, -0.10), -0.01)))

# F04 — puissances, racines et logarithmes
stopifnot(isTRUE(all.equal(exp(log(7)), 7)))
stopifnot(sqrt(81) == 9)

# F05/F06 — factorisation et racines
stopifnot(identical(polyroot(c(6, -5, 1)), c(2+0i, 3+0i)))

# F07/F08 — fonction, pente et notation scientifique
f <- function(x) 3*x - 2
stopifnot(f(5) == 13)
stopifnot((13 - 5) / (6 - 2) == 2)
print(format(0.00000456, scientific = TRUE))

cat("Tous les contrôles de l'atelier R sont réussis.\n")
cat("Variation composée (+10 %, -10 %) :",
    sprintf("%.2f %%", 100 * chained_change(0.10, -0.10)), "\n")
