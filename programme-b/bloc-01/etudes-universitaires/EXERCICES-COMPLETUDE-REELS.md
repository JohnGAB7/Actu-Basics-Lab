# Exercices — Complétude, supremum, infimum et suites de Cauchy

**Consigne :** toute réponse doit être justifiée. Les exercices sont classés par compétence. Les preuves doivent expliciter les quantificateurs et les hypothèses utilisées.

## Partie A — Bornes, supremum et infimum

### Exercice 1 — Distinguer les notions
Pour chaque ensemble, déterminer s'il est majoré, minoré et borné. Calculer supremum et infimum lorsqu'ils existent. Préciser si maximum ou minimum existent.
1. A=(0,1).
2. B=[−2,3].
3. C={1/n : n∈N, n≥1}.
4. D={x∈R : x≥4}.
5. E={n∈Z : n≤0}.

### Exercice 2 — Caractérisation du supremum
Soit A non vide et majoré, et s∈R. Démontrer que s=sup A si et seulement si :
- pour tout a∈A, a≤s ;
- pour tout ε>0, il existe aε∈A tel que s−ε<aε.

### Exercice 3 — Unicité du supremum
Démontrer que si s et t sont tous deux des supremums de A, alors s=t.

### Exercice 4 — Supremum d'un ensemble transformé
Soit A⊂R non vide et majoré, et c∈R.
1. Démontrer que sup(A+c)=sup A+c.
2. Si λ>0, démontrer que sup(λA)=λ sup A.
3. Expliquer pourquoi la formule de la question 2 doit être adaptée si λ<0.

### Exercice 5 — Un supremum non atteint
Soit A={x∈R : 0≤x<2}.
1. Montrer que 2 est un majorant.
2. Montrer qu'aucun réel strictement inférieur à 2 n'est un majorant.
3. En déduire sup A et préciser si A possède un maximum.

## Partie B — Complétude et densité

### Exercice 6 — Rationnels et irrationnels
1. Rappeler pourquoi √2 est irrationnel.
2. Considérer A={q∈Q : q≥0 et q²<2}. Expliquer pourquoi A est non vide et majoré dans Q.
3. Montrer, par contradiction ou par une preuve détaillée, que A ne possède pas de supremum rationnel.
4. Quelle propriété de R permet de conclure que sup A existe dans R ?

### Exercice 7 — Propriété archimédienne
Démontrer que pour tout ε>0, il existe n∈N tel que 1/n<ε. En déduire que 1/n→0.

### Exercice 8 — Densité de Q
Soient a,b∈R avec a<b.
1. Utiliser la propriété archimédienne pour choisir n∈N tel que 1/n<b−a.
2. Montrer qu'il existe un entier m tel que na<m<nb.
3. En déduire l'existence d'un rationnel q=m/n dans (a,b).
*Indication : traiter avec soin le choix de m à partir de la partie entière de na.*

### Exercice 9 — Intervalles emboîtés
On pose Iₙ=[1−1/n, 2+1/n] pour n≥1.
1. Vérifier que les intervalles sont emboîtés.
2. Calculer leur intersection.
3. Expliquer pourquoi l'intersection n'est pas réduite à un point.
4. Quelle hypothèse supplémentaire du théorème des intervalles emboîtés manque-t-il ?

## Partie C — Suites de Cauchy

### Exercice 10 — Convergente implique Cauchy
Rédiger une preuve complète, avec quantificateurs, du fait que toute suite réelle convergente est de Cauchy.

### Exercice 11 — Cauchy et bornitude
Démontrer que toute suite réelle de Cauchy est bornée.
*Indication : appliquer la définition avec ε=1, puis traiter séparément le nombre fini de premiers termes.*

### Exercice 12 — Écart consécutif insuffisant
Soit Hₙ=1+1/2+…+1/n.
1. Calculer Hₙ₊₁−Hₙ et montrer que cet écart tend vers 0.
2. Rappeler pourquoi Hₙ diverge.
3. Conclure que |uₙ₊₁−uₙ|→0 ne suffit pas à prouver que la suite est de Cauchy ou convergente.

### Exercice 13 — Approximations rationnelles de √2
Pour n≥1, poser uₙ=⌊10ⁿ√2⌋/10ⁿ.
1. Montrer que uₙ∈Q.
2. Établir 0≤√2−uₙ<10⁻ⁿ.
3. Montrer que (uₙ) est de Cauchy.
4. Expliquer pourquoi elle ne converge pas dans Q.
5. Dans quel ensemble converge-t-elle ?

### Exercice 14 — Une suite de Cauchy dans Z
Soit (uₙ) une suite d'entiers relatifs qui est de Cauchy pour la distance usuelle.
1. Appliquer la définition avec ε=1.
2. Montrer qu'à partir d'un certain rang, tous les termes sont égaux.
3. En déduire que la suite est stationnaire à partir d'un certain rang et converge vers un entier.

