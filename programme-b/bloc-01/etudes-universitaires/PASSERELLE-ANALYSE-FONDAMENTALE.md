# Passerelle vers l’analyse mathématique — Fondements

**Statut :** extension préparatoire du Bloc 1 (Programme B).  
**Niveau visé :** transition lycée avancé / première année universitaire, avec formalisation de niveau licence.  
**Charge indicative :** 18 à 24 heures.  
**Prérequis :** F01 à F07, calcul algébrique, intervalles, fonctions élémentaires, valeur absolue.  
**Périmètre :** logique, rédaction de preuves, suites réelles, limites de suites, limites de fonctions et continuité. Les dérivées et intégrales ne sont pas encore étudiées ici.

> Cette passerelle ne constitue pas un nouveau Bloc 2 et ne certifie pas la maîtrise du Bloc 1. Elle prépare le passage du calcul opératoire au raisonnement d’analyse.

## 1. Compétences visées

À l’issue du parcours, l’étudiant doit pouvoir :

1. traduire correctement les quantificateurs « pour tout » et « il existe » ;
2. distinguer implication, réciproque, contraposée et équivalence ;
3. rédiger une preuve directe, par contraposée, par contradiction et par récurrence ;
4. construire un contre-exemple pertinent ;
5. définir une suite réelle et étudier sa monotonie, son bornage et sa convergence ;
6. utiliser la définition epsilon-N de la convergence d’une suite ;
7. comprendre la définition epsilon-delta d’une limite de fonction ;
8. distinguer limite, valeur de la fonction et continuité ;
9. appliquer les théorèmes de convergence et de continuité en vérifiant leurs hypothèses.

## 2. Logique mathématique : le langage des énoncés

### 2.1 Proposition et valeur de vérité

Une proposition est un énoncé auquel on peut attribuer une valeur de vérité, vraie ou fausse. « 7 est premier » est une proposition vraie ; « 9 est premier » est une proposition fausse. Une expression contenant une variable libre, telle que « x > 2 », n’est pas encore une proposition tant que x n’est pas fixé ou quantifié.

Les connecteurs usuels sont :
- négation : non P ;
- conjonction : P et Q ;
- disjonction inclusive : P ou Q ;
- implication : si P, alors Q ;
- équivalence : P si et seulement si Q.

L’implication P ⇒ Q n’affirme pas que P est vraie. Elle affirme seulement qu’aucun cas où P est vraie et Q fausse n’est admissible.

### 2.2 Quantificateurs

- ∀x ∈ E, P(x) : pour chaque élément x de E, P(x) est vraie.
- ∃x ∈ E tel que P(x) : au moins un élément de E vérifie P.
- ∃!x ∈ E tel que P(x) : il existe un unique élément.

La négation échange les quantificateurs :
- non (∀x ∈ E, P(x)) équivaut à ∃x ∈ E tel que non P(x) ;
- non (∃x ∈ E, P(x)) équivaut à ∀x ∈ E, non P(x).

**Exemple.** La négation de « pour tout réel x, x² ≥ 0 » est « il existe un réel x tel que x² < 0 ». Il ne suffit pas d’écrire « pour tout x, x² < 0 » : ce serait une autre proposition.

### 2.3 Implication, réciproque et contraposée

Pour P ⇒ Q :
- la réciproque est Q ⇒ P ; elle n’est pas automatiquement vraie ;
- la contraposée est non Q ⇒ non P ; elle est logiquement équivalente à P ⇒ Q.

**Exemple.** Si n est divisible par 4, alors n est pair. La réciproque « si n est pair, alors n est divisible par 4 » est fausse (contre-exemple n = 2). La contraposée « si n n’est pas pair, alors n n’est pas divisible par 4 » est vraie.

## 3. Méthodes de démonstration

### 3.1 Preuve directe

Pour démontrer « si P alors Q », on suppose P et on déduit Q par des étapes justifiées.

**Exemple.** Si n est pair, il existe k ∈ Z tel que n = 2k. Alors n² = 4k² = 2(2k²), donc n² est pair.

### 3.2 Preuve par contraposée

On démontre non Q ⇒ non P. Cette méthode est utile lorsque la négation de la conclusion est plus facile à exploiter.

