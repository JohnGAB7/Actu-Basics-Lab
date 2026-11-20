# Suites et séries numériques — convergence, extraction et critères

**Programme B · Bloc 1 · Extension préparatoire d'analyse réelle**  
**Niveau :** premier cycle universitaire, avec preuves élémentaires.  
**Charge indicative :** 18 à 24 heures.  
**Prérequis :** limites de suites, complétude de \(\mathbb R\), suites de Cauchy, inégalités et méthodes de démonstration.  
**Statut :** approfondissement du Bloc 1 ; ce document n'ouvre pas le Bloc 2.

---

## 1. Objectifs d'apprentissage

À l'issue de ce dossier, l'apprenant doit pouvoir :

1. définir une sous-suite et expliquer ce qu'une extraction conserve ou ne conserve pas ;
2. appliquer et interpréter le théorème de Bolzano–Weierstrass ;
3. relier monotonie, bornitude et convergence ;
4. définir une série par la suite de ses sommes partielles ;
5. distinguer convergence, divergence, convergence absolue et convergence conditionnelle ;
6. choisir un critère de convergence adapté et vérifier toutes ses hypothèses ;
7. contrôler une approximation par une série alternée ;
8. rédiger une preuve courte et identifier les erreurs classiques de raisonnement.

## 2. Sous-suites et extractions

### 2.1 Définition

Soit \( (u_n)_{n\geq 0} \) une suite réelle. Une sous-suite est une suite de la forme
\[
(u_{n_k})_{k\geq 0},
\]
où \(n_0<n_1<n_2<\cdots\) est une suite strictement croissante d'indices naturels.

Une sous-suite conserve l'ordre des termes sélectionnés, mais peut en omettre une infinité. Elle ne réordonne jamais les termes.

Exemples :

- si \(u_n=(-1)^n\), les indices pairs donnent la sous-suite constante égale à 1 et les indices impairs celle égale à -1 ;
- si \(u_n=1/n\) pour \(n\geq1\), la sous-suite \(u_{2k}=1/(2k)\) converge encore vers 0 ;
- si \(u_n=n\), toute sous-suite tend vers \( +\infty\).

### 2.2 Propriétés fondamentales

**Théorème.** Toute sous-suite d'une suite convergente vers \(L\) converge vers \(L\).

*Preuve.* Soit \(\varepsilon>0\). Il existe \(N\) tel que \(n\geq N\) implique \( |u_n-L|<\varepsilon\). Comme \(n_k\) est strictement croissante, \(n_k\geq k\) à un décalage d'indexation près ; en particulier, les indices \(n_k\) dépassent finalement \(N\). Donc \( |u_{n_k}-L|<\varepsilon\) à partir d'un certain rang. \(\square\)

**Conséquence.** Si deux sous-suites convergent vers deux limites différentes, la suite initiale ne converge pas.

Attention : la réciproque « une sous-suite converge, donc la suite converge » est fausse. Pour \(u_n=(-1)^n\), la sous-suite paire converge vers 1, mais la suite entière diverge.

### 2.3 Valeurs d'adhérence

Un réel \(L\) est une valeur d'adhérence de \( (u_n) \) s'il existe une sous-suite qui converge vers \(L\). Une suite convergente possède une seule valeur d'adhérence. Une suite bornée peut en avoir plusieurs : \( (-1)^n \) en possède deux, -1 et 1.

Cette notion permet de décrire les oscillations d'une suite sans exiger qu'elle ait une limite.

## 3. Théorème de Bolzano–Weierstrass

**Énoncé.** Toute suite réelle bornée possède au moins une sous-suite convergente.

La conclusion concerne une sous-suite, et non nécessairement la suite entière.

### 3.1 Idée de preuve par intervalles emboîtés

Une suite bornée est contenue dans un intervalle fermé \([a_0,b_0]\). On partage cet intervalle en deux moitiés. Au moins une moitié contient une infinité de termes de la suite ; on la conserve. On répète le procédé.

