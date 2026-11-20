# Topologie élémentaire de la droite réelle

**Programme B · Bloc 1 · Extension préparatoire d'analyse réelle**  
**Niveau :** premier cycle universitaire, rigueur introductive.  
**Charge indicative :** 18 à 24 heures.  
**Prérequis :** ensembles, fonctions, valeur absolue, suites convergentes, complétude de R, Bolzano–Weierstrass et séries numériques.  
**Statut :** extension préparatoire du Bloc 1 ; ne constitue pas l'ouverture du Bloc 2.

---

## 1. Objectifs d'apprentissage

À la fin de ce dossier, l'apprenant doit pouvoir :

1. définir les boules ouvertes, les voisinages et les ensembles ouverts de R ;
2. caractériser les ensembles fermés par les suites convergentes ;
3. distinguer intérieur, adhérence, frontière et points isolés ;
4. reconnaître les propriétés de stabilité des ouverts et des fermés ;
5. définir la compacité et démontrer le théorème de Heine–Borel dans R ;
6. utiliser la compacité pour établir l'existence de minimum et de maximum ;
7. comprendre la connexité de la droite réelle et le rôle des intervalles ;
8. reconnaître les ensembles denses, parfaits et dénombrables ;
9. relier ces concepts aux limites, à la continuité et aux méthodes numériques.

## 2. Distance et voisinages

### 2.1 La distance sur R

Pour deux réels x et y, on définit la distance usuelle par
\[
d(x,y)=|x-y|.
\]
Elle vérifie :
- positivité : d(x,y) ≥ 0 ;
- séparation : d(x,y)=0 si et seulement si x=y ;
- symétrie : d(x,y)=d(y,x) ;
- inégalité triangulaire : d(x,z) ≤ d(x,y)+d(y,z).

La valeur absolue n'est donc pas seulement une notation algébrique : elle mesure la distance entre deux points.

### 2.2 Boule ouverte et boule fermée

Pour x dans R et r>0 :
\[
B(x,r)=\{y\in R:|y-x|<r\}=(x-r,x+r)
\]
est la boule ouverte de centre x et de rayon r.

La boule fermée est
\[
\overline B(x,r)=\{y\in R:|y-x|\leq r\}=[x-r,x+r].
\]

Un voisinage de x est un ensemble qui contient une boule ouverte centrée en x. Il n'est pas nécessairement lui-même une boule.

### 2.3 Points intérieurs

Soit A inclus dans R. Un point x est intérieur à A s'il existe r>0 tel que B(x,r) soit inclus dans A.

L'ensemble des points intérieurs est noté A° ou int(A). C'est le plus grand ouvert contenu dans A.

Exemple : pour A=[0,1], on a A°=(0,1). Les extrémités ne sont pas intérieures, car toute boule centrée en 0 ou 1 contient des points extérieurs à A.

## 3. Ensembles ouverts

### 3.1 Définition

Un ensemble U inclus dans R est ouvert si pour tout x dans U, il existe r>0 tel que
\[
(x-r,x+r)\subset U.
\]

Intuitivement, chaque point d'un ouvert dispose d'une petite marge autour de lui qui reste dans l'ensemble.

Exemples :
- (a,b) est ouvert ;
- R et l'ensemble vide sont ouverts ;
- [a,b] n'est pas ouvert si a<b ;
- [0,1) n'est pas ouvert.

### 3.2 Stabilité des ouverts

**Théorème.**
1. Toute union, même infinie, d'ouverts est ouverte.
2. Toute intersection finie d'ouverts est ouverte.
3. Une intersection infinie d'ouverts n'est pas nécessairement ouverte.

**Preuve de la première propriété.** Soit U=union des U_i, où chaque U_i est ouvert. Si x appartient à U, alors x appartient à au moins un U_j. Comme U_j est ouvert, il existe r>0 tel que B(x,r) soit inclus dans U_j, donc dans U. Ainsi U est ouvert.

**Pourquoi l'intersection doit-elle être finie ?** Les ensembles U_n=(-1/n,1/n) sont ouverts, mais leur intersection sur n≥1 vaut {0}, qui n'est pas ouvert dans R.

### 3.3 Exemples importants

- Tout intervalle ouvert est ouvert.
- Une union quelconque d'intervalles ouverts est ouverte.
- Tout ouvert non vide de R est une union d'intervalles ouverts deux à deux disjoints (les composantes ouvertes de l'ensemble).

Cette dernière propriété est spécifique à la structure de la droite réelle et prépare l'étude de la connexité.

