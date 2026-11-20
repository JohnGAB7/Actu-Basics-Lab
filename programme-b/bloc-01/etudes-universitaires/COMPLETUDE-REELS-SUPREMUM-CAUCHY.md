# Analyse réelle — Complétude de R, supremum, infimum et suites de Cauchy

**Statut :** approfondissement de la passerelle préparatoire du Bloc 1 — Programme B.  
**Niveau visé :** première année de licence en mathématiques / sciences quantitatives.  
**Charge indicative :** 12 à 16 heures.  
**Prérequis :** définitions de convergence des suites, monotonie, bornes, valeur absolue et démonstrations élémentaires.  
**Périmètre :** structure ordonnée de R, propriété de la borne supérieure, propriété archimédienne, densité de Q, intervalles emboîtés, suites de Cauchy et complétude métrique élémentaire.

Ce document est consacré à une idée fondamentale : **les nombres réels ne présentent pas les « trous » qui existent dans les rationnels**. Cette propriété, appelée complétude, est l'une des bases logiques de l'analyse.

## 1. Pourquoi construire les réels ?

Les nombres rationnels Q permettent de mesurer des rapports et d'effectuer les opérations usuelles, mais ils ne suffisent pas à l'analyse. L'équation x²=2 n'a aucune solution rationnelle. Pourtant, il est naturel de vouloir parler d'une longueur dont le carré vaut 2, de limites qui tendent vers cette longueur, et de fonctions définies sur tout un intervalle réel.

La différence essentielle entre Q et R n'est pas que les réels seraient simplement « plus nombreux ». Elle tient à une propriété structurelle : **R est complet**, tandis que Q ne l'est pas.

Il existe plusieurs formulations équivalentes de cette complétude :
- propriété de la borne supérieure ;
- convergence de toute suite de Cauchy réelle ;
- propriété des intervalles fermés emboîtés, sous les hypothèses usuelles ;
- théorème de Bolzano–Weierstrass pour les suites réelles bornées.

Ces équivalences sont des résultats mathématiques. Elles ne doivent pas être confondues avec des définitions indépendantes sans lien.

## 2. Rappels : corps ordonné

### 2.1 Structure algébrique

Les réels sont munis de l'addition et de la multiplication. Ces opérations satisfont notamment :
- associativité et commutativité ;
- existence de 0 et de 1 ;
- existence de l'opposé de tout réel ;
- existence de l'inverse de tout réel non nul ;
- distributivité de la multiplication sur l'addition.

Ces propriétés font de R un corps.

### 2.2 Compatibilité avec l'ordre

L'ordre ≤ est compatible avec les opérations :
- si a≤b, alors a+c≤b+c ;
- si a≤b et 0≤c, alors ac≤bc.

La valeur absolue est définie par |x|=x si x≥0 et |x|=−x si x<0. Elle mesure la distance de x à 0. La distance entre x et y est |x−y|.

### 2.3 Corps ordonné et corps complet

Être un corps ordonné ne suffit pas à être R. Q est lui aussi un corps ordonné. C'est précisément la complétude qui distingue R de Q.

## 3. Majorants, minorants, supremum et infimum

Soit A une partie non vide de R.

### 3.1 Définitions

- M est un **majorant** de A si, pour tout x∈A, x≤M.
- m est un **minorant** de A si, pour tout x∈A, m≤x.
- A est majorée si elle possède au moins un majorant.
- A est minorée si elle possède au moins un minorant.
- A est bornée si elle est à la fois majorée et minorée.

Un majorant n'appartient pas nécessairement à A. De même, un minorant n'appartient pas nécessairement à A.

### 3.2 Supremum

Un réel s est le **supremum** de A, noté sup A, si :
1. s est un majorant de A ;
2. tout majorant M de A vérifie s≤M.

Le supremum est le plus petit des majorants. Il est unique lorsqu'il existe.

Une caractérisation utile est :
- s majore A ;
- pour tout ε>0, il existe a∈A tel que s−ε<a.

