# AL02 — Matrices et systèmes linéaires

**Programme B · Bloc 2 — Algèbre linéaire**  
Niveau : universitaire introductif/intermédiaire.  
Charge indicative : 10 à 12 heures de cours et 8 à 10 heures d'exercices.  
Prérequis : AL01, algèbre et systèmes d'équations du Bloc 1.

## Objectifs

Savoir représenter un système par \(Ax=b\), effectuer les opérations matricielles, comprendre les dimensions, résoudre un système par élimination de Gauss, distinguer existence et unicité des solutions, reconnaître les matrices inversibles et comprendre la factorisation \(A=LU\).

## 1. Définition et notation

Une matrice réelle de taille \(m\times n\) est un tableau \(A=(a_{ij})\) de \(m\) lignes et \(n\) colonnes :
\[
A=\begin{pmatrix}a_{11}&\cdots&a_{1n}\\ \vdots&&\vdots\\a_{m1}&\cdots&a_{mn}\end{pmatrix}.
\]
Le nombre de lignes est \(m\), celui des colonnes \(n\). Une matrice carrée vérifie \(m=n\). La matrice nulle, l'identité \(I_n\) et la matrice diagonale jouent des rôles particuliers.

La transposée \(A^\top\) échange lignes et colonnes. Les dimensions deviennent \(n\times m\).

## 2. Opérations et compatibilité dimensionnelle

Deux matrices de même taille s'additionnent terme à terme. La multiplication par un scalaire s'effectue sur chaque coefficient.

Le produit \(AB\) est défini si le nombre de colonnes de \(A\) égale le nombre de lignes de \(B\). Si \(A\) est \(m\times n\) et \(B\) est \(n\times p\), alors \(AB\) est \(m\times p\) et
\[
(AB)_{ij}=\sum_{k=1}^n a_{ik}b_{kj}.
\]
En général \(AB\ne BA\), et parfois \(AB\) existe alors que \(BA\) n'existe pas.

Propriétés :
- associativité : \((AB)C=A(BC)\), lorsque les produits sont définis ;
- distributivité : \(A(B+C)=AB+AC\) ;
- identité : \(AI=IA=A\) ;
- transposition : \((AB)^\top=B^\top A^\top\).

La multiplication matricielle représente la composition de transformations linéaires ; l'ordre inversé change généralement la transformation.

## 3. Systèmes linéaires sous forme matricielle

Un système de \(m\) équations à \(n\) inconnues s'écrit \(Ax=b\), où \(A\in\mathbb R^{m\times n}\), \(x\in\mathbb R^n\), \(b\in\mathbb R^m\).

Exemple :
\[
\begin{cases}
2x+y=5,\\
x-y=1
\end{cases}
\quad\Longleftrightarrow\quad
\begin{pmatrix}2&1\\1&-1\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=\begin{pmatrix}5\\1\end{pmatrix}.
\]

Le système peut avoir :
- aucune solution ;
- une solution unique ;
- une infinité de solutions.

La forme carrée ne garantit pas à elle seule l'unicité. La structure des colonnes et les pivots sont déterminants.

## 4. Opérations élémentaires sur les lignes

Les opérations suivantes ne changent pas l'ensemble des solutions :
1. échanger deux lignes ;
2. multiplier une ligne par un scalaire non nul ;
3. ajouter à une ligne un multiple d'une autre ligne.

On applique ces opérations à la matrice augmentée \([A\mid b]\).

### 4.1 Élimination de Gauss

L'objectif est d'obtenir une forme échelonnée :
- les lignes nulles éventuelles sont en bas ;
- le premier coefficient non nul de chaque ligne (pivot) est à droite du pivot précédent ;
- les coefficients sous les pivots sont nuls.

On résout ensuite par substitution arrière.

### Exemple détaillé

\[
\begin{cases}
x+2y-z=0,\\
2x+5y+z=3,\\
-x-y+2z=1.
\end{cases}
\]
Matrice augmentée :
\[
\left[\begin{array}{rrr|r}
1&2&-1&0\\
2&5&1&3\\
-1&-1&2&1
\end{array}\right].
\]
\(L_2\leftarrow L_2-2L_1\), \(L_3\leftarrow L_3+L_1\) :
\[
\left[\begin{array}{rrr|r}
1&2&-1&0\\
0&1&3&3\\
0&1&1&1
\end{array}\right].
\]
\(L_3\leftarrow L_3-L_2\) :
\[
\left[\begin{array}{rrr|r}
1&2&-1&0\\
0&1&3&3\\
0&0&-2&-2
\end{array}\right].
\]
Donc \(z=1\), puis \(y+3=3\), donc \(y=0\), puis \(x-1=0\), donc \(x=1\). Solution unique \((1,0,1)\).

## 5. Forme échelonnée réduite et pivots

La forme échelonnée réduite impose en plus :
- chaque pivot vaut 1 ;
- chaque pivot est l'unique coefficient non nul de sa colonne.