## 4. Ensembles fermés

### 4.1 Définition par complémentaire

Un ensemble F inclus dans R est fermé si son complémentaire R\F est ouvert.

Exemples :
- [a,b] est fermé ;
- R et l'ensemble vide sont fermés ;
- (a,b) n'est pas fermé ;
- [a,b) n'est ni ouvert ni fermé ;
- un singleton {a} est fermé.

Un ensemble peut être à la fois ouvert et fermé : R et l'ensemble vide le sont. Dans R, ce sont les seuls ensembles à la fois ouverts et fermés.

### 4.2 Caractérisation séquentielle

**Théorème.** F est fermé si et seulement si toute suite (x_n) de points de F qui converge dans R a sa limite dans F.

**Sens direct.** Supposons F fermé et x_n dans F avec x_n→x. Si x n'appartenait pas à F, alors x serait dans l'ouvert R\F. Il existerait r>0 tel que B(x,r) soit incluse dans R\F. Or, par convergence, x_n appartient à B(x,r) à partir d'un certain rang, contradiction.

**Sens réciproque.** Supposons que toute suite de F convergente dans R ait sa limite dans F. Si F n'était pas fermé, son complémentaire ne serait pas ouvert. Il existerait alors x dans le complémentaire tel que toute boule B(x,1/n) rencontre F. On pourrait choisir x_n dans F avec |x_n−x|<1/n. Alors x_n→x, ce qui contredit l'hypothèse puisque x n'appartient pas à F.

Cette caractérisation est extrêmement utile : elle transforme une propriété de topologie en une propriété sur les limites de suites.

### 4.3 Stabilité des fermés

- Toute intersection, même infinie, de fermés est fermée.
- Toute union finie de fermés est fermée.
- Une union infinie de fermés n'est pas nécessairement fermée.

Exemple : chaque singleton {1/n} est fermé, mais leur union {1/n : n≥1} n'est pas fermé dans R, car la suite 1/n converge vers 0 qui n'appartient pas à cette union.

## 5. Adhérence, accumulation et frontière

### 5.1 Points d'adhérence

Un point x est adhérent à A si tout voisinage de x rencontre A. L'ensemble de ces points est l'adhérence de A, notée cl(A) ou \overline A.

Caractérisation séquentielle :
\[
x\in\overline A
\quad\Longleftrightarrow\quad
\exists (a_n)\subset A,\ a_n\to x.
\]

L'adhérence est le plus petit fermé contenant A.

Exemple : si A=(0,1), alors \overline A=[0,1].

### 5.2 Points d'accumulation

Un point x est un point d'accumulation de A si tout voisinage de x contient un point de A distinct de x.

La distinction avec l'adhérence est importante : un point isolé de A appartient à A et à son adhérence, mais n'est pas un point d'accumulation.

Exemple : pour A={0}∪{1/n : n≥1}, les points 1/n sont isolés, tandis que 0 est un point d'accumulation.

### 5.3 Frontière

La frontière de A, notée ∂A, est l'ensemble des points dont tout voisinage rencontre à la fois A et son complémentaire.

On a :
\[
\partial A=\overline A\setminus A^\circ.
\]

Exemples :
- ∂(0,1)={0,1} ;
- ∂[0,1]={0,1} ;
- ∂Q=R, car Q et son complémentaire sont tous deux denses dans R.

Un ensemble peut avoir un intérieur vide et une frontière très grande.

## 6. Densité et ensembles remarquables

### 6.1 Ensemble dense

A est dense dans R si son adhérence est R. De manière équivalente, tout intervalle ouvert non vide contient au moins un élément de A.

Exemples :
- Q est dense dans R ;
- R\Q, l'ensemble des irrationnels, est également dense dans R ;
- Z n'est pas dense dans R.

La densité ne signifie pas que l'ensemble contient tous les réels : les rationnels sont dénombrables, mais denses dans R.

### 6.2 Ensembles dénombrables et non dénombrables

Un ensemble est dénombrable s'il est fini ou si ses éléments peuvent être énumérés par les entiers naturels. Q est dénombrable ; R ne l'est pas.

Un ensemble dénombrable peut être dense. La densité et la cardinalité répondent à deux questions différentes.

### 6.3 Ensemble parfait

Un ensemble est parfait s'il est fermé et si chacun de ses points est un point d'accumulation de cet ensemble.

Exemples :
- R est parfait ;
- [0,1] est parfait ;
- l'ensemble de Cantor est parfait, fermé, non dénombrable et d'intérieur vide.

