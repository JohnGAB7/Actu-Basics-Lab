# F01 — Approfondissement : nombres, ensembles et numération

## 1. Structure des ensembles numériques

On utilise les inclusions \(\mathbb N\subset\mathbb Z\subset\mathbb Q\subset\mathbb R\subset\mathbb C\), avec la convention \(0\in\mathbb N\). Chaque inclusion est stricte : \(-1\in\mathbb Z\setminus\mathbb N\), \(1/2\in\mathbb Q\setminus\mathbb Z\), \(\sqrt2\in\mathbb R\setminus\mathbb Q\), et \(i\in\mathbb C\setminus\mathbb R\).

**Résultat.** Un rationnel possède une écriture décimale finie si et seulement si, après simplification, son dénominateur ne contient que les facteurs premiers 2 et 5.

**Justification.** Une écriture à \(n\) décimales est de la forme \(m/10^n\), dont le dénominateur simplifié ne peut contenir que 2 et 5. Réciproquement, si le dénominateur vaut \(2^a5^b\), on multiplie numérateur et dénominateur pour obtenir un dénominateur \(10^{\max(a,b)}\).

Exemples : \(7/40=0,175\), tandis que \(1/3=0,333\ldots\).

## 2. Valeur absolue et distance

Pour \(x\in\mathbb R\), \(|x|=\max(x,-x)\). La distance entre deux réels est \(d(a,b)=|a-b|\). Ainsi \(|x-a|<r\), avec \(r>0\), équivaut à \(a-r<x<a+r\).

La valeur absolue vérifie l'inégalité triangulaire : \(|x+y|\leq |x|+|y|\). Elle découle de \(-|x|\leq x\leq |x|\) et des mêmes bornes pour \(y\), d'où \(-(|x|+|y|)\leq x+y\leq |x|+|y|\).

**Contre-exemple à une intuition fréquente :** \(|x+y|=|x|+|y|\) n'est pas toujours vrai. Pour \(x=3,y=-2\), le membre gauche vaut 1 et le droit 5.

## 3. Numération positionnelle

En base \(b\geq2\), un entier s'écrit \(a_ka_{k-1}\ldots a_0\)_b et représente \(\sum_{j=0}^k a_jb^j\), avec \(0\leq a_j<b\). La conversion vers la base 10 est donc une évaluation polynomiale. La conversion inverse utilise les divisions euclidiennes successives par \(b\), les restes étant lus de bas en haut.

Exemple : \(101101_2=1\cdot32+0\cdot16+1\cdot8+1\cdot4+0\cdot2+1=45\).

## 4. Représentation machine et précision

Un ordinateur représente généralement les réels par des nombres flottants de précision finie. Il faut distinguer erreur d'arrondi, erreur de troncature et erreur de modèle. L'expression \(0,1+0,2\) peut ne pas être exactement égale à \(0,3\) en binaire flottant.

Pour comparer des calculs numériques, préférer une tolérance : \(|x-y|\leq \varepsilon_{abs}+\varepsilon_{rel}|y|\). Le choix des tolérances dépend de l'échelle et du problème.

## 5. Exercices de raisonnement

1. Montrer que \(0,125\) est rationnel et donner sa fraction irréductible.
2. Déterminer si \(13/75\) possède une écriture décimale finie, en justifiant.
3. Résoudre \(|2x-3|\leq5\) comme une condition de distance.
4. Convertir \(173_{10}\) en base 2 puis vérifier par reconversion.
5. Expliquer pourquoi une égalité numérique approchée ne constitue pas une preuve d'égalité exacte.

## 6. Application quantitative

Un système stocke un montant en unités monétaires avec deux décimales. Décrire la différence entre arrondir chaque transaction puis sommer, et sommer les montants exacts puis arrondir une seule fois. Construire un exemple où les résultats diffèrent. Cette différence est une question de règle de calcul, pas seulement de format d'affichage.

**À maîtriser :** inclusions d'ensembles, critère des décimaux finis, distance, inégalité triangulaire, conversion de base et limites des flottants.