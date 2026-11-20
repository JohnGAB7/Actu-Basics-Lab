# Exercices corrigés — Topologie élémentaire de R

**Programme B · Bloc 1 · Extension préparatoire d'analyse réelle**  
**Consigne :** rédiger les preuves et justifier les hypothèses des théorèmes. Un résultat annoncé sans argument ne constitue pas une solution complète.

---

## Partie A — Ouverts et fermés

### Exercice 1 — Classifier les intervalles

Pour chacun des ensembles suivants, déterminer s'il est ouvert, fermé, les deux ou aucun dans R :
(a) (0,1) ; (b) [0,1] ; (c) [0,1) ; (d) R ; (e) l'ensemble vide ; (f) {3}.

**Corrigé.**

(a) (0,1) est ouvert, pas fermé : la suite 1/n appartient à l'ensemble pour n≥2 et converge vers 0 qui n'y appartient pas.  
(b) [0,1] est fermé et borné, mais pas ouvert : aucune boule centrée en 0 ne reste dans l'ensemble.  
(c) [0,1) n'est ni ouvert ni fermé : 0 n'est pas intérieur, et 1 est limite de points de l'ensemble sans lui appartenir.  
(d) R est ouvert et fermé : son complémentaire est vide.  
(e) L'ensemble vide est ouvert et fermé par vacuité et complémentarité.  
(f) {3} est fermé, car son complémentaire est ouvert ; il n'est pas ouvert, car toute boule centrée en 3 contient d'autres réels.

### Exercice 2 — Union et intersection

Poser U_n=(-1/n,1/n) pour n≥1.

1. Montrer que chaque U_n est ouvert.
2. Déterminer leur intersection.
3. Cette intersection est-elle ouverte ?

**Corrigé.**

Chaque intervalle ouvert U_n est ouvert. Un réel x appartient à tous les U_n si |x|<1/n pour tout n. Cela n'est possible que pour x=0 ; donc l'intersection vaut {0}. Le singleton {0} n'est pas ouvert. L'intersection infinie d'ouverts n'est donc pas nécessairement ouverte.

### Exercice 3 — Caractérisation séquentielle d'un fermé

Montrer que F={1/n : n≥1}∪{0} est fermé dans R.

**Corrigé.**

Soit une suite (x_k) de F qui converge vers x. Si x=0, la limite appartient à F. Si x>0, il existe un voisinage de x qui ne contient qu'un nombre fini de points de l'ensemble F, car les points 1/n ne s'accumulent qu'en 0. Une suite convergente vers x>0, dont les termes appartiennent à F, doit alors prendre finalement l'une des valeurs de ce voisinage ; sa limite est cette valeur et appartient à F. Une limite négative est impossible puisque tous les termes sont non négatifs. Ainsi toute limite de suite de F reste dans F ; F est fermé.

### Exercice 4 — Fermeture d'un ensemble

Déterminer l'adhérence et la frontière de A=(0,1)∪{2}.

**Corrigé.**

L'adhérence est [0,1]∪{2}, car 0 et 1 sont approchés par les points de (0,1), et 2 appartient à A comme point isolé. L'intérieur est (0,1). La frontière vaut donc {0,1,2}.

---

## Partie B — Adhérence, densité et accumulation

### Exercice 5 — Densité des rationnels

Énoncer ce que signifie « Q est dense dans R ». Pourquoi cela n'implique-t-il pas Q=R ?

**Corrigé.**

Q est dense dans R si tout intervalle ouvert non vide contient un rationnel, ou de façon équivalente si l'adhérence de Q est R. Cela n'implique pas Q=R : les irrationnels existent, par exemple √2, et Q reste dénombrable alors que R est non dénombrable.

### Exercice 6 — Frontière des rationnels

Montrer que la frontière de Q dans R est R.

**Corrigé.**

Tout intervalle ouvert non vide contient un rationnel et un irrationnel. Ainsi chaque voisinage de chaque réel rencontre Q et R\Q. Chaque réel est donc un point frontière. La frontière de Q est R.

### Exercice 7 — Points isolés et accumulation

Soit A={0}∪{1/n : n≥1}. Déterminer les points isolés et les points d'accumulation.