L'ensemble de Cantor montre qu'un ensemble peut être grand au sens de la cardinalité tout en ne contenant aucun intervalle.

## 7. Compacité

### 7.1 Recouvrements ouverts

Une famille (U_i) d'ouverts recouvre A si
\[
A\subset\bigcup_i U_i.
\]

Un ensemble K est compact si de tout recouvrement ouvert de K, on peut extraire un sous-recouvrement fini : il existe un nombre fini d'indices i_1,...,i_m tels que
\[
K\subset U_{i_1}\cup\cdots\cup U_{i_m}.
\]

La définition peut sembler abstraite. Elle exprime une propriété de finitude : même si l'on dispose d'une infinité d'ouverts pour couvrir K, quelques-uns suffisent toujours.

### 7.2 Théorème de Heine–Borel dans R

**Théorème.** Un sous-ensemble de R est compact si et seulement s'il est fermé et borné.

Conséquences :
- [a,b] est compact ;
- (a,b) n'est pas compact ;
- [a,+∞) n'est pas compact ;
- un fermé borné est compact ;
- un compact de R est fermé et borné.

**Attention :** fermé seul ne suffit pas, borné seul ne suffit pas.

### 7.3 Idée de preuve : compact implique fermé et borné

Si K n'était pas borné, les ouverts (-n,n), n≥1, formeraient un recouvrement de K sans sous-recouvrement fini.

Si K n'était pas fermé, il existerait une suite de points de K convergeant vers x hors de K. En utilisant des voisinages adaptés de chaque point de K et du point limite extérieur, on construirait un recouvrement ouvert sans sous-recouvrement fini. La démonstration formelle peut aussi être obtenue à partir de Bolzano–Weierstrass et de la caractérisation séquentielle de la compacité dans R.

### 7.4 Pourquoi la compacité est utile

Sur un compact, les phénomènes continus sont contrôlés globalement. La compacité permet notamment :
- d'assurer qu'une fonction continue est bornée ;
- d'assurer qu'elle atteint ses bornes ;
- d'obtenir l'uniforme continuité d'une fonction continue ;
- de garantir l'existence de sous-suites convergentes pour les suites de points du compact.

## 8. Théorèmes fondamentaux pour les fonctions continues

### 8.1 Théorème des bornes atteintes (Weierstrass)

Si K est compact et f:K→R est continue, alors f est bornée et atteint son minimum et son maximum.

Il existe donc x_min et x_max dans K tels que
\[
f(x_{\min})\leq f(x)\leq f(x_{\max})
\quad\text{pour tout }x\in K.
\]

L'hypothèse de compacité du domaine et celle de continuité sont essentielles.

Contre-exemples :
- f(x)=x sur (0,1) est continue et bornée, mais n'atteint ni son infimum 0 ni son supremum 1 ;
- f(x)=x sur R est continue, mais non bornée.

### 8.2 Image continue d'un compact

Si K est compact et f continue, alors f(K) est compact. Dans R, f(K) est donc fermé et borné.

C'est une autre formulation du contrôle global apporté par la compacité.

### 8.3 Continuité uniforme sur un compact

Si K est compact et f:K→R continue, alors f est uniformément continue : pour tout ε>0, il existe δ>0 tel que, pour tous x,y dans K,
\[
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.
\]

La différence avec la continuité ordinaire est que δ ne dépend plus du point x.

Exemple : f(x)=x² est uniformément continue sur [0,1], mais pas sur R. Sur R, les accroissements |(x+h)²−x²|=|h||2x+h| peuvent devenir arbitrairement grands pour un h fixé non nul lorsque x augmente.

## 9. Connexité et intervalles

### 9.1 Définition intuitive

Un ensemble est connexe s'il ne peut pas être séparé en deux morceaux disjoints, non vides, ouverts relativement à cet ensemble.

Sur la droite réelle, le résultat fondamental est :

**Théorème.** Les sous-ensembles connexes de R sont exactement les intervalles.

Cela inclut les intervalles ouverts, fermés, semi-ouverts, les demi-droites, R et les singletons.

Un ensemble comme [0,1]∪[2,3] n'est pas connexe : il possède une séparation entre les deux morceaux.

### 9.2 Lien avec le théorème des valeurs intermédiaires

Si I est un intervalle et f:I→R est continue, alors f(I) est un intervalle.

C'est la base topologique du théorème des valeurs intermédiaires : une fonction continue ne peut pas « sauter » une valeur entre deux valeurs prises.

La connexité fournit donc une explication structurelle à un résultat essentiel du calcul différentiel et de l'analyse.