On obtient des intervalles fermés emboîtés \([a_k,b_k]\), chacun contenant une infinité de termes, et dont les longueurs tendent vers zéro. Par complétude de \(\mathbb R\), leur intersection contient un unique réel \(L\). On choisit successivement des indices croissants \(n_k\) tels que \(u_{n_k}\in[a_k,b_k]\). La longueur des intervalles tendant vers zéro, \(u_{n_k}\to L\).

Cette preuve montre précisément où la complétude des réels intervient.

### 3.2 Applications et limites

- Une suite bornée n'est pas forcément convergente : \( (-1)^n \).
- Toute suite bornée possède au moins une valeur d'adhérence.
- Si une suite bornée possède une unique valeur d'adhérence, alors elle converge vers cette valeur. En effet, si elle ne convergeait pas vers cette valeur, on pourrait extraire une sous-suite restant à distance au moins \(\varepsilon\), puis en extraire une sous-suite convergente par Bolzano–Weierstrass : sa limite serait une autre valeur d'adhérence.

### 3.3 Théorème de Bolzano–Weierstrass et compacité

Dans \(\mathbb R\), le théorème de Bolzano–Weierstrass est étroitement lié à la compacité des intervalles fermés et bornés. La formulation générale en dimension finie est le théorème de Bolzano–Weierstrass dans \(\mathbb R^d\) : toute suite bornée admet une sous-suite convergente. La limite appartient à \(\mathbb R^d\), mais pas nécessairement à un sous-ensemble arbitraire contenant les termes.

## 4. Suites monotones et convergence

Une suite est croissante si \(u_{n+1}\geq u_n\) pour tout \(n\), décroissante si \(u_{n+1}\leq u_n\). « Monotone » signifie ici croissante ou décroissante au sens large.

**Théorème de convergence monotone.**

- Toute suite croissante et majorée converge vers sa borne supérieure.
- Toute suite décroissante et minorée converge vers sa borne inférieure.

*Preuve pour le cas croissant.* Posons \(L=\sup\{u_n:n\in\mathbb N\}\). Pour tout \(\varepsilon>0\), \(L-\varepsilon\) n'est pas un majorant ; il existe donc un indice \(N\) tel que \(u_N>L-\varepsilon\). Pour \(n\geq N\), la croissance donne \(L-\varepsilon<u_N\leq u_n\leq L\), donc \( |u_n-L|<\varepsilon\). Ainsi \(u_n\to L\). Le cas décroissant s'obtient en changeant le signe. \(\square\)

La monotonie seule ne suffit pas : \(u_n=n\) est croissante mais non majorée ; \(u_n=-n\) est décroissante mais non minorée.

## 5. Séries numériques : définition par les sommes partielles

### 5.1 Définition

À une suite \( (a_n)_{n\geq0} \), on associe la série
\[
\sum_{n=0}^{\infty}a_n.
\]
On définit les sommes partielles
\[
S_N=\sum_{n=0}^{N}a_n.
\]
La série converge si et seulement si la suite \( (S_N) \) converge vers un réel \(S\). On écrit alors \(\sum_{n=0}^{\infty}a_n=S\). Sinon, la série diverge.

Une série n'est donc pas une addition ordinaire d'une infinité de nombres : sa définition repose sur une limite.

### 5.2 Condition nécessaire, non suffisante

Si \(\sum a_n\) converge, alors \(a_n\to0\), car
\[
a_n=S_n-S_{n-1}\longrightarrow S-S=0.
\]
La réciproque est fausse. La série harmonique \(\sum_{n=1}^{\infty}1/n\) diverge alors que \(1/n\to0\). Une preuve par regroupement donne
\[
1+\frac12+\left(\frac13+\frac14\right)
+\left(\frac15+\cdots+\frac18\right)+\cdots
\]
et chaque bloc après le premier apporte au moins \(1/2\), donc les sommes partielles ne sont pas bornées.