### 3.3 Preuve par contradiction

On suppose la négation de la conclusion, puis on déduit une contradiction avec une hypothèse ou un résultat établi. La contradiction doit être explicite.

### 3.4 Contre-exemple

Pour réfuter une affirmation universelle « pour tout x, P(x) », un seul x admissible pour lequel P(x) est fausse suffit. Un contre-exemple doit respecter le domaine et toutes les hypothèses.

### 3.5 Récurrence

Pour prouver P(n) pour tout entier n ≥ n₀ :
1. **Initialisation :** vérifier P(n₀).
2. **Hérédité :** supposer P(n) vraie pour un n arbitraire ≥ n₀ et démontrer P(n+1).
3. **Conclusion :** par le principe de récurrence, P(n) est vraie pour tout n ≥ n₀.

**Exemple.** Pour n ≥ 1, 1 + 2 + … + n = n(n+1)/2.
- Initialisation : n=1 donne 1=1.
- Hérédité : si la somme jusqu’à n vaut n(n+1)/2, alors la somme jusqu’à n+1 vaut n(n+1)/2 + (n+1) = (n+1)(n+2)/2.
- La formule est donc vraie pour tout n ≥ 1.

### 3.6 Existence et unicité

Une preuve d’existence construit un objet ou démontre qu’il doit exister. Une preuve d’unicité suppose deux objets satisfaisant la propriété et montre qu’ils sont égaux. Prouver l’existence ne prouve pas l’unicité.

## 4. Suites réelles

### 4.1 Définition

Une suite réelle est une fonction u : N → R. On note uₙ son terme d’indice n. Une suite peut être définie explicitement (uₙ = 1/(n+1)), par récurrence (uₙ₊₁ = g(uₙ)) ou par une propriété.

Il faut distinguer la suite (uₙ) de son terme uₙ et de l’ensemble de ses valeurs.

### 4.2 Monotonie et bornes

- croissante : uₙ₊₁ ≥ uₙ pour tout n ;
- strictement croissante : uₙ₊₁ > uₙ ;
- décroissante : uₙ₊₁ ≤ uₙ ;
- majorée : il existe M ∈ R tel que uₙ ≤ M pour tout n ;
- minorée : il existe m ∈ R tel que uₙ ≥ m pour tout n ;
- bornée : majorée et minorée.

Pour une suite définie par récurrence, l’étude de la monotonie commence souvent par le signe de uₙ₊₁ − uₙ. Pour le bornage, on peut établir un invariant par récurrence.

### 4.3 Convergence : définition epsilon-N

La suite (uₙ) converge vers L ∈ R si :

**pour tout ε > 0, il existe N ∈ N tel que, pour tout n ≥ N, |uₙ − L| < ε.**

Symboliquement : ∀ε>0, ∃N∈N, ∀n≥N : |uₙ−L|<ε.

L’ordre des quantificateurs est essentiel : N peut dépendre de ε, mais pas de n après le seuil N.

**Exemple :** uₙ = 1/n pour n ≥ 1 converge vers 0. Soit ε>0. Choisir un entier N > 1/ε. Pour tout n ≥ N, 0 < 1/n ≤ 1/N < ε. Donc uₙ → 0.

### 4.4 Unicité de la limite

Une suite ne peut pas converger vers deux limites distinctes.

**Preuve.** Supposons uₙ → L et uₙ → M avec L ≠ M. Posons ε = |L−M|/3 > 0. Pour n assez grand, |uₙ−L|<ε et |uₙ−M|<ε. Par inégalité triangulaire, |L−M| ≤ |L−uₙ|+|uₙ−M| < 2ε = 2|L−M|/3, contradiction. Donc L=M.

### 4.5 Théorèmes fondamentaux sur les suites

- Toute suite convergente est bornée.
- Toute suite croissante et majorée converge dans R.
- Toute suite décroissante et minorée converge dans R.
- Si uₙ → L et vₙ → M, alors uₙ+vₙ → L+M et uₙvₙ → LM.
- Si vₙ → M ≠ 0, alors vₙ est non nul à partir d’un certain rang et uₙ/vₙ → L/M lorsque uₙ → L.