**Corrigé.**

Chaque 1/n est isolé : on peut choisir un petit intervalle autour de 1/n qui ne contient aucun autre élément de A. Le point 0 est un point d'accumulation, puisque 1/n→0. Il n'y a pas d'autre point d'accumulation, car les termes 1/n ne peuvent s'accumuler qu'en 0. L'adhérence de A est donc A lui-même.

### Exercice 8 — Intérieur vide

Montrer que Z a un intérieur vide et que sa frontière est Z.

**Corrigé.**

Aucune boule ouverte centrée en un entier ne reste dans Z, car tout intervalle réel contient des non-entiers. Aucun réel non entier n'est adhérent à Z : sa distance aux entiers voisins est strictement positive. Ainsi l'adhérence de Z est Z, l'intérieur est vide, et la frontière vaut adhérence moins intérieur, soit Z.

---

## Partie C — Compacité

### Exercice 9 — Appliquer Heine–Borel

Les ensembles suivants sont-ils compacts dans R ?
(a) [−2,5] ; (b) (−2,5) ; (c) [0,+∞) ; (d) Z ; (e) {1/n : n≥1}∪{0}.

**Corrigé.**

(a) Oui : fermé et borné.  
(b) Non : borné mais non fermé.  
(c) Non : fermé mais non borné.  
(d) Non : fermé mais non borné.  
(e) Oui : l'ensemble est borné et fermé, comme établi par la caractérisation séquentielle. Le théorème de Heine–Borel s'applique.

### Exercice 10 — Recouvrement sans sous-recouvrement fini

Montrer que la famille U_n=(-n,n), n≥1, recouvre R mais qu'aucune sous-famille finie ne recouvre R.

**Corrigé.**

Tout réel x appartient à U_n dès que n>|x|, donc la famille recouvre R. Une sous-famille finie possède un plus grand indice N ; son union est alors U_N=(-N,N), qui ne couvre pas R. R n'est donc pas compact.

### Exercice 11 — Pourquoi la fermeture compte

La fonction f(x)=1/x est-elle bornée sur (0,1) ? Le domaine est-il compact ? Expliquer le lien avec le théorème de Weierstrass.

**Corrigé.**

f est continue sur (0,1), mais n'est pas bornée : f(x)→+∞ lorsque x→0 par valeurs positives. Le domaine est borné mais pas fermé, donc non compact. Le théorème de Weierstrass ne s'applique pas. Cela montre pourquoi la seule bornitude du domaine ne suffit pas.

---

## Partie D — Continuité, compacité et connexité

### Exercice 12 — Théorème des bornes atteintes

Soit f(x)=x²−2x sur [0,3]. Justifier l'existence d'un minimum et d'un maximum, puis les déterminer.

**Corrigé.**

Le domaine [0,3] est compact et f est continue. Weierstrass assure que les deux bornes sont atteintes. On écrit f(x)=(x−1)²−1 : le minimum vaut −1 en x=1. Pour le maximum sur [0,3], les valeurs aux extrémités sont f(0)=0 et f(3)=3 ; la parabole est convexe et son maximum sur cet intervalle est 3, atteint en x=3.

### Exercice 13 — Continuité uniforme

Montrer que f(x)=3x+1 est uniformément continue sur R.

**Corrigé.**

Pour tous x,y réels,
\[
|f(x)-f(y)|=3|x-y|.
\]
Soit ε>0. Choisissons δ=ε/3. Si |x−y|<δ, alors |f(x)−f(y)|<ε. Le δ ne dépend pas de x : la continuité est uniforme sur R.

### Exercice 14 — Connexité et intervalles

Les ensembles [0,1]∪[2,3] et (0,2) sont-ils connexes dans R ?

**Corrigé.**

[0,1]∪[2,3] n'est pas un intervalle et n'est pas connexe : il peut être séparé en ses deux morceaux disjoints. (0,2) est un intervalle, donc connexe dans R.

### Exercice 15 — Valeurs intermédiaires

Soit f:[−1,2]→R continue avec f(−1)=−3 et f(2)=4. Que peut-on affirmer sur l'équation f(x)=1 ?

**Corrigé.**