**Premier réflexe devant une série :** calculer la limite du terme général. Si elle n'est pas nulle ou n'existe pas, la série diverge. Si elle vaut zéro, aucune conclusion n'est encore permise.

### 5.3 Linéarité et modification d'un nombre fini de termes

Si \(\sum a_n\) et \(\sum b_n\) convergent, alors pour \(\alpha,\beta\in\mathbb R\),
\[
\sum(\alpha a_n+\beta b_n)
=\alpha\sum a_n+\beta\sum b_n.
\]
Modifier un nombre fini de termes ne change pas la nature (convergence ou divergence) d'une série, mais change généralement sa somme.

## 6. Séries de référence

### 6.1 Série géométrique

Pour \(r\in\mathbb R\),
\[
\sum_{n=0}^{N}r^n=
\begin{cases}
\dfrac{1-r^{N+1}}{1-r},&r\ne1,\\
N+1,&r=1.
\end{cases}
\]
Ainsi,
\[
\sum_{n=0}^{\infty}r^n=\frac1{1-r}
\quad\text{si et seulement si } |r|<1.
\]
Si \( |r|\geq1\), le terme général ne tend pas vers zéro, sauf cas particulier impossible ici pour une série géométrique de raison réelle de module au moins 1.

### 6.2 Séries télescopiques

Les termes se simplifient après développement des sommes partielles. Exemple :
\[
\frac1{n(n+1)}=\frac1n-\frac1{n+1}.
\]
Alors
\[
\sum_{n=1}^{N}\frac1{n(n+1)}
=1-\frac1{N+1}\longrightarrow1.
\]

### 6.3 Séries de Riemann (p-séries)

Pour \(p\in\mathbb R\),
\[
\sum_{n=1}^{\infty}\frac1{n^p}
\]
converge si et seulement si \(p>1\). Elle diverge pour \(p\leq1\).

Le cas \(p=1\) est la série harmonique. Pour \(p>1\), on peut démontrer la convergence par comparaison intégrale avec \(\int_1^{\infty}x^{-p}\,dx\).

## 7. Critères de comparaison pour les séries à termes positifs

Dans cette section, on suppose les termes non négatifs à partir d'un certain rang. Les premiers termes ne modifient pas la nature de la série.

### 7.1 Comparaison directe

Si \(0\leq a_n\leq b_n\) à partir d'un certain rang :

- si \(\sum b_n\) converge, alors \(\sum a_n\) converge ;
- si \(\sum a_n\) diverge, alors \(\sum b_n\) diverge.

La comparaison doit être orientée dans le bon sens. Une série plus petite qu'une série divergente n'est pas nécessairement divergente.

### 7.2 Comparaison par équivalence

Si \(a_n,b_n>0\) à partir d'un certain rang et
\[
\frac{a_n}{b_n}\longrightarrow c\in(0,+\infty),
\]
alors les deux séries sont de même nature.

En pratique, on compare souvent à \(1/n^p\) ou à une série géométrique.

### 7.3 Critère intégral

Soit \(f:[1,+\infty)\to[0,+\infty)\) continue, décroissante et telle que \(a_n=f(n)\). Alors \(\sum_{n=1}^{\infty}a_n\) et \(\int_1^{\infty}f(x)\,dx\) sont de même nature.

Les hypothèses de positivité et de décroissance sont essentielles. Le critère ne s'applique pas mécaniquement à toute fonction.

## 8. Critères du quotient et de la racine

### 8.1 Critère du quotient (d'Alembert)

Pour une série \(\sum a_n\), si
\[
L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|
\]
existe :