La propriété « croissante et majorée implique convergente » dépend de la complétude de R. Elle n’est pas vraie dans Q avec sa structure usuelle : une suite rationnelle croissante peut approcher √2 sans avoir de limite rationnelle.

### 4.6 Exemple : suite récurrente

Considérons u₀ = 1 et uₙ₊₁ = (uₙ+2)/2.
On montre par récurrence que 1 ≤ uₙ ≤ 2. De plus,
uₙ₊₁ − uₙ = (2−uₙ)/2 ≥ 0,
donc la suite est croissante. Elle est majorée par 2, donc converge vers une limite L. Par passage à la limite dans la relation de récurrence, L=(L+2)/2, donc L=2.

Attention : le passage à la limite dans une relation fonctionnelle exige la continuité de la fonction concernée ou une justification équivalente. Ici g(x)=(x+2)/2 est continue.

## 5. Limites de fonctions

### 5.1 Idée et définition

Dire que lim(x→a) f(x)=L signifie que f(x) devient aussi proche que souhaité de L lorsque x est suffisamment proche de a, sans exiger x=a.

Définition epsilon-delta : pour tout ε>0, il existe δ>0 tel que, pour tout x appartenant au domaine de f, si 0<|x−a|<δ, alors |f(x)−L|<ε.

Le terme 0<|x−a| exclut le point a : la limite dépend du comportement au voisinage, non nécessairement de f(a).

### 5.2 Exemple epsilon-delta

Montrer que lim(x→2)(3x+1)=7.
Soit ε>0. On veut |(3x+1)−7|<ε, soit 3|x−2|<ε. Il suffit de choisir δ=ε/3. Si 0<|x−2|<δ, alors |3x+1−7|=3|x−2|<3δ=ε.

### 5.3 Limites à gauche et à droite

Une limite bilatérale existe et vaut L si les limites à gauche et à droite existent et valent toutes deux L. Si elles diffèrent, la limite bilatérale n’existe pas.

Exemple : f(x)=−1 si x<0 et f(x)=1 si x≥0. En 0, la limite à gauche vaut −1 et celle à droite vaut 1 ; la limite bilatérale n’existe pas, même si f(0)=1.

### 5.4 Outils de calcul

Les lois usuelles des limites permettent de traiter sommes, produits, quotients (si la limite du dénominateur est non nulle), puissances et compositions lorsque les hypothèses sont satisfaites. La factorisation et la multiplication par le conjugué sont des techniques algébriques, mais elles ne dispensent jamais de vérifier le domaine et les conditions d’application.

**Exemple.** Pour x≠1, (x²−1)/(x−1) = x+1. La limite en 1 vaut donc 2, bien que l’expression initiale ne soit pas définie en 1.

## 6. Continuité

### 6.1 Continuité en un point

Une fonction f est continue en a si :
1. f(a) est définie ;
2. lim(x→a) f(x) existe ;
3. lim(x→a) f(x)=f(a).

Ces trois conditions sont nécessaires. Un trou, un saut ou une divergence peut empêcher la continuité.

### 6.2 Continuité et suites

Une caractérisation séquentielle : f est continue en a si, pour toute suite (xₙ) de son domaine qui converge vers a, la suite f(xₙ) converge vers f(a). Cette caractérisation relie la topologie des réels à la notion de limite de fonction.

### 6.3 Théorèmes majeurs

- Somme, produit et composition de fonctions continues : continues sur les domaines où les opérations sont définies.
- Quotient : continu là où le dénominateur ne s’annule pas.
- **Théorème des valeurs intermédiaires (TVI) :** si f est continue sur [a,b], toute valeur comprise entre f(a) et f(b) est atteinte au moins une fois.
- **Théorème des bornes atteintes :** une fonction continue sur un segment [a,b] est bornée et atteint ses minimum et maximum.

Le TVI garantit l’existence, pas nécessairement l’unicité, d’une solution. Pour établir l’unicité, il faut une information supplémentaire, par exemple la stricte monotonie.

### 6.4 Exemple d’application

Soit f(x)=x³+x−1 sur [0,1]. La fonction est continue, f(0)=−1 et f(1)=1. Le TVI garantit l’existence d’au moins un c∈(0,1) tel que f(c)=0. En outre, f est strictement croissante (on peut le montrer sans dérivée : si y>x, alors f(y)−f(x)=(y−x)(y²+xy+x²+1)>0). La solution est donc unique.