La seconde propriété dit qu'on peut trouver des éléments de A aussi proches de s que l'on veut par la gauche, sans nécessairement atteindre s.

### 3.3 Maximum et supremum

Le maximum de A est un élément de A qui est supérieur ou égal à tous les autres éléments. Si A possède un maximum, celui-ci est son supremum. L'inverse est faux.

**Exemple.** A=(0,1). On a sup A=1, mais A ne possède pas de maximum, car 1∉A.

Pour B=[0,1], sup B=max B=1.

### 3.4 Infimum

L'infimum inf A est le plus grand des minorants de A. Il est unique. Une caractérisation duale est :
- t minore A ;
- pour tout ε>0, il existe a∈A tel que a<t+ε.

L'infimum n'est pas nécessairement un minimum. Pour A=(0,1), inf A=0, mais 0∉A.

## 4. Axiome de complétude de R

### 4.1 Propriété de la borne supérieure

**Axiome / propriété fondamentale de R :** toute partie non vide de R qui est majorée possède un supremum dans R.

Par symétrie, toute partie non vide minorée possède un infimum dans R.

Cette propriété est souvent appelée axiome de complétude. Dans une construction axiomatique des réels, elle fait partie des propriétés qui caractérisent le corps ordonné complet.

### 4.2 Exemple : supremum d'un intervalle ouvert

Pour A=(2,5), le réel 5 est un majorant. Si M<5, on peut choisir un élément de A strictement supérieur à M (en tenant compte du fait que A contient des nombres arbitrairement proches de 5). Aucun réel inférieur à 5 ne peut donc être un majorant. Ainsi sup A=5, mais A n'a pas de maximum.

### 4.3 Exemple : ensemble non majoré

A={n∈N : n≥0} n'est pas majoré dans R. Il n'a donc pas de supremum réel. On peut écrire sup A=+∞ dans les réels étendus, mais +∞ n'est pas un nombre réel.

### 4.4 Pourquoi Q n'est pas complet

Considérons A={q∈Q : q≥0 et q²<2}. L'ensemble est non vide et majoré dans Q. S'il avait un supremum s dans Q, on pourrait montrer que s²=2 :
- s²<2 permettrait de trouver un rationnel légèrement supérieur à s dont le carré reste inférieur à 2, contredisant le fait que s est un majorant minimal ;
- s²>2 permettrait de trouver un rationnel légèrement inférieur à s qui reste un majorant, contredisant la minimalité de s.

Mais aucun rationnel ne vérifie s²=2. Donc A n'a pas de supremum dans Q. La propriété de la borne supérieure échoue dans Q.

## 5. Propriété archimédienne et densité

### 5.1 Propriété archimédienne

Pour tout réel x, il existe un entier naturel n tel que n>x.

Une formulation équivalente : pour tout ε>0, il existe n∈N tel que 1/n<ε.

Cette propriété exclut l'existence d'un entier réel infiniment grand ou d'un réel strictement positif plus petit que 1/n pour tout entier naturel n.

### 5.2 Partie entière

Pour tout réel x, il existe un unique entier k tel que k≤x<k+1. Cet entier est la partie entière de x, notée ⌊x⌋.

Elle permet notamment d'approcher un réel par des rationnels décimaux.

### 5.3 Densité de Q dans R

Entre deux réels distincts a<b, il existe au moins un rationnel q tel que a<q<b.

Plus fortement, il existe une infinité de rationnels entre a et b. Les irrationnels sont également denses dans R.

**Interprétation.** Les rationnels sont partout dans R au sens de la densité, mais ils ne remplissent pas tous les points de R. Densité et complétude sont deux notions distinctes.

## 6. Intervalles fermés emboîtés

Soit une suite d'intervalles fermés non vides Iₙ=[aₙ,bₙ] telle que Iₙ₊₁⊆Iₙ pour tout n. Si la longueur bₙ−aₙ tend vers 0, alors l'intersection de tous les Iₙ contient exactement un réel.

C'est le théorème des intervalles emboîtés.

### 6.1 Idée de démonstration