Elle permet de lire directement les variables pivots et libres. Les variables libres paramètrent les solutions lorsque le système est compatible et sous-déterminé.

Une ligne \([0\ \cdots\ 0\mid c]\) avec \(c\ne0\) correspond à \(0=c\) : le système est incompatible.

## 6. Existence et unicité : premiers critères

Le rang est le nombre de pivots de la matrice échelonnée. Sa définition intrinsèque sera approfondie dans AL03.

Pour \(A\in\mathbb R^{m\times n}\), le système \(Ax=b\) est compatible si et seulement si \(b\) appartient à l'espace engendré par les colonnes de \(A\). Si le système est compatible, l'ensemble des solutions est une solution particulière plus le noyau de \(A\).

Pour une matrice carrée \(A\in\mathbb R^{n\times n}\), les conditions suivantes sont équivalentes :
- \(Ax=b\) possède une solution unique pour tout \(b\in\mathbb R^n\) ;
- \(Ax=0\) n'a que la solution nulle ;
- \(A\) possède \(n\) pivots ;
- \(A\) est inversible.

La démonstration complète sera reprise après l'étude des espaces vectoriels.

## 7. Matrice inverse

Une matrice carrée \(A\) est inversible s'il existe \(A^{-1}\) telle que
\[
AA^{-1}=A^{-1}A=I.
\]
L'inverse est unique. Si elle existe, la solution de \(Ax=b\) est \(x=A^{-1}b\).

Pour une matrice \(2\times2\),
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
A^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}
\]
lorsque \(ad-bc\ne0\). Le déterminant sera défini et étudié dans AL05.

En calcul numérique, former explicitement l'inverse est généralement moins efficace et moins stable que résoudre directement le système par factorisation. La formule est surtout conceptuelle et utile pour les petites matrices.

## 8. Factorisation LU — première approche

L'élimination de Gauss peut être codée sous la forme
\[
A=LU,
\]
où \(L\) est triangulaire inférieure (souvent avec des 1 sur la diagonale) et \(U\) triangulaire supérieure, lorsque l'élimination se déroule sans permutation de lignes. Avec pivotement, on écrit généralement \(PA=LU\).

Résoudre \(Ax=b\) revient alors à résoudre successivement \(Ly=b\), puis \(Ux=y\). Une factorisation peut être réutilisée pour plusieurs seconds membres \(b\).

La factorisation LU sera approfondie dans AL08 avec le pivotement, les erreurs d'arrondi et les limites de stabilité.

## 9. Applications

- **Équilibre de flux :** conservation d'un flux dans plusieurs secteurs se traduit par un système linéaire.
- **Mélanges et allocations :** les contraintes de ressources peuvent être écrites \(Ax=b\).
- **Modèles linéaires :** les prédicteurs et coefficients peuvent être organisés en matrices, même si l'estimation statistique et les hypothèses du modèle demandent un traitement distinct.
- **Réseaux :** les relations entre nœuds et arêtes conduisent à des matrices d'incidence.
- **Actuariat :** des systèmes simplifiés peuvent représenter des équilibres de flux ou des répartitions ; les données réelles peuvent être bruitées, contraintes et non linéaires.

## 10. Erreurs fréquentes

1. Multiplier des matrices dont les dimensions ne sont pas compatibles.
2. Supposer \(AB=BA\).
3. Effectuer une opération de ligne sur \(A\) sans l'effectuer sur \(b\).
4. Diviser par un pivot nul sans permuter les lignes.
5. Conclure qu'un système carré a nécessairement une solution unique.
6. Oublier de traiter les variables libres.
7. Confondre une ligne nulle et une contradiction \(0=c\ne0\).
8. Utiliser l'inverse explicite pour un grand système numérique sans raison.
9. Confondre solution exacte et solution approchée d'un système mal conditionné.

## 11. Critères de maîtrise

L'apprenant doit pouvoir :
- contrôler les dimensions avant toute opération ;
- calculer un produit matriciel et sa transposée ;
- traduire un système en \(Ax=b\) ;
- appliquer Gauss sans perdre les équivalences ;
- classifier les cas compatible unique, compatible indéterminé et incompatible ;
- justifier les critères d'inversibilité d'une matrice carrée ;
- expliquer pourquoi une factorisation est préférable à un calcul explicite d'inverse dans les grands problèmes.

## 12. Références

- Gilbert Strang, *Introduction to Linear Algebra*, Wellesley-Cambridge Press.
- MIT OpenCourseWare, [18.06SC Linear Algebra — Unit I: \(Ax=b\) and the Four Subspaces](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/).
- MIT OpenCourseWare, [18.06 Linear Algebra — syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/).
- Stephen Boyd et Lieven Vandenberghe, [Introduction to Applied Linear Algebra](https://web.stanford.edu/~boyd/vmls/).
