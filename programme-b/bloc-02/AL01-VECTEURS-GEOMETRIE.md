# AL01 — Vecteurs et géométrie dans \(\mathbb R^n\)

**Programme B · Bloc 2 — Algèbre linéaire**  
Niveau : universitaire introductif, progression vers la formalisation.  
Charge indicative : 8 à 10 heures d'étude et 6 à 8 heures d'exercices.  
Prérequis : calcul algébrique, coordonnées cartésiennes, équations et fonctions du Bloc 1.

## Objectifs d'apprentissage

À l'issue de cette unité, l'apprenant doit pouvoir :
1. distinguer point, vecteur libre, coordonnées et déplacement ;
2. effectuer les opérations vectorielles et interpréter leurs propriétés ;
3. calculer normes, distances, produits scalaires et angles ;
4. utiliser l'inégalité de Cauchy-Schwarz et l'inégalité triangulaire ;
5. décrire droites et plans à l'aide de formes paramétriques et cartésiennes ;
6. comprendre combinaison linéaire, colinéarité et coplanarité dans les cas géométriques simples ;
7. reconnaître la généralisation de \(\mathbb R^2\) et \(\mathbb R^3\) à \(\mathbb R^n\).

## 1. Points et vecteurs

Un **point** décrit une position. Un **vecteur** décrit un déplacement, une direction et une norme. Dans un repère, un vecteur de \(\mathbb R^n\) est une liste ordonnée de \(n\) réels :
\[
x=(x_1,\ldots,x_n).
\]
Les coordonnées dépendent du repère choisi ; le vecteur géométrique ne se réduit pas à son écriture dans un repère particulier.

Pour deux points \(A=(a_1,\ldots,a_n)\) et \(B=(b_1,\ldots,b_n)\), le vecteur déplacement est
\[
\overrightarrow{AB}=B-A=(b_1-a_1,\ldots,b_n-a_n).
\]
Exemple : si \(A=(2,-1)\) et \(B=(5,3)\), alors \(\overrightarrow{AB}=(3,4)\).

## 2. Opérations vectorielles

Pour \(x,y\in\mathbb R^n\) et \(\lambda\in\mathbb R\) :
\[
x+y=(x_1+y_1,\ldots,x_n+y_n),
\qquad
\lambda x=(\lambda x_1,\ldots,\lambda x_n).
\]
Le vecteur nul \(0=(0,\ldots,0)\) est neutre pour l'addition et \(-x\) est l'opposé de \(x\).

Les propriétés suivantes découlent des propriétés des réels, coordonnée par coordonnée :
- commutativité : \(x+y=y+x\) ;
- associativité : \((x+y)+z=x+(y+z)\) ;
- distributivité : \(\lambda(x+y)=\lambda x+\lambda y\) ;
- compatibilité : \((\lambda\mu)x=\lambda(\mu x)\) ;
- \(1x=x\).

Une combinaison linéaire de vecteurs \(v_1,\ldots,v_k\) est une expression
\[
\lambda_1v_1+\cdots+\lambda_kv_k.
\]
Elle permet de décrire les directions et les positions accessibles à partir de vecteurs donnés.

## 3. Norme et distance euclidiennes

La norme euclidienne de \(x\) est
\[
\|x\|_2=\sqrt{x_1^2+\cdots+x_n^2}.
\]
La distance entre \(x\) et \(y\) est \(d(x,y)=\|x-y\|_2\).

Exemple : pour \(x=(3,4)\), \(\|x\|_2=5\). Pour \(y=(-1,1)\), la distance entre \(x\) et \(y\) vaut
\[
\sqrt{(3+1)^2+(4-1)^2}=\sqrt{25}=5.
\]

La norme vérifie :
1. positivité : \(\|x\|\geq0\), et \(\|x\|=0\iff x=0\) ;
2. homogénéité : \(\|\lambda x\|=|\lambda|\|x\|\) ;
3. inégalité triangulaire : \(\|x+y\|\leq\|x\|+\|y\|\).

### Preuve de l'inégalité triangulaire

Le produit scalaire défini plus loin vérifie Cauchy-Schwarz. Ainsi :
\[
\|x+y\|^2=\|x\|^2+2\langle x,y\rangle+\|y\|^2
\leq \|x\|^2+2\|x\|\|y\|+\|y\|^2
=(\|x\|+\|y\|)^2.
\]
Les deux membres étant positifs, on prend la racine carrée.

## 4. Produit scalaire

Dans \(\mathbb R^n\), le produit scalaire euclidien est
\[
\langle x,y\rangle=x_1y_1+\cdots+x_ny_n.
\]
Il est bilinéaire, symétrique et défini positif :
\[
\langle x,x\rangle\geq0,\qquad \langle x,x\rangle=0\iff x=0.
\]
La norme s'en déduit : \(\|x\|=\sqrt{\langle x,x\rangle}\).

### 4.1 Cauchy-Schwarz

Pour tous \(x,y\in\mathbb R^n\),
\[
|\langle x,y\rangle|\leq\|x\|\|y\|.
\]
**Démonstration.** Si \(y=0\), c'est immédiat. Sinon, pour tout réel \(t\),
\[
0\leq\|x-ty\|^2
=\|x\|^2-2t\langle x,y\rangle+t^2\|y\|^2.
\]
Ce trinôme en \(t\) est toujours positif ou nul ; son discriminant est donc négatif ou nul :
\[
4\langle x,y\rangle^2-4\|x\|^2\|y\|^2\leq0.
\]
On obtient l'inégalité. L'égalité a lieu lorsque les vecteurs sont linéairement dépendants.

### 4.2 Angle et orthogonalité