## 10. Applications au raisonnement quantitatif

### 10.1 Optimisation

Un modèle de coût ou de risque continu sur un domaine fermé et borné possède un minimum global. Cela justifie l'existence d'une solution optimale, mais ne donne pas nécessairement sa formule ni son unicité.

### 10.2 Robustesse numérique

La continuité uniforme sur un domaine compact garantit qu'une petite erreur sur l'entrée entraîne une erreur uniformément contrôlée sur la sortie. C'est une propriété utile pour analyser des approximations numériques.

### 10.3 Modélisation statistique

Les paramètres contraints dans un compact et une fonction objectif continue fournissent un cadre où l'existence d'un optimum est assurée. Les hypothèses doivent cependant être vérifiées dans le modèle réel : fermeture du domaine, bornitude et continuité de l'objectif.

### 10.4 Limite logique

Un théorème d'existence n'est pas un algorithme. Heine–Borel ou Weierstrass garantit une propriété mathématique, mais ne fournit pas à lui seul une méthode efficace pour calculer l'optimum.

## 11. Méthode de résolution

Devant un problème de topologie :

1. préciser l'espace ambiant (ici R) ;
2. identifier l'ensemble et sa définition ;
3. traduire les notions en boules, voisinages ou suites ;
4. chercher une preuve directe ou un contre-exemple ;
5. vérifier si le théorème exige ouverture, fermeture, bornitude, compacité, continuité ou connexité ;
6. distinguer l'existence d'un objet de sa construction effective ;
7. conclure exactement ce que les hypothèses autorisent.

## 12. Erreurs fréquentes

- Dire qu'un ensemble fermé contient tous ses points d'accumulation sans préciser l'espace ambiant.
- Confondre adhérence et ensemble lui-même.
- Confondre point isolé et point d'accumulation.
- Affirmer que toute intersection d'ouverts est ouverte.
- Affirmer que toute union de fermés est fermée.
- Croire qu'un ensemble borné est compact.
- Croire qu'un ensemble fermé est compact.
- Appliquer Heine–Borel dans un espace général sans vérifier le cadre.
- Appliquer Weierstrass à une fonction non continue ou sur un domaine non compact.
- Confondre continuité et continuité uniforme.
- Confondre connexité et simple propriété d'être un intervalle dans un espace qui n'est pas R.

## 13. Parcours d'étude

| Étape | Travail | Temps indicatif |
|---|---|---:|
| 1 | Distance, boules et ouverts | 3 h |
| 2 | Fermés, caractérisation séquentielle | 3 h |
| 3 | Adhérence, frontière, densité | 3 h |
| 4 | Compacité et Heine–Borel | 4 h |
| 5 | Weierstrass et continuité uniforme | 3 h |
| 6 | Connexité, intervalles et synthèse | 2–5 h |

La maîtrise exige de savoir produire des preuves et des contre-exemples, pas seulement réciter les définitions. Les durées sont indicatives et propres à ce cursus.

## 14. Bibliographie et ressources

1. **Stephen Abbott**, *Understanding Analysis*, 2e édition, Springer. Chapitre 3, « Basic Topology of R » : ouverts et fermés, compacité, ensembles parfaits et connexes. [Sommaire et page éditeur](https://link.springer.com/book/10.1007/978-1-4939-2712-8). Référence centrale pour ce dossier.
2. **MIT OpenCourseWare**, *18.100A Real Analysis*, Fall 2020. Le cours traite les limites de fonctions, la continuité, les théorèmes du minimum/maximum et des valeurs intermédiaires, puis la continuité uniforme. [Page du cours](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/) · [Notes de cours](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/pages/lecture-notes-and-readings/).
3. **Jiří Lebl**, *Basic Analysis I: Introduction to Real Analysis*, édition libre. Ressource de lecture utilisée dans le cours du MIT. [Livre et ressources](https://www.jirka.org/ra/).
4. **Walter Rudin**, *Principles of Mathematical Analysis*, 3e édition, McGraw-Hill, 1976. Référence plus formelle, notamment pour les espaces métriques et les résultats généraux.

Les documents du Programme B sont des synthèses originales et des supports d'étude ; ils ne reproduisent pas les ouvrages cités et ne prétendent pas les remplacer.

---

**Positionnement :** ce cours approfondit la droite réelle avant l'étude plus systématique des limites de fonctions, de la continuité uniforme et du calcul différentiel. Les espaces métriques généraux, la topologie de R^n, les espaces normés et la topologie fonctionnelle seront des prolongements ultérieurs.
