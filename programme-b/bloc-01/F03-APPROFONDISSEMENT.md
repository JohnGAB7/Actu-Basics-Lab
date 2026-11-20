# F03 — Approfondissement : pourcentages, variations et indices

## 1. Taux et facteur multiplicatif

Une hausse de \(t\) (écrit en proportion) transforme une valeur initiale \(V_0\) en \(V_1=V_0(1+t)\). Une baisse de \(t\) utilise \(1-t\). Le facteur multiplicatif permet de composer plusieurs périodes.

Si les taux successifs sont \(t_1,\ldots,t_n\), alors \(V_n=V_0\prod_{j=1}^n(1+t_j)\). Le taux global est le produit des facteurs moins 1, et non la somme simple des taux.

## 2. Démonstration de la non-additivité

Une hausse de 10 % puis une baisse de 10 % donne \(1,10\times0,90=0,99\). La valeur finale est donc inférieure de 1 % à la valeur initiale. L'asymétrie vient du fait que la seconde variation s'applique à une base modifiée.

Pour revenir de \(V_1\) à \(V_0\) après une hausse de \(t\), la baisse requise est \(t/(1+t)\), pas \(t\).

## 3. Indices et changement de base

Un indice base 100 s'écrit \(I_t=100X_t/X_0\). Il compare une valeur à une référence. Changer la base vers la période \(s\) revient à calculer \(I'_t=100I_t/I_s\), si les séries sont comparables.

Un indice synthétique dépend de la méthode de pondération. Deux indices construits avec des paniers ou des poids différents peuvent évoluer différemment sans que l'un soit nécessairement erroné.

## 4. Moyenne arithmétique et géométrique

Pour des facteurs positifs \(g_t\), le facteur moyen composé est \(\bar g=(\prod_{t=1}^n g_t)^{1/n}\). Le taux composé moyen vaut \(\bar g-1\). Il répond à la question : quel taux constant aurait conduit au même facteur cumulé ?

## 5. Pièges d'interprétation

- Une hausse de 20 % suivie d'une baisse de 20 % ne ramène pas au point de départ.
- Une variation en points de pourcentage n'est pas une variation en pourcentage.
- Une hausse relative dépend de la base choisie.
- Un indice ne donne pas à lui seul le niveau absolu de la grandeur.
- Comparer des taux suppose des définitions, populations et périodes compatibles.

## 6. Exercices avancés

1. Une prime augmente de 7 %, puis de 4 %, puis diminue de 3 %. Calculer le taux global.
2. Une valeur a doublé en 8 ans. Calculer le taux annuel composé constant.
3. Un taux passe de 2 % à 3 %. Distinguer l'écart en points et la variation relative.
4. Rebaser un indice 2020=100 lorsque l'indice de 2022 vaut 112 et celui de 2024 vaut 126.
5. Construire un exemple où la moyenne arithmétique des taux donne une conclusion différente du taux composé.

**À maîtriser :** facteurs multiplicatifs, composition, taux composé, rebasage, points de pourcentage et lecture critique des indices.