# Exercices — Passerelle vers l’analyse mathématique

**Consigne générale :** rédiger les raisonnements. Une réponse numérique sans justification ne valide pas la compétence. Les exercices 1 à 12 sont progressifs ; les exercices 13 à 16 sont des problèmes de synthèse.

## Partie A — Logique et preuves

### Exercice 1 — Négation des quantificateurs
Écrire la négation exacte de chacune des propositions :
1. Pour tout réel x, x²+1>0.
2. Il existe un réel x tel que x²=2.
3. Pour tout ε>0, il existe N∈N tel que, pour tout n≥N, |uₙ−L|<ε.

### Exercice 2 — Implication et réciproque
On considère, pour n entier, l'affirmation : « si n est divisible par 6, alors n est divisible par 3 ».
1. Démontrer l'affirmation.
2. Écrire sa réciproque.
3. La réciproque est-elle vraie ? Justifier par un contre-exemple si nécessaire.
4. Écrire la contraposée.

### Exercice 3 — Preuve directe
Démontrer que la somme de deux entiers impairs est paire.

### Exercice 4 — Contraposée
Démontrer que si n² est impair, alors n est impair, pour n∈Z.

### Exercice 5 — Récurrence
Démontrer, pour tout entier n≥1 :
1+3+5+…+(2n−1)=n².

### Exercice 6 — Contre-exemple
Réfuter les affirmations suivantes :
1. Toute suite bornée converge.
2. Si ab=ac, alors b=c.
3. Toute fonction qui possède une limite en a est continue en a.

Pour chaque cas, donner un exemple respectant le domaine et expliquer précisément l'échec.

## Partie B — Suites réelles

### Exercice 7 — Monotonie et bornage
Soit uₙ=3−2/(n+1), n≥0.
1. Calculer u₀, u₁, u₂.
2. Étudier la monotonie.
3. Montrer que la suite est majorée et minorée.
4. Conjecturer puis démontrer sa limite.

### Exercice 8 — Suite alternée
Soit vₙ=(−1)ⁿ.
1. Montrer que la suite est bornée.
2. Examiner les sous-suites (v₂ₙ) et (v₂ₙ₊₁).
3. En déduire que (vₙ) ne converge pas.

### Exercice 9 — Définition epsilon-N
Démontrer directement que uₙ=5/(n+1) converge vers 0. Pour un ε>0 arbitraire, proposer un entier N adapté et conclure.

### Exercice 10 — Récurrence et convergence
Soit u₀=0 et uₙ₊₁=(uₙ+4)/2.
1. Montrer par récurrence que 0≤uₙ≤4.
2. Étudier la monotonie.
3. En déduire la convergence.
4. Déterminer la limite en justifiant le passage à la limite.

### Exercice 11 — Unicité de la limite
Rédiger une preuve complète de l'unicité de la limite d'une suite réelle, en utilisant l'inégalité triangulaire et les quantificateurs.

## Partie C — Limites de fonctions et continuité

### Exercice 12 — Définition epsilon-delta
Démontrer avec la définition formelle que :
lim(x→−1)(2x+5)=3.

### Exercice 13 — Limite et valeur
On définit f par f(x)=(x²−4)/(x−2) pour x≠2 et f(2)=7.
1. Simplifier l'expression pour x≠2.
2. Calculer lim(x→2)f(x).
3. La fonction est-elle continue en 2 ? Justifier avec les trois conditions.

### Exercice 14 — Limites latérales
Soit f(x)=−2 si x<1 et f(x)=3 si x≥1.
1. Calculer la limite à gauche en 1.
2. Calculer la limite à droite en 1.
3. La limite bilatérale existe-t-elle ?
4. f est-elle continue en 1 ?

### Exercice 15 — Théorème des valeurs intermédiaires
Soit g(x)=x³+x−1 sur [0,1].
1. Vérifier la continuité.
2. Calculer g(0) et g(1).
3. Conclure sur l'existence d'une racine dans (0,1).
4. Démontrer que cette racine est unique sans utiliser de dérivée.

### Exercice 16 — Problème de synthèse : convergence d'un algorithme
On définit x₀=1 et xₙ₊₁=(xₙ+3)/2.
1. Calculer les quatre premiers termes.
2. Montrer que si xₙ≤3, alors xₙ₊₁≤3.
3. Montrer que xₙ₊₁−xₙ=(3−xₙ)/2.
4. Établir par récurrence que la suite est croissante et majorée par 3.
5. Conclure à la convergence.
6. Déterminer sa limite.
7. Expliquer pourquoi ce raisonnement établit la convergence de la suite mathématique, mais ne suffit pas à garantir qu'un algorithme numérique quelconque converge.

---

# Corrigé détaillé

## Exercice 1
1. Il existe x∈R tel que x²+1≤0.
2. Pour tout x∈R, x²≠2.
3. Il existe ε>0 tel que, pour tout N∈N, il existe n≥N avec |uₙ−L|≥ε.

Dans la troisième négation, l'ordre des quantificateurs est inversé successivement et l'inégalité stricte devient son complément.

## Exercice 2
1. Si n=6k, alors n=3(2k), donc n est divisible par 3.
2. Réciproque : si n est divisible par 3, alors n est divisible par 6.
3. Faux : n=3 est divisible par 3 mais pas par 6.
4. Contraposée : si n n'est pas divisible par 3, alors n n'est pas divisible par 6. Elle est équivalente à l'énoncé initial.

## Exercice 3
Soient a et b deux entiers impairs. Il existe k,l∈Z tels que a=2k+1 et b=2l+1. Alors a+b=2(k+l+1), qui est pair.