- si \(L<1\), la série converge absolument ;
- si \(L>1\) (ou si le quotient tend vers l'infini), la série diverge ;
- si \(L=1\), le critère ne conclut pas.

On l'utilise particulièrement pour les factorielles et les produits.

### 8.2 Critère de la racine (Cauchy)

Si
\[
L=\limsup_{n\to\infty}\sqrt[n]{|a_n|},
\]
alors :

- si \(L<1\), la série converge absolument ;
- si \(L>1\), la série diverge ;
- si \(L=1\), le critère ne conclut pas.

Lorsque la limite \(\sqrt[n]{|a_n|}\) existe, elle remplace le \(\limsup\). Le critère de la racine est souvent efficace lorsque le terme contient une puissance d'ordre \(n\).

**Règle méthodologique :** un critère qui ne conclut pas n'est pas une preuve de divergence ni de convergence. Il faut changer de méthode.

## 9. Convergence absolue et convergence conditionnelle

Une série \(\sum a_n\) converge absolument si \(\sum |a_n|\) converge. Elle converge conditionnellement si elle converge mais pas absolument.

**Théorème.** Toute série absolument convergente converge.

La convergence absolue est donc plus forte que la convergence simple.

### 9.1 Série alternée

Une série alternée est souvent de la forme
\[
\sum_{n=0}^{\infty}(-1)^n b_n,
\quad b_n\geq0.
\]
**Critère de Leibniz.** Si :

1. \(b_n\) est décroissante à partir d'un certain rang ;
2. \(b_n\to0\) ;

alors la série alternée converge.

De plus, si \(S\) est sa somme et \(S_N\) sa somme partielle, le reste vérifie
\[
|S-S_N|\leq b_{N+1}
\]
avec une indexation cohérente.

Exemple :
\[
\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}n
=1-\frac12+\frac13-\frac14+\cdots
\]
converge par Leibniz, mais n'est pas absolument convergente car la série des valeurs absolues est harmonique. C'est un exemple de convergence conditionnelle.

### 9.2 Réarrangement : mise en garde

Pour une série absolument convergente, toute permutation des termes conserve la somme. Pour une série conditionnellement convergente, un réarrangement peut modifier la somme, voire produire une divergence. Ce phénomène est décrit par le théorème de réarrangement de Riemann. Il interdit de traiter une série conditionnelle comme une somme finie que l'on pourrait réordonner librement.

## 10. Stratégie de résolution

Devant \(\sum a_n\) :

1. **Terme général :** vérifier si \(a_n\to0\). Si non, divergence immédiate.
2. **Signe :** les termes sont-ils positifs à partir d'un rang ? Alternés ? De signe variable ?
3. **Forme :** géométrique, télescopique, p-série, factorielle, puissance à l'ordre \(n\) ?
4. **Comparaison :** identifier une série de référence et prouver l'inégalité ou l'équivalence.
5. **Quotient/racine :** calculer la limite, sans oublier le cas égal à 1.
6. **Alternée :** vérifier décroissance et limite nulle ; exploiter la borne du reste.
7. **Conclusion :** nommer le critère, énoncer ses hypothèses et expliciter la conclusion (convergence, absolue, conditionnelle ou divergence).

Un résultat numérique de somme partielle ne démontre jamais, à lui seul, la convergence d'une série.

## 11. Applications en calcul numérique et en statistique

- **Approximation contrôlée :** une borne de reste permet de choisir le nombre de termes nécessaires pour atteindre une tolérance.
- **Algorithmes itératifs :** les suites décrivent les itérés ; convergence et vitesse de convergence sont deux questions distinctes.
- **Probabilités :** les sommes de probabilités sur un ensemble dénombrable sont des séries à termes positifs, dont la somme doit être 1.
- **Statistique et apprentissage :** les séries interviennent dans des développements, des fonctions génératrices et des approximations. La convergence d'une série numérique ne garantit pas automatiquement la convergence uniforme d'une série de fonctions ; cette question relève d'un cours ultérieur.

### Exemple : tolérance d'une approximation alternée