Comme le domaine [−1,2] est un intervalle et f est continue, le théorème des valeurs intermédiaires garantit qu'il existe au moins un c dans [−1,2] tel que f(c)=1, puisque 1 est entre −3 et 4. L'unicité n'est pas garantie.

---

## Partie E — Synthèse et contre-exemples

### Exercice 16 — Vrai ou faux, avec justification

1. Toute partie fermée de R est compacte.
2. Toute partie compacte de R est fermée.
3. Toute intersection d'ouverts est ouverte.
4. Toute union de fermés est fermée.
5. L'image continue d'un compact est compacte.
6. Tout intervalle de R est connexe.

**Corrigé.**

1. Faux : R est fermé mais non borné, donc non compact.  
2. Vrai : conséquence de Heine–Borel (ou de la compacité dans R).  
3. Faux : l'intersection des (-1/n,1/n) vaut {0}, non ouvert.  
4. Faux : l'union des singletons {1/n} n'est pas fermée sans le point limite 0.  
5. Vrai : théorème de l'image continue d'un compact.  
6. Vrai : caractérisation des connexes dans R.

### Exercice 17 — Un ensemble à la fois dense et de mesure conceptuelle faible

Expliquer pourquoi Q peut être dense tout en étant dénombrable. Quel enseignement faut-il en tirer sur la notion de « taille » ?

**Corrigé.**

La densité est une propriété de proximité : chaque intervalle contient des rationnels. La dénombrabilité est une propriété de cardinalité : les rationnels peuvent être énumérés. Ces notions sont indépendantes. Un ensemble peut être dénombrable et dense, donc « rencontrer partout » sans contenir tous les points.

### Exercice 18 — Optimisation et existence

On considère une fonction continue f sur un ensemble de paramètres K⊂R. Quelles hypothèses simples garantissent que f atteint un minimum global ? Donner un exemple où la conclusion échoue si K n'est pas fermé.

**Corrigé.**

Il suffit que K soit compact, ce qui dans R équivaut à être fermé et borné, et que f soit continue. Exemple : f(x)=x sur K=(0,1). Son infimum vaut 0 mais aucun point de K ne l'atteint. L'absence de fermeture empêche l'application de Weierstrass.

### Exercice 19 — Prouver qu'un ensemble est fermé

Soit F={x∈R : x²≤4}. Montrer que F est fermé de deux façons :
1. en déterminant F explicitement ;
2. en utilisant la continuité de g(x)=x².

**Corrigé.**

La première méthode donne F=[−2,2], intervalle fermé. Pour la seconde, g est continue et F=g^{-1}((−∞,4]). L'ensemble (−∞,4] est fermé ; l'image réciproque d'un fermé par une fonction continue est fermée. Donc F est fermé.

### Exercice 20 — Problème de synthèse

Soit K=[0,2] et f(x)=x³−3x.

1. Justifier que f atteint un minimum et un maximum sur K.
2. Déterminer ces deux valeurs.
3. L'image f(K) est-elle un intervalle ?

**Corrigé.**

K est fermé et borné, donc compact ; f est polynomiale, donc continue. Weierstrass assure l'existence des extrema. On étudie f'(x)=3x²−3=3(x²−1), qui s'annule dans K en x=1. Les valeurs pertinentes sont f(0)=0, f(1)=−2 et f(2)=2. Le minimum est −2 et le maximum 2. Comme K est un intervalle et f est continue, f(K) est un intervalle ; ici f(K)=[−2,2].

---

## Grille de maîtrise

| Compétence | Exercices |
|---|---|
| Distinguer ouverts et fermés | 1–4 |
| Calculer adhérence, frontière et accumulation | 4, 6–8 |
| Comprendre densité et cardinalité | 5–6, 17 |
| Appliquer Heine–Borel | 9–11 |
| Exploiter compacité et continuité | 12–13, 18, 20 |
| Utiliser connexité et valeurs intermédiaires | 14–15 |
| Construire des contre-exemples et des preuves | 16, 19 |

**Critère pédagogique proposé :** viser au moins 16 exercices maîtrisés sur 20, dont les exercices 3, 9, 12, 16 et 20. Ce seuil est une convention interne au Programme B, pas une norme universitaire universelle.