Pour deux vecteurs non nuls, l'angle \(\theta\in[0,\pi]\) est défini par
\[
\cos\theta=\frac{\langle x,y\rangle}{\|x\|\|y\|}.
\]
Cauchy-Schwarz garantit que le membre de droite appartient à [-1,1]. Les vecteurs sont orthogonaux lorsque \(\langle x,y\rangle=0\).

Exemple : \(x=(1,2)\), \(y=(2,-1)\). Leur produit scalaire vaut \(2-2=0\) : ils sont perpendiculaires.

## 5. Combinaisons linéaires, colinéarité et géométrie

Deux vecteurs non nuls \(u,v\) sont colinéaires si l'un est un multiple scalaire de l'autre. En dimension 2, cela équivaut à l'annulation du déterminant des deux colonnes ; le déterminant sera étudié formellement dans AL05.

Trois vecteurs de \(\mathbb R^3\) sont coplanaires lorsqu'ils sont linéairement dépendants. Géométriquement, leur parallélépipède a un volume nul.

L'ensemble des combinaisons linéaires de \(v_1,\ldots,v_k\) est leur **espace engendré** :
\[
\operatorname{Vect}(v_1,\ldots,v_k)
=\{\lambda_1v_1+\cdots+\lambda_kv_k:\lambda_i\in\mathbb R\}.
\]
Ce concept sera formalisé dans AL03.

## 6. Droites et plans

### 6.1 Droite paramétrique

Une droite passant par \(A\) et de vecteur directeur non nul \(v\) s'écrit
\[
X=A+tv,\qquad t\in\mathbb R.
\]
En coordonnées dans \(\mathbb R^2\), avec \(A=(a_1,a_2)\) et \(v=(u_1,u_2)\) :
\[
x=a_1+tu_1,\quad y=a_2+tu_2.
\]

### 6.2 Équation cartésienne dans le plan

Une droite de normale \(n=(a,b)\ne0\), passant par \(A=(x_0,y_0)\), vérifie
\[
a(x-x_0)+b(y-y_0)=0.
\]
Soit \(ax+by+c=0\), avec \((a,b)\ne(0,0)\). Le vecteur normal est orthogonal au vecteur directeur.

### 6.3 Plan dans l'espace

Un plan de normale \(n=(a,b,c)\ne0\), passant par \(A=(x_0,y_0,z_0)\), vérifie
\[
a(x-x_0)+b(y-y_0)+c(z-z_0)=0.
\]
L'équation cartésienne est \(ax+by+cz+d=0\). Une représentation paramétrique utilise un point et deux directions non colinéaires appartenant au plan.

## 7. Généralisation à \(\mathbb R^n\)

Les formules de norme et de produit scalaire s'étendent à toute dimension finie. La géométrie devient moins directement visualisable au-delà de trois dimensions, mais les calculs coordonnés restent définis.

Dans les applications statistiques, une observation à \(p\) variables peut être représentée par un vecteur de \(\mathbb R^p\). Une collection de \(m\) observations donne naturellement une matrice \(m\times p\), étudiée dans AL02.

## 8. Applications quantitatives

- **Données multivariées :** un individu décrit par âge, ancienneté, revenu et fréquence d'usage devient un vecteur de caractéristiques. Les unités et échelles doivent être examinées avant toute distance.
- **Distance et similarité :** la distance euclidienne mesure une différence géométrique, mais peut être dominée par les variables à grande échelle. La standardisation ou d'autres métriques peuvent être nécessaires.
- **Combinaison de scénarios :** une combinaison linéaire de vecteurs représente une agrégation pondérée ; les poids doivent avoir une interprétation et des contraintes explicites.
- **Projection :** le produit scalaire permet de mesurer la composante d'un vecteur dans une direction. Les projections sur des sous-espaces seront approfondies en AL06.

## 9. Erreurs fréquentes

1. Confondre coordonnées d'un point et composantes d'un vecteur déplacement.
2. Additionner des points comme s'ils étaient des vecteurs sans préciser le repère affine.
3. Oublier la valeur absolue dans \(\|\lambda x\|=|\lambda|\|x\|\).
4. Calculer l'angle sans vérifier que les deux vecteurs sont non nuls.
5. Déduire l'orthogonalité d'un dessin approximatif au lieu de calculer le produit scalaire.
6. Utiliser une distance euclidienne sur des variables d'échelles incompatibles sans justification.
7. Décrire une droite par un vecteur directeur nul.
8. Généraliser une intuition de \(\mathbb R^2\) à \(\mathbb R^n\) sans vérifier les dimensions.

## 10. Synthèse

Les vecteurs portent des quantités directionnelles et des coordonnées ; les opérations linéaires permettent de les combiner ; la norme mesure leur taille ; le produit scalaire formalise angles et orthogonalité ; les combinaisons linéaires décrivent les directions accessibles. Ces outils préparent les matrices et systèmes \(Ax=b\), qui constituent le cœur de l'unité AL02.

## 11. Références

- Gilbert Strang, *Introduction to Linear Algebra*, Wellesley-Cambridge Press.
- MIT OpenCourseWare, [18.06SC Linear Algebra — cours et syllabus](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/). Le cours précise que le calcul différentiel n'est pas nécessaire pour apprendre l'algèbre linéaire, mais que la familiarité avec vecteurs, matrices et coordonnées est utile.
- Stephen Boyd et Lieven Vandenberghe, [Introduction to Applied Linear Algebra](https://web.stanford.edu/~boyd/vmls/).

## 12. Critère de maîtrise

L'unité est maîtrisée lorsque l'apprenant sait effectuer les calculs sans erreur de dimension, justifier Cauchy-Schwarz et l'inégalité triangulaire, traduire une droite ou un plan entre formes paramétrique et cartésienne, expliquer le sens géométrique d'un produit scalaire et signaler les limites d'une distance calculée sur des variables hétérogènes.