## Exercice 4
On démontre la contraposée : si n est pair, alors n² est pair. Si n=2k, alors n²=4k²=2(2k²), donc n² est pair. La contraposée étant équivalente à l'implication initiale, le résultat est démontré.

## Exercice 5
Initialisation : pour n=1, le membre de gauche vaut 1 et le membre de droite vaut 1.
Hérédité : supposons 1+3+…+(2n−1)=n². Alors :
1+3+…+(2n−1)+(2(n+1)−1)
= n²+2n+1
= (n+1)².
La propriété est vraie pour tout n≥1 par récurrence.

## Exercice 6
1. uₙ=(−1)ⁿ est bornée entre −1 et 1, mais ne converge pas : les sous-suites paires et impaires ont des limites distinctes.
2. Prendre a=0, b=1, c=2 : ab=ac=0 mais b≠c. L'annulation de a empêche la simplification.
3. Définir f(x)=0 pour x≠0 et f(0)=1. La limite en 0 vaut 0, mais f(0)=1 ; f n'est pas continue en 0.

## Exercice 7
u₀=1, u₁=2, u₂=7/3.
Pour tout n≥0 :
uₙ₊₁−uₙ = 3−2/(n+2)−(3−2/(n+1))
= 2/((n+1)(n+2)) >0.
La suite est strictement croissante. Comme n+1≥1, 0<2/(n+1)≤2, donc 1≤uₙ<3. Elle est bornée et croissante, donc convergente. Puis 2/(n+1)→0, donc uₙ→3.

## Exercice 8
−1≤vₙ≤1, donc la suite est bornée. Mais v₂ₙ=1 pour tout n et v₂ₙ₊₁=−1 pour tout n. Ces deux sous-suites convergent vers des limites différentes. Une suite convergente aurait toutes ses sous-suites convergentes vers la même limite ; contradiction. La suite ne converge pas.

## Exercice 9
Soit ε>0. Choisir N entier tel que N+1>5/ε. Pour n≥N :
|uₙ−0|=5/(n+1)≤5/(N+1)<ε.
La définition epsilon-N est satisfaite ; uₙ→0.

## Exercice 10
Initialisation : u₀=0∈[0,4].
Hérédité : si 0≤uₙ≤4, alors 2≤uₙ+4≤8, donc 1≤uₙ₊₁≤4. Ainsi 0≤uₙ₊₁≤4.
De plus uₙ₊₁−uₙ=(4−uₙ)/2≥0. La suite est croissante et majorée par 4, donc converge vers L. La fonction x↦(x+4)/2 est continue ; en passant à la limite, L=(L+4)/2, donc L=4.

## Exercice 11
Supposons uₙ→L et uₙ→M. Si L≠M, posons ε=|L−M|/3. Par convergence, il existe N₁ tel que n≥N₁ implique |uₙ−L|<ε, et N₂ tel que n≥N₂ implique |uₙ−M|<ε. Pour n≥max(N₁,N₂), l'inégalité triangulaire donne :
|L−M|≤|L−uₙ|+|uₙ−M|<2ε=2|L−M|/3.
C'est impossible puisque |L−M|>0. Donc L=M.

## Exercice 12
Soit ε>0. On cherche δ>0 tel que |2x+5−3|<ε lorsque 0<|x+1|<δ. Or |2x+2|=2|x+1|. Choisir δ=ε/2. Alors 0<|x+1|<δ implique |2x+5−3|=2|x+1|<2δ=ε. La limite vaut 3.

## Exercice 13
Pour x≠2, f(x)=(x−2)(x+2)/(x−2)=x+2. Ainsi lim(x→2)f(x)=4. Mais f(2)=7. La première condition de continuité est satisfaite, la deuxième aussi, mais la troisième échoue puisque 4≠7. f n'est pas continue en 2.

## Exercice 14
La limite à gauche vaut −2 ; la limite à droite vaut 3. Elles sont différentes, donc la limite bilatérale n'existe pas. f(1)=3 ; la fonction n'est pas continue en 1.

## Exercice 15
g est un polynôme, donc continue sur [0,1]. g(0)=−1 et g(1)=1. Le TVI garantit une racine c∈(0,1).
Pour l'unicité, soient y>x. Alors :
g(y)−g(x)=y³−x³+y−x
=(y−x)(y²+xy+x²+1)>0.
Donc g est strictement croissante et ne peut avoir deux racines distinctes. La racine est unique.

## Exercice 16
Les premiers termes sont x₀=1, x₁=2, x₂=5/2, x₃=11/4.
Si xₙ≤3, alors xₙ₊₁=(xₙ+3)/2≤3. Comme x₀≤3, une récurrence donne xₙ≤3 pour tout n. De plus :
xₙ₊₁−xₙ=(3−xₙ)/2≥0.
La suite est croissante et majorée par 3 ; elle converge donc vers L. En passant à la limite dans xₙ₊₁=(xₙ+3)/2, on obtient L=(L+3)/2, donc L=3.
La preuve utilise une récurrence et le théorème de convergence des suites croissantes majorées. Un autre algorithme peut ne pas respecter ces propriétés : il faut étudier ses propres hypothèses, erreurs d'arrondi, stabilité et critère d'arrêt.

## Barème indicatif
- Exercices 1 à 6 : 30 points.
- Exercices 7 à 11 : 35 points.
- Exercices 12 à 16 : 35 points.

Un résultat correct sans justification ne reçoit qu'une partie des points. Seuil conseillé : 80/100, avec reprise obligatoire des erreurs de logique, de quantificateurs ou d'hypothèses de théorèmes.