## 7. Applications aux sciences quantitatives

- **Données et algorithmes :** une tolérance numérique doit être interprétée comme un voisinage, non comme une égalité exacte.
- **Modélisation :** la continuité d’une fonction de coût ou de risque est une hypothèse mathématique, pas une vérité automatique sur le phénomène.
- **Convergence numérique :** une suite d’itérés peut converger, diverger ou osciller ; observer quelques itérations ne démontre pas la convergence.
- **Statistique :** les limites et la convergence forment le langage théorique qui sera nécessaire pour étudier les estimateurs et leurs propriétés asymptotiques. Cette passerelle n’introduit pas encore les théorèmes probabilistes de convergence.

## 8. Erreurs à éviter

1. Inverser les quantificateurs dans une définition.
2. Confondre implication et réciproque.
3. Considérer quelques exemples numériques comme une preuve générale.
4. Démontrer la monotonie sans préciser l’indice et le domaine.
5. Affirmer qu’une suite bornée converge : c’est faux en général (uₙ=(−1)ⁿ).
6. Confondre la limite de f en a et la valeur f(a).
7. Oublier le caractère strict 0<|x−a| dans la définition d’une limite.
8. Appliquer le TVI sans continuité sur tout l’intervalle.
9. Déduire l’unicité d’une solution du seul TVI.
10. Passer à la limite dans une récurrence sans justifier la continuité ou la stabilité de l’opération.

## 9. Plan de travail recommandé

| Séquence | Travail | Durée indicative |
|---|---|---:|
| 1 | Logique, quantificateurs, négations | 2 h |
| 2 | Preuves directes, contraposée, contradiction | 3 h |
| 3 | Récurrence et contre-exemples | 2 h |
| 4 | Suites, monotonie et bornage | 3 h |
| 5 | Convergence epsilon-N et théorèmes | 3 h |
| 6 | Limites epsilon-delta | 3 h |
| 7 | Continuité et théorèmes | 3 h |
| 8 | Exercices de synthèse et oral | 2 à 5 h |

## 10. Bibliographie et ressources vérifiables

1. Richard Hammack, *Book of Proof*, 3e édition, notamment chapitres 2 et 4–10 (logique, quantificateurs, preuves, récurrence), et chapitre 13 (preuves en calcul, limites, continuité, suites). Livre librement consultable/téléchargeable depuis le site de l’auteur : https://richardhammack.github.io/BookOfProof/
2. American Institute of Mathematics, Open Textbook Initiative, notice d’évaluation de *Book of Proof* : https://textbooks.aimath.org/textbooks/approved-textbooks/hammack/
3. OpenStax, *Calculus Volume 1*, section 2.4, “Continuity” : https://openstax.org/books/calculus-volume-1/pages/2-4-continuity
4. OpenStax, *Calculus Volume 1*, chapitre 2, “Limits” et “The Limit Laws” : https://openstax.org/books/calculus-volume-1/pages/2-key-concepts
5. MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2005, notes de cours : https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2005/pages/lecture-notes/

Les références 1–2 soutiennent prioritairement la logique et les démonstrations ; les références 3–5 fournissent une progression universitaire sur limites et continuité. Le présent cours est une synthèse pédagogique originale : il ne reproduit pas ces ouvrages et ne prétend pas couvrir toute l’analyse réelle.

## 11. Critères de maîtrise

La passerelle est considérée comme acquise lorsque l’étudiant peut :
- traduire et nier correctement un énoncé avec quantificateurs ;
- rédiger au moins une preuve directe, une contraposée et une récurrence ;
- produire un contre-exemple valide ;
- démontrer la convergence d’une suite simple par epsilon-N ;
- établir une limite de fonction par epsilon-delta dans un cas affine ;
- vérifier les trois conditions de continuité ;
- citer les hypothèses du TVI et distinguer existence et unicité.

Seuil pédagogique proposé : 80 % aux exercices, sans erreur critique sur les quantificateurs, la définition de convergence ou les hypothèses des théorèmes. Ce seuil est une règle interne de progression, pas une norme universitaire universelle.