## Partie D — Synthèse

### Exercice 15 — Critère de Cauchy et complétude
Énoncer le critère de Cauchy dans R. Expliquer pourquoi le sens « Cauchy implique convergente » ne peut pas être appliqué automatiquement à une suite de rationnels si l'on exige une limite rationnelle.

### Exercice 16 — Problème de calcul numérique
Un algorithme produit des approximations xₙ d'une quantité inconnue. On observe que |xₙ₊₁−xₙ|<10⁻⁶ à partir de n=500.
1. Cette information prouve-t-elle que (xₙ) est de Cauchy ? Pourquoi ?
2. Quelle condition sur toutes les paires de termes serait nécessaire ?
3. Quelles informations supplémentaires seraient utiles pour établir une convergence et une borne d'erreur ?
4. Distinguer convergence, précision et stabilité numérique.

---

# Corrigé détaillé

## Exercice 1
1. A=(0,1) est borné, inf A=0 et sup A=1. Aucun des deux n'appartient à A : ni minimum ni maximum.
2. B=[−2,3] est borné ; inf B=min B=−2 et sup B=max B=3.
3. C={1/n:n≥1} est borné ; inf C=0 et sup C=1. Le maximum vaut 1 (atteint pour n=1), mais il n'y a pas de minimum.
4. D=[4,+∞) est minoré par 4, inf D=min D=4, mais non majoré et donc non borné.
5. E={n∈Z:n≤0} est majoré par 0 et sup E=max E=0 ; il n'est pas minoré.

## Exercice 2
Si s=sup A, alors s majore A. Pour tout ε>0, s−ε ne peut pas être un majorant, car il est strictement inférieur au plus petit majorant. Il existe donc aε∈A tel que aε>s−ε.
Réciproquement, supposons les deux propriétés. La première dit que s est un majorant. Si M<s, choisir ε=(s−M)/2>0. La seconde fournit aε∈A tel que aε>s−ε=(s+M)/2>M. Donc M n'est pas un majorant. Aucun réel strictement inférieur à s n'est majorant ; s est le supremum.

## Exercice 3
Comme s est supremum, c'est un majorant minimal ; puisque t est un majorant, s≤t. De même, t≤s. Donc s=t.

## Exercice 4
1. Posons s=sup A. Pour tout a∈A, a≤s, donc a+c≤s+c : s+c majore A+c. Si M est un majorant de A+c, alors M−c majore A ; donc s≤M−c, soit s+c≤M. Ainsi sup(A+c)=s+c.
2. Pour λ>0, la multiplication conserve l'ordre. λs majore λA. Si M majore λA, M/λ majore A, donc s≤M/λ et λs≤M. Ainsi sup(λA)=λs.
3. Si λ<0, la multiplication inverse l'ordre : le supremum de λA est λ inf A, sous réserve que A soit minoré. Le supremum et l'infimum sont échangés.

## Exercice 5
2 est un majorant. Soit M<2. Si M<0, n'importe quel élément de A convient ; si 0≤M<2, choisir x=(M+2)/2. Alors M<x<2, donc x∈A et M ne majore pas A. Ainsi sup A=2. Comme 2∉A, A n'a pas de maximum.

## Exercice 6
1. Supposons √2=p/q avec p,q entiers premiers entre eux et q≠0. Alors p²=2q², donc p est pair ; écrire p=2k donne q²=2k², donc q est pair. Cela contredit le fait que p et q sont premiers entre eux.
2. 1∈A car 1²<2. Tout q∈A vérifie q<2, donc 2 est un majorant rationnel.
3. Supposons s=sup_Q A. Si s²<2, par continuité de x↦x² ou par développement algébrique, il existe un rationnel r>s suffisamment proche de s avec r²<2 ; r∈A, contradiction au fait que s majore A. Si s²>2, on peut choisir un rationnel r<s suffisamment proche de s avec r²>2 ; alors tout q∈A vérifie q<r, donc r est un majorant plus petit que s, contradiction à la minimalité de s. Il faudrait donc s²=2, impossible puisque s est rationnel. A n'a pas de supremum dans Q.
4. La propriété de la borne supérieure dans R garantit que tout ensemble non vide majoré de R possède un supremum réel. Le supremum de A considéré comme sous-ensemble de R est √2.

## Exercice 7
Par la propriété archimédienne, pour tout 1/ε>0, il existe n∈N tel que n>1/ε. Donc 1/n<ε. C'est exactement la définition de 1/n→0.

