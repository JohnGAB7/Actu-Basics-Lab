# Bloc 2 — Algèbre linéaire et géométrie vectorielle

**Programme B · Cursus mathématique, statistique et quantitatif**

## 1. Positionnement dans le cursus

Le Bloc 2 prolonge les fondations mathématiques du Bloc 1. Il développe le langage des vecteurs, des matrices et des transformations linéaires qui structure aujourd'hui une grande partie des mathématiques appliquées, de la statistique, de l'économétrie, de l'informatique scientifique et de l'apprentissage automatique.

Le Bloc 2 est un domaine autonome : il ne suppose pas la maîtrise du calcul différentiel multivarié. Les prérequis utiles sont l'algèbre du Bloc 1, les fonctions, les systèmes d'équations, la géométrie analytique et les notions élémentaires de preuve. Le calcul différentiel peut éclairer certaines applications, mais il n'est pas nécessaire pour commencer l'algèbre linéaire.

## 2. Objectifs généraux

À la fin du bloc, l'apprenant sera capable de :
1. représenter et interpréter des vecteurs dans des espaces de dimension finie ;
2. modéliser un système linéaire par \(Ax=b\), résoudre et classifier ses solutions ;
3. comprendre espaces vectoriels, sous-espaces, indépendance, bases, dimension et rang ;
4. interpréter les transformations linéaires et les changements de base ;
5. utiliser déterminants et critères d'inversibilité avec discernement ;
6. maîtriser produit scalaire, orthogonalité, projections et moindres carrés ;
7. calculer et interpréter valeurs propres, vecteurs propres et diagonalisation ;
8. comprendre les factorisations LU, QR, Cholesky et la décomposition en valeurs singulières ;
9. distinguer résolution exacte, approximation numérique, stabilité et conditionnement ;
10. mobiliser l'algèbre linéaire dans des problèmes de régression, de données, de réseaux, de chaînes de Markov et de réduction de dimension.

## 3. Architecture du bloc

| Code | Unité | Contenus principaux | Compétence |
|---|---|---|---|
| AL01 | Vecteurs et géométrie dans \(\mathbb R^n\) | Vecteurs, opérations, norme, distance, produit scalaire, angles, droites et plans | Décrire géométriquement les objets vectoriels |
| AL02 | Matrices et systèmes linéaires | Opérations, systèmes \(Ax=b\), élimination de Gauss, pivots, rang initial, inverses, LU | Résoudre et classifier les systèmes |
| AL03 | Espaces vectoriels et dimension | Sous-espaces, combinaisons, span, indépendance, bases, dimension, quatre sous-espaces fondamentaux | Comprendre la structure des solutions |
| AL04 | Applications linéaires | Linéarité, noyau, image, rang-nullité, matrices d'applications, composition et changement de base | Relier transformations et matrices |
| AL05 | Déterminants et inversibilité | Définition, propriétés, développement, opérations élémentaires, volume, interprétation géométrique | Comprendre l'inversibilité et le volume orienté |
| AL06 | Orthogonalité et moindres carrés | Orthogonalité, projections, Gram-Schmidt, QR, approximation, équations normales et résidus | Construire des approximations optimales |
| AL07 | Valeurs propres et diagonalisation | Polynôme caractéristique, spectre, diagonalisation, matrices symétriques, théorème spectral, matrices définies positives | Étudier les transformations itérées |
| AL08 | Factorisations et algèbre linéaire numérique | LU, QR, Cholesky, SVD, pseudo-inverse, conditionnement, stabilité, méthodes numériques | Choisir et évaluer une méthode de calcul |

Les applications transversales (régression linéaire, PCA, graphes et réseaux, matrices de transition, compression et systèmes de grande dimension) seront distribuées dans les unités où les outils correspondants sont établis.

## 4. Progression et dépendances

AL01 → AL02 → AL03 → AL04 → AL05.  
AL03 et AL04 préparent AL06. AL05 et AL06 préparent AL07. AL06 et AL07 préparent AL08.

Un apprenant peut utiliser les matrices dès AL02 sans avoir encore étudié la définition abstraite d'un espace vectoriel ; le cours reviendra ensuite sur les fondements et explicitera les structures.

## 5. Méthode pédagogique

Chaque unité doit comporter :
- des objectifs observables et prérequis explicites ;
- une intuition géométrique ou algorithmique, suivie d'une définition formelle ;
- des propositions avec hypothèses, démonstrations ou justifications ;
- des exemples résolus à la main et des contre-exemples ;
- des interprétations géométriques, algébriques et numériques ;
- des applications quantitatives sans réduire la théorie à un contexte métier ;
- des exercices gradués et corrigés détaillés ;
- des ateliers Python et R, et Excel lorsque pertinent ;
- des erreurs fréquentes, critères de maîtrise et références.

## 6. Évaluation du bloc

Évaluation cumulative proposée :
1. exercices formatifs à chaque unité ;
2. devoirs de synthèse après AL03 et AL06 ;
3. ateliers numériques avec comparaison entre calcul manuel et calcul logiciel ;
4. examen final écrit et problème intégrateur ;
5. mini-projet reproductible sur un jeu de données ou un réseau.

Les seuils de validation seront fixés dans le dossier d'évaluation. Ils sont des conventions pédagogiques du Programme B, pas des normes universitaires universelles. Le dépôt des supports ne vaut pas réussite d'un apprenant.

## 7. Ressources publiées

### AL01 — Vecteurs et géométrie
- [Cours AL01](AL01-VECTEURS-GEOMETRIE.md)
- [Exercices corrigés AL01](EXERCICES-AL01-VECTEURS.md)
- [Atelier Python](ateliers/python/al01_vecteurs.py)
- [Atelier R](ateliers/r/al01_vecteurs.R)

Les autres unités seront ajoutées dans cet index au fur et à mesure de leur rédaction, contrôle et publication.

## 8. Références structurantes

1. Gilbert Strang, *Introduction to Linear Algebra*, Wellesley-Cambridge Press. Référence de fond pour matrices, espaces, projections, valeurs propres et SVD.
2. MIT OpenCourseWare, [18.06SC Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), cours d'autoformation structuré en \(Ax=b\) et quatre sous-espaces, moindres carrés/déterminants/valeurs propres, matrices définies positives et applications.
3. MIT OpenCourseWare, [18.06 Linear Algebra — syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/), objectifs et prérequis.
4. David C. Lay, Steven R. Lay et Judi J. McDonald, *Linear Algebra and Its Applications*, Pearson.
5. Stephen Boyd et Lieven Vandenberghe, [Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares](https://web.stanford.edu/~boyd/vmls/), ressource ouverte orientée vers les applications.

## 9. Périmètre et limites

Ce bloc traite principalement l'algèbre linéaire réelle de dimension finie, avec des ouvertures vers les matrices complexes, les espaces de fonctions et les problèmes numériques. Il n'est pas un cours complet d'analyse fonctionnelle, d'algèbre abstraite, de théorie spectrale infinidimensionnelle ni d'optimisation convexe. Ces sujets nécessiteront des prérequis et des blocs dédiés.

## 10. Règle de qualité

Une réponse correcte doit distinguer la structure mathématique, les hypothèses, la méthode de résolution, le résultat, l'interprétation géométrique et les limites numériques. Une matrice inversible calculée par logiciel n'explique pas à elle seule pourquoi l'inverse existe ; une solution de moindres carrés n'est pas automatiquement une solution exacte ; une valeur propre numériquement approchée n'est pas une preuve de diagonalisation.
