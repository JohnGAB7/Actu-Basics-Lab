# Atelier AL02 — matrices et systèmes linéaires (R de base)

matmul <- function(A, B) {
  if (ncol(A) != nrow(B)) stop("Dimensions incompatibles")
  A %*% B
}

gauss_solve <- function(A, b, tol = 1e-12) {
  A <- as.matrix(A)
  b <- as.numeric(b)
  n <- nrow(A)
  if (n != ncol(A) || length(b) != n) stop("A doit être carrée et compatible avec b")
  M <- cbind(A, b)
  for (j in seq_len(n)) {
    pivot <- j - 1 + which.max(abs(M[j:n, j]))
    if (abs(M[pivot, j]) <= tol) stop("Matrice singulière ou système non unique")
    if (pivot != j) M[c(j, pivot), ] <- M[c(pivot, j), ]
    if (j < n) {
      for (i in (j + 1):n) {
        facteur <- M[i, j] / M[j, j]
        M[i, j:(n + 1)] <- M[i, j:(n + 1)] - facteur * M[j, j:(n + 1)]
      }
    }
  }
  x <- numeric(n)
  for (i in n:1) {
    reste <- if (i < n) sum(M[i, (i + 1):n] * x[(i + 1):n]) else 0
    x[i] <- (M[i, n + 1] - reste) / M[i, i]
  }
  x
}

A <- matrix(c(2, 1, 1, -1), nrow = 2, byrow = TRUE)
stopifnot(isTRUE(all.equal(matmul(A, diag(2)), A)))
solution <- gauss_solve(A, c(5, 1))
stopifnot(isTRUE(all.equal(unname(solution), c(2, 1))))
cat("AL02 — tests de base réussis.\n")