Comme les intervalles sont emboîtés, les bornes gauches aₙ forment une suite croissante et les bornes droites bₙ une suite décroissante. Elles sont bornées. La complétude permet de définir a=sup{aₙ}. On montre que aₙ≤a≤bₙ pour tout n. Ainsi a appartient à tous les intervalles. Si deux réels appartenaient à tous les intervalles, leur distance serait inférieure ou égale à bₙ−aₙ pour tout n ; cette longueur tendant vers 0, les deux réels seraient égaux.

La complétude est donc mobilisée pour garantir l'existence du point commun.

## 7. Suites de Cauchy

### 7.1 Définition

Une suite réelle (uₙ) est dite **de Cauchy** si :

Pour tout ε>0, il existe N∈N tel que, pour tous m,n≥N, |uₙ−uₘ|<ε.

La différence avec la convergence est importante :
- convergence : les termes se rapprochent d'un réel L déjà identifié ;
- Cauchy : les termes se rapprochent les uns des autres, sans que la limite soit connue à l'avance.

La condition porte sur toutes les paires m,n suffisamment grandes, pas seulement sur deux termes consécutifs.

### 7.2 Toute suite convergente est de Cauchy

**Théorème.** Toute suite convergente dans R est de Cauchy.

**Preuve.** Supposons uₙ→L. Soit ε>0. Il existe N tel que, pour n≥N, |uₙ−L|<ε/2. Pour m,n≥N, l'inégalité triangulaire donne :

|uₙ−uₘ|≤|uₙ−L|+|uₘ−L|<ε/2+ε/2=ε.

La suite est donc de Cauchy.

### 7.3 Le critère de Cauchy dans R

**Théorème de complétude séquentielle de R.** Une suite réelle converge dans R si et seulement si elle est de Cauchy.

Le sens « convergente ⇒ Cauchy » vient d'être démontré. Le sens réciproque dépend de la complétude de R. Il est faux dans Q : une suite de rationnels peut être de Cauchy sans converger vers un rationnel.

Ce critère est puissant car il permet de démontrer la convergence sans connaître la limite.

### 7.4 Exemple : les approximations décimales de √2

Posons uₙ=⌊10ⁿ√2⌋/10ⁿ. Chaque uₙ est rationnel et :

0≤√2−uₙ<10⁻ⁿ.

Pour m,n suffisamment grands, l'inégalité triangulaire donne :

|uₙ−uₘ|≤|uₙ−√2|+|√2−uₘ|<10⁻ⁿ+10⁻ᵐ.

Le membre de droite peut être rendu aussi petit que souhaité. La suite est donc de Cauchy dans Q. Elle ne converge pourtant vers aucun rationnel : sa limite réelle est √2, qui est irrationnel. C'est un exemple concret de l'incomplétude de Q.

### 7.5 Une condition insuffisante

La propriété |uₙ₊₁−uₙ|→0 n'implique pas que (uₙ) soit de Cauchy.

**Contre-exemple :** uₙ=1+1/2+…+1/n. Les écarts successifs valent 1/(n+1), donc tendent vers 0, mais la suite des sommes partielles de la série harmonique diverge vers +∞.

## 8. Liens entre les formulations de la complétude

Dans R, les formulations suivantes sont équivalentes :
1. Toute partie non vide majorée possède un supremum.
2. Toute suite de Cauchy réelle converge dans R.
3. Toute suite réelle bornée possède une sous-suite convergente (Bolzano–Weierstrass).
4. Toute suite d'intervalles fermés emboîtés dont les longueurs tendent vers 0 possède un unique point commun.

Ces équivalences constituent une partie importante de l'analyse réelle. Une preuve complète de toutes les implications est un sujet de travail avancé ; le présent dossier établit les idées et les preuves fondamentales sans prétendre développer chaque équivalence dans tous ses détails.

## 9. Applications aux sciences quantitatives et au calcul numérique