Pour la série alternée de terme \(b_n=1/n^2\), le critère de Leibniz donne un reste après \(N\) termes inférieur ou égal à \(1/(N+1)^2\). Pour garantir une erreur strictement inférieure à \(10^{-4}\), il suffit de choisir \(N\) tel que
\[
\frac1{(N+1)^2}<10^{-4},
\]
soit \(N+1>100\). Prendre \(N=100\) donne une borne égale à \(1/101^2\), inférieure à \(10^{-4}\).

## 12. Erreurs fréquentes à éviter

- Confondre convergence d'une sous-suite et convergence de la suite entière.
- Affirmer qu'une suite bornée converge : Bolzano–Weierstrass ne garantit qu'une sous-suite convergente.
- Oublier qu'une série est définie par les sommes partielles.
- Conclure qu'une série converge parce que son terme général tend vers zéro.
- Utiliser une comparaison dans le mauvais sens.
- Appliquer le critère intégral sans vérifier décroissance et positivité.
- Conclure avec le critère du quotient ou de la racine lorsque la limite vaut 1.
- Appliquer Leibniz sans établir la décroissance des valeurs absolues.
- Confondre convergence absolue et convergence conditionnelle.
- Manipuler ou réordonner librement une série conditionnelle.

## 13. Parcours conseillé et critères de maîtrise

| Étape | Travail | Temps indicatif |
|---|---|---:|
| 1 | Sous-suites, valeurs d'adhérence, Bolzano–Weierstrass | 3 h |
| 2 | Monotonie, suites de Cauchy, convergence | 2 h |
| 3 | Sommes partielles et séries de référence | 3 h |
| 4 | Comparaison et critère intégral | 3 h |
| 5 | Quotient, racine, convergence absolue | 3 h |
| 6 | Séries alternées, reste et synthèse | 4–6 h |

La maîtrise est démontrée lorsque l'apprenant sait : produire une extraction ; expliquer Bolzano–Weierstrass ; prouver la convergence d'une suite monotone bornée ; définir une série par ses sommes partielles ; sélectionner un critère en justifiant ses hypothèses ; distinguer convergence absolue et conditionnelle ; et estimer un reste.

Les temps et seuils sont des propositions pédagogiques propres au cursus, pas des normes académiques universelles.

## 14. Bibliographie et ressources ouvertes

1. **Stephen Abbott**, *Understanding Analysis*, 2e édition, Springer, 2015, chapitre 2 « Sequences and Series » (sous-suites, Bolzano–Weierstrass, critère de Cauchy et séries). [Page de l'éditeur et sommaire](https://link.springer.com/book/10.1007/978-1-4939-2712-8). Référence principale pour l'approche rigoureuse.
2. **MIT OpenCourseWare**, *18.100A Real Analysis*, Fall 2020. Les semaines 4 à 6 couvrent suites monotones, sous-suites, Bolzano–Weierstrass, séries, convergence absolue, comparaison, quotient, racine et séries alternées. [Cours](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/) · [Notes et lectures](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/pages/lecture-notes-and-readings/) · [Notes complètes PDF](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_lec_full.pdf).
3. **Robert G. Bartle et Donald R. Sherbert**, *Introduction to Real Analysis*, 4e édition, Wiley, 2011. Référence complémentaire pour les preuves et les exercices.
4. **Walter Rudin**, *Principles of Mathematical Analysis*, 3e édition, McGraw-Hill, 1976. Référence plus exigeante, à utiliser en complément et non comme premier support.

Les liens ont été retenus pour leur pertinence pédagogique et leur traçabilité. Les cours ci-dessus sont des synthèses originales : ils ne reproduisent pas les manuels et ne remplacent pas leur lecture.

---

**Positionnement dans le cursus :** cette extension consolide l'analyse réelle élémentaire après la passerelle logique/limites et le dossier sur la complétude de \(\mathbb R\). La topologie élémentaire, les limites de fonctions plus avancées, les dérivées et les intégrales seront abordées dans une progression ultérieure.
