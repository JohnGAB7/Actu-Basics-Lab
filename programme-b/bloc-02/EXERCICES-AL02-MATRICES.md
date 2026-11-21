# Exercices corrigés — AL02 Matrices et systèmes linéaires

## Exercice 1 — Dimensions

Soit \(A\) une matrice \(3\times2\), \(B\) une matrice \(2\times4\). Quelles sont les dimensions de \(AB\) et \(BA\) ?

**Corrigé.** \(AB\) existe et est de taille \(3\times4\). \(BA\) n'existe pas, car les 4 colonnes de \(B\) ne correspondent pas aux 3 lignes de \(A\).

## Exercice 2 — Produit matriciel

Calculer
\[
A=\begin{pmatrix}1&2\\3&-1\end{pmatrix},\quad
B=\begin{pmatrix}2&0\\1&4\end{pmatrix}.
\]

**Corrigé.**
\[
AB=\begin{pmatrix}4&8\\5&-4\end{pmatrix},\qquad
BA=\begin{pmatrix}2&4\\13&-2\end{pmatrix}.
\]
Ils sont différents : la multiplication n'est pas commutative.

## Exercice 3 — Transposée

Calculer \(A^\top\) pour \(A=\begin{pmatrix}1&0&2\\-1&3&4\end{pmatrix}\).

**Corrigé.** \(A^\top=\begin{pmatrix}1&-1\\0&3\\2&4\end{pmatrix}\), de taille \(3\times2\).

## Exercice 4 — Écriture matricielle

Écrire le système \(2x-y=3\), \(x+3y=7\) sous forme \(Ax=b\).

**Corrigé.**
\[
\begin{pmatrix}2&-1\\1&3\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=\begin{pmatrix}3\\7\end{pmatrix}.
\]

## Exercice 5 — Gauss, solution unique

Résoudre \(x+2y=5\), \(3x-y=4\).

**Corrigé.** Matrice augmentée \(\left[\begin{smallmatrix}1&2|5\\3&-1|4\end{smallmatrix}\right]\). \(L_2\leftarrow L_2-3L_1\) donne \([0,-7|-11]\), donc \(y=11/7\). Puis \(x=5-22/7=13/7\). Solution unique \((13/7,11/7)\).

## Exercice 6 — Système incompatible

Étudier \(x+y=1\), \(2x+2y=3\).

**Corrigé.** La deuxième ligne moins deux fois la première donne \(0=1\). Le système est incompatible.

## Exercice 7 — Infinité de solutions

Résoudre \(x+2y=4\), \(2x+4y=8\).

**Corrigé.** Les deux équations sont dépendantes. Poser \(y=t\), alors \(x=4-2t\). Ensemble des solutions : \((x,y)=(4-2t,t)\), \(t\in\mathbb R\).

## Exercice 8 — Variables libres

Résoudre \(x+y+z=3\), \(2x-y+z=2\).

**Corrigé.** Soustraire deux fois la première équation à la seconde donne \(-3y-z=-4\), donc \(y=(4-z)/3\). Poser \(z=t\). Alors \(y=(4-t)/3\), et \(x=3-y-z=(5-2t)/3\). Une infinité de solutions paramétrées par \(t\).

## Exercice 9 — Pivot nul

Résoudre \(0x+y=2\), \(x+y=3\), en expliquant le choix du pivot.

**Corrigé.** Le premier pivot de la première ligne est nul. Échanger les deux lignes donne \(x+y=3\), \(y=2\), donc \(x=1\), \(y=2\). Il ne faut jamais diviser par un pivot nul.

## Exercice 10 — Inverse 2×2

Calculer l'inverse de \(A=\begin{pmatrix}2&1\\1&1\end{pmatrix}\).

**Corrigé.** \(ad-bc=2-1=1\). Donc \(A^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}\). Vérifier que le produit avec \(A\) donne \(I_2\).

## Exercice 11 — Résolution par inverse

Résoudre \(Ax=b\) avec \(A\) de l'exercice 10 et \(b=(5,3)^\top\).

**Corrigé.** \(x=A^{-1}b=(5-3,-5+6)^\top=(2,1)^\top\). Vérification : \(2(2)+1=5\), \(2+1=3\).

## Exercice 12 — Factorisation LU

Vérifier la factorisation suivante :
\[
A=\begin{pmatrix}2&1\\4&3\end{pmatrix},\quad
L=\begin{pmatrix}1&0\\2&1\end{pmatrix},\quad
U=\begin{pmatrix}2&1\\0&1\end{pmatrix}.
\]

**Corrigé.** \(LU=\begin{pmatrix}2&1\\4&3\end{pmatrix}=A\). Pour résoudre \(Ax=b\), on résout d'abord \(Ly=b\), puis \(Ux=y\).

## Exercice 13 — Interprétation des solutions

Un modèle d'allocation \(Ax=b\) admet une infinité de solutions. Est-ce nécessairement un défaut de calcul ?

**Corrigé.** Non. Cela peut refléter des contraintes redondantes ou une liberté réelle dans l'allocation. Il faut déterminer les variables libres, ajouter éventuellement des contraintes justifiées par le problème, et ne pas imposer arbitrairement une solution unique.

## Exercice 14 — Contrôle d'une solution

Pour \(A=\begin{pmatrix}1&2\\3&-1\end{pmatrix}\), \(x=(2,1)^\top\), calculer \(Ax\).

**Corrigé.** \(Ax=(4,5)^\top\). Cette opération permet de vérifier une solution proposée à un système dont le second membre serait \(b=(4,5)^\top\).

## Exercice 15 — Synthèse et conditionnement

Un système a une solution exacte unique, mais une petite perturbation de \(b\) provoque une grande variation de la solution. La matrice est-elle nécessairement singulière ?

**Corrigé.** Non. Elle peut être inversible mais mal conditionnée. L'unicité est une propriété algébrique ; la sensibilité aux perturbations est une propriété numérique. Le conditionnement sera étudié en AL08.
