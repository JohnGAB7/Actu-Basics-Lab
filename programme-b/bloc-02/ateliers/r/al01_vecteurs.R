# Atelier AL01 — vecteurs dans R^n
# Implémentation en R de base, sans package externe.

addition <- function(u, v) {
  stopifnot(length(u) == length(v))
  u + v
}

produit_scalaire <- function(u, v) {
  stopifnot(length(u) == length(v))
  sum(u * v)
}

norme <- function(u) {
  sqrt(produit_scalaire(u, u))
}

distance <- function(u, v) {
  norme(u - v)
}

angle <- function(u, v) {
  nu <- norme(u); nv <- norme(v)
  if (nu == 0 || nv == 0) stop("Angle non défini pour un vecteur nul")
  cos_theta <- produit_scalaire(u, v) / (nu * nv)
  cos_theta <- max(-1, min(1, cos_theta))
  acos(cos_theta)
}

stopifnot(all.equal(addition(c(1, 2), c(3, 4)), c(4, 6)))
stopifnot(isTRUE(all.equal(norme(c(3, 4)), 5)))
stopifnot(isTRUE(all.equal(distance(c(1, 2, 2), c(4, 6, 2)), 5)))
stopifnot(produit_scalaire(c(2, 1, -1), c(1, -1, 1)) == 0)
stopifnot(isTRUE(all.equal(angle(c(1, 0), c(1, sqrt(3))), pi / 3)))
cat("AL01 — tous les tests sont réussis.\n")