- **Optimisation :** le supremum décrit la meilleure borne supérieure d'une fonction ou d'un ensemble de valeurs ; il ne garantit pas que cette valeur soit atteinte.
- **Estimation numérique :** une suite d'approximations peut être de Cauchy même si la valeur exacte est inconnue.
- **Arrêt d'un algorithme :** la petitesse de l'écart entre deux itérations successives n'est pas, à elle seule, une preuve de convergence.
- **Statistique asymptotique :** les résultats de convergence des estimateurs et des suites de variables aléatoires s'appuient sur des idées de complétude, de métrique et de convergence, qui seront approfondies dans les blocs ultérieurs.
- **Analyse des erreurs :** distinguer convergence mathématique, stabilité numérique et précision de calcul. Ce sont trois questions différentes.

## 10. Erreurs conceptuelles à éviter

1. Confondre majorant et maximum.
2. Confondre supremum et maximum.
3. Supposer que tout ensemble borné possède un maximum et un minimum.
4. Confondre densité de Q et complétude de Q.
5. Croire qu'une suite de Cauchy est automatiquement convergente dans tout ensemble numérique.
6. Vérifier seulement |uₙ₊₁−uₙ|→0 pour conclure qu'une suite est de Cauchy.
7. Utiliser la propriété de la borne supérieure dans Q sans vérifier qu'elle y est vraie.
8. Confondre une borne supérieure finie avec un élément de l'ensemble.
9. Confondre convergence d'une suite et convergence de toutes ses sous-suites.
10. Conclure qu'un algorithme est stable parce que ses premières itérations semblent se rapprocher.

## 11. Plan de travail

| Séquence | Contenu | Durée indicative |
|---|---|---:|
| 1 | Corps ordonné, bornes et intervalles | 2 h |
| 2 | Supremum, infimum, maximum et minimum | 3 h |
| 3 | Complétude et comparaison R / Q | 2 h |
| 4 | Propriété archimédienne et densité | 2 h |
| 5 | Intervalles emboîtés | 2 h |
| 6 | Suites de Cauchy et critère de convergence | 3 h |
| 7 | Exercices de synthèse et défense orale | 2 h |

## 12. Critères de maîtrise

L'étudiant doit pouvoir :
- donner les définitions exactes de majorant, minorant, supremum et infimum ;
- distinguer supremum et maximum à l'aide d'exemples ;
- justifier pourquoi tout ensemble non vide majoré de R possède un supremum ;
- expliquer pourquoi Q n'est pas complet ;
- énoncer et utiliser la propriété archimédienne ;
- démontrer qu'une suite convergente est de Cauchy ;
- expliquer le critère de Cauchy dans R et construire un exemple de suite de Cauchy rationnelle sans limite rationnelle ;
- réfuter la fausse implication |uₙ₊₁−uₙ|→0 ⇒ convergence.

## 13. Références bibliographiques

1. Stephen Abbott, *Understanding Analysis*, 2nd edition, Springer, 2015. Chapitre 1 : construction conceptuelle des réels, axiome de complétude, supremum/infimum, propriété archimédienne et densité ; chapitre 2 : suites, convergence monotone, Bolzano–Weierstrass et critère de Cauchy. Ressource de l'auteur/éditeur : https://link.springer.com/book/10.1007/978-1-4939-2712-8
2. Robert G. Bartle et Donald R. Sherbert, *Introduction to Real Analysis*, 4th edition, Wiley, 2011. Chapitres sur les nombres réels, les suites et la complétude.
3. MIT OpenCourseWare, *18.100A Real Analysis*, Fall 2020. Notes de cours, notamment les sections sur la complétude et les suites de Cauchy : https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/
4. University of Waterloo, notes de cours de révision en analyse réelle, définitions de Cauchy, complétude de R, Bolzano–Weierstrass et supremum : https://uwaterloo.ca/scholar/sites/default/files/g6tran/files/amath731_lecture01.pdf

Les références 1 et 2 sont des manuels de référence pour l'analyse réelle. La ressource MIT est un support universitaire ouvert. Le document est une synthèse pédagogique originale ; il ne remplace pas la lecture suivie des manuels.