## Exercice 8
Choisir n tel que n(b−a)>1. Par la propriété de la partie entière, il existe m entier avec na<m≤na+1. Comme na+1<nb, on obtient na<m<nb. Ainsi a<m/n<b et m/n est rationnel. (Selon le cas où na est entier, on peut choisir m=⌊na⌋+1 ; l'inégalité stricte reste satisfaite grâce à n(b−a)>1.)

## Exercice 9
Pour tout n≥1, 1−1/(n+1)>1−1/n et 2+1/(n+1)<2+1/n ; donc Iₙ₊₁⊂Iₙ. L'intersection est [1,2]. Elle n'est pas réduite à un point. La condition manquante est que la longueur des intervalles tende vers 0 ; ici elle vaut 1+2/n et tend vers 1.

## Exercice 10
Soit ε>0. Puisque uₙ→L, il existe N tel que n≥N implique |uₙ−L|<ε/2. Pour m,n≥N :
|uₙ−uₘ|≤|uₙ−L|+|uₘ−L|<ε.
C'est la définition d'une suite de Cauchy.

## Exercice 11
Puisque (uₙ) est de Cauchy, pour ε=1 il existe N tel que m,n≥N impliquent |uₙ−uₘ|<1. Fixons m=N. Alors, pour n≥N, |uₙ|≤|uₙ−u_N|+|u_N|<1+|u_N|. Les termes à partir de N sont bornés. Les N premiers termes forment un ensemble fini, donc sont également bornés. La suite entière est bornée.

## Exercice 12
Hₙ₊₁−Hₙ=1/(n+1)→0. Pourtant, la série harmonique diverge : on peut grouper les termes par blocs, chaque bloc 1/2+1/3+1/4+1/5, puis 1/6+…+1/9, etc., et montrer que chaque bloc à partir d'un certain rang contribue au moins une constante positive (par exemple 1/2). Les sommes partielles ne sont donc pas bornées et ne convergent pas. Les écarts consécutifs tendant vers zéro ne suffisent pas.

## Exercice 13
1. La partie entière est entière et 10ⁿ est entier non nul, donc uₙ est rationnel.
2. Pour tout y réel, ⌊y⌋≤y<⌊y⌋+1. En prenant y=10ⁿ√2 et en divisant par 10ⁿ, on obtient uₙ≤√2<uₙ+10⁻ⁿ.
3. Pour m,n≥N, |uₙ−uₘ|≤|uₙ−√2|+|√2−uₘ|<10⁻ⁿ+10⁻ᵐ≤2·10⁻ᴺ. Choisir N suffisamment grand pour que 2·10⁻ᴺ<ε.
4. Si la suite convergeait dans Q vers q, elle convergerait aussi dans R vers q. Or sa limite réelle est √2. Par unicité de la limite, q=√2, contradiction puisque q∈Q et √2∉Q.
5. Elle converge dans R vers √2.

## Exercice 14
Avec ε=1, il existe N tel que m,n≥N implique |uₙ−uₘ|<1. Or uₙ et uₘ sont entiers ; leur différence est un entier. Le seul entier de valeur absolue strictement inférieure à 1 est 0. Donc uₙ=uₘ pour tous m,n≥N. La suite est constante à partir du rang N et converge vers cette valeur entière.

## Exercice 15
Le critère de Cauchy dans R affirme qu'une suite réelle converge dans R si et seulement si elle est de Cauchy. Dans Q, la propriété réciproque est fausse : les approximations rationnelles de √2 forment une suite de Cauchy dans Q mais leur limite réelle n'appartient pas à Q. La complétude dépend donc de l'ensemble dans lequel on exige que la limite se trouve.

## Exercice 16
1. Non. Une borne sur les écarts entre termes consécutifs, même à partir du rang 500, ne contrôle pas la distance entre xₙ et xₘ pour deux indices arbitrairement éloignés.
2. Il faudrait montrer que pour tout ε>0, il existe N tel que pour tous m,n≥N, |xₙ−xₘ|<ε.
3. Une preuve de contraction, une estimation a priori de l'erreur, un encadrement par une suite convergente, ou un théorème de convergence adapté à l'algorithme. Il faut connaître les hypothèses du procédé et le domaine où il est appliqué.
4. **Convergence** : les itérés tendent vers une limite. **Précision** : l'écart à la valeur exacte est inférieur à une tolérance connue ou estimée. **Stabilité** : de petites perturbations des données ou des calculs n'entraînent pas de grandes perturbations du résultat. Ces notions sont liées mais non équivalentes.

## Barème indicatif
- Partie A : 25 points.
- Partie B : 25 points.
- Partie C : 30 points.
- Partie D : 20 points.

Seuil pédagogique proposé : 80/100, avec reprise obligatoire de toute confusion entre supremum et maximum, entre densité et complétude, ou entre écart consécutif et condition de Cauchy. Ce seuil n'est pas une norme académique universelle.
