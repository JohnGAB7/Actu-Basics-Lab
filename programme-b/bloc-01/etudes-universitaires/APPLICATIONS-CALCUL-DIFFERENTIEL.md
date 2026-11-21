# Applications du calcul différentiel — étude universitaire

**Programme B · Bloc 1 · Calcul différentiel à une variable**  
Niveau : universitaire introductif/intermédiaire, avec preuves fondamentales, analyse des hypothèses et applications.  
Charge indicative : 18 à 24 heures de cours et 12 à 18 heures d'exercices.  
Prérequis : limites, continuité, dérivabilité, règles de dérivation et dérivées usuelles.

> Cette unité complète le calcul différentiel du Bloc 1. Elle ne traite pas l'intégration, les équations différentielles ni le calcul multivarié. Les durées sont des estimations pédagogiques.

## 1. Objectifs

À l'issue de l'unité, l'apprenant doit pouvoir :
1. énoncer et utiliser les théorèmes de Rolle et des accroissements finis en vérifiant chaque hypothèse ;
2. établir des inégalités et des bornes d'erreur à partir d'une dérivée bornée ;
3. étudier monotonie, extrema, convexité, points d'inflexion et asymptotes ;
4. construire une étude complète de fonction en tenant compte du domaine et des limites ;
5. développer une approximation de Taylor et contrôler le reste ;
6. formaliser et résoudre un problème d'optimisation sur un domaine admissible ;
7. traiter un problème de taux liés par dérivation implicite ;
8. appliquer la méthode de Newton et expliquer pourquoi elle peut échouer ;
9. interpréter une sensibilité quantitative ou actuarielle sans confondre association mathématique et causalité.

## 2. Théorème de Rolle

**Théorème.** Si \(f:[a,b]\to\mathbb R\) est continue sur \([a,b]\), dérivable sur \(]a,b[\), et si \(f(a)=f(b)\), alors il existe \(c\in]a,b[\) tel que \(f'(c)=0\).

**Démonstration.** Par le théorème de Weierstrass, \(f\) atteint un maximum et un minimum sur le compact \([a,b]\). Si \(f\) est constante, toute valeur intérieure convient. Sinon, au moins l'un des extrema est atteint en un point intérieur \(c\), puisque les valeurs aux deux extrémités sont égales et qu'une valeur intérieure diffère de cette valeur commune. Au point intérieur d'extremum, la dérivabilité entraîne \(f'(c)=0\) : les taux d'accroissement à droite et à gauche ont des signes opposés et leur limite commune ne peut être que zéro.

**Pourquoi les hypothèses comptent.** La continuité sur le segment garantit l'existence des extrema ; la dérivabilité à l'intérieur permet d'annuler la dérivée au point d'extremum. Sans ces hypothèses, la conclusion peut échouer.

Exemple : \(f(x)=x^2-1\) sur \([-1,1]\). Les valeurs aux bornes sont nulles et \(f'(x)=2x\), donc \(c=0\).

## 3. Théorème des accroissements finis (TAF)

**Théorème.** Si \(f\) est continue sur \([a,b]\) et dérivable sur \(]a,b[\), avec \(a<b\), il existe \(c\in]a,b[\) tel que
\[
f'(c)=\frac{f(b)-f(a)}{b-a}.
\]

**Preuve.** Posons
\[
g(x)=f(x)-\left[f(a)+\frac{f(b)-f(a)}{b-a}(x-a)\right].
\]
La fonction \(g\) est continue sur le segment, dérivable à l'intérieur, et \(g(a)=g(b)=0\). Rolle fournit \(c\) tel que \(g'(c)=0\), ce qui donne le résultat.

**Interprétation.** À un instant intermédiaire, le taux instantané égale le taux moyen sur l'intervalle. Le théorème est une affirmation d'existence : il ne donne pas nécessairement la valeur de \(c\).

### 3.1 Corollaires

- Si \(f'=0\) sur un intervalle, \(f\) y est constante.
- Si \(f'=g'\) sur un intervalle, \(f-g\) est constante.
- Si \(f'\geq0\), alors \(f\) est croissante ; si \(f'>0\), elle est strictement croissante. Les versions avec signes négatifs sont analogues.
- Si \(|f'|\leq M\) sur un intervalle, alors \(|f(y)-f(x)|\leq M|y-x|\). C'est une condition de Lipschitz.

La stricte positivité de la dérivée est suffisante, mais non nécessaire, pour la stricte croissance : \(x^3\) est strictement croissante même si sa dérivée s'annule en zéro.

## 4. Inégalités et bornes d'erreur

Si \(f\) est dérivable entre \(x\) et \(x+h\), et \(|f'|\leq M\), le TAF donne
\[
|f(x+h)-f(x)|\leq M|h|.
\]
Cette borne transforme une incertitude sur l'entrée en une borne sur la sortie.

Si \(f'\geq m>0\), alors
\[
f(y)-f(x)\geq m(y-x)\quad\text{pour }y>x.
\]
Une telle borne peut prouver l'unicité d'une solution et contrôler la stabilité de l'inversion.

**Exemple.** Sur \([0,1]\), pour \(f(x)=e^x\), \(f'(x)=e^x\leq e\). Ainsi \(|e^{x+h}-e^x|\leq e|h|\) dès que les deux points et le segment qui les relie restent dans \([0,1]\).

Attention : une borne de dérivée doit être établie sur tout le segment considéré, pas uniquement à ses extrémités.

## 5. Points critiques et extrema

Pour une fonction définie sur un intervalle ouvert, un extremum local intérieur où \(f\) est dérivable impose \(f'(c)=0\) (théorème de Fermat). La réciproque est fausse : \(x^3\) a une dérivée nulle en zéro sans extremum.

Les candidats à examiner dans une étude d'extrema sont :
- les points où \(f'=0\) ;
- les points du domaine où \(f'\) n'existe pas ;
- les extrémités du domaine lorsque celui-ci est fermé et borné.

### 5.1 Tests

**Test de signe de \(f'\).** Un changement de signe de \(+\) vers \(-\) indique un maximum local ; de \(-\) vers \(+\), un minimum local. Sans changement de signe, il n'y a pas d'extremum strict déduit de ce test.

**Test de la dérivée seconde.** Si \(f'(c)=0\), si \(f''\) existe près de \(c\), et si \(f''(c)>0\), alors \(c\) est un minimum local strict ; si \(f''(c)<0\), un maximum local strict. Si \(f''(c)=0\), le test est muet : examiner \(x^4\), \(-x^4\) et \(x^3\) en zéro.

Un extremum global sur un intervalle fermé borné existe si \(f\) y est continue (Weierstrass). Sur un domaine non compact, l'existence doit être démontrée séparément.

## 6. Convexité, concavité et inflexion

Sur un intervalle où \(f\) est deux fois dérivable :
- \(f''\geq0\) implique que \(f'\) est croissante et que \(f\) est convexe ;
- \(f''\leq0\) implique que \(f\) est concave.

Un point d'inflexion est un point où la convexité change. L'annulation de \(f''\) n'est ni suffisante ni nécessaire si la dérivée seconde n'existe pas. Pour \(x^4\), \(f''(0)=0\) mais il n'y a pas de changement de convexité. Pour \(x^3\), la convexité change en zéro.

La convexité donne une information de forme et des inégalités de support. Pour une fonction convexe dérivable,
\[
f(y)\geq f(x)+f'(x)(y-x).
\]
La tangente est sous le graphe. Pour une fonction concave, l'inégalité est inversée.

## 7. Étude complète d'une fonction

Une étude raisonnée suit l'ordre suivant :

1. **Domaine** : exclusions, contraintes de racines, logarithmes et dénominateurs.
2. **Symétries et périodicité** : seulement si elles simplifient réellement l'étude.
3. **Limites** aux bornes du domaine et à l'infini.
4. **Continuité et dérivabilité**, points singuliers.
5. **Dérivée première** : factorisation, signe, variations et extrema.
6. **Dérivée seconde** : convexité et inflexions.
7. **Asymptotes** : verticales, horizontales ou obliques, à établir par des limites.
8. **Points remarquables** : zéros, intersections, tangentes.
9. **Graphique** : cohérent avec les résultats précédents, sans substituer le dessin à la preuve.

### Exemple guidé : \(f(x)=x+\frac1x\)

Domaine : \(\mathbb R\setminus\{0\}\).  
Dérivée :
\[
f'(x)=1-\frac1{x^2}=\frac{(x-1)(x+1)}{x^2}.
\]
La fonction est croissante sur \(]-\infty,-1[\), décroissante sur \(]-1,0[\), décroissante sur \(]0,1[\), puis croissante sur \(]1,+\infty[\). Elle admet un maximum local en \(-1\), de valeur \(-2\), et un minimum local en \(1\), de valeur \(2\).

\[
f''(x)=\frac{2}{x^3}.
\]
Elle est concave sur \(]-\infty,0[\), convexe sur \(]0,+\infty[\). La droite \(x=0\) est une asymptote verticale. Comme \(f(x)-x=1/x\to0\) lorsque \(x\to\pm\infty\), la droite \(y=x\) est une asymptote oblique aux deux infinis.

## 8. Taylor et contrôle du reste

Si \(f\) est suffisamment régulière près de \(a\), son polynôme de Taylor d'ordre \(n\) est
\[
T_n(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k.
\]
Il s'agit d'une approximation locale, pas d'une identité globale.

**Formule de Taylor-Lagrange.** Si \(f\) possède des dérivées jusqu'à l'ordre \(n+1\) sur l'intervalle entre \(a\) et \(x\), avec les conditions usuelles de continuité aux extrémités et de dérivabilité à l'intérieur, alors il existe \(\xi\) entre \(a\) et \(x\) tel que
\[
f(x)=T_n(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}.
\]
Si \(|f^{(n+1)}(t)|\leq M\) sur cet intervalle,
\[
|R_n(x)|\leq \frac{M|x-a|^{n+1}}{(n+1)!}.
\]

Exemples autour de zéro :
\[
e^x=1+x+\frac{x^2}{2}+R_2(x),
\]
\[
\sin x=x-\frac{x^3}{6}+R_3(x),
\qquad
\ln(1+x)=x-\frac{x^2}{2}+R_2(x)\quad(x>-1).
\]
Les bornes de reste doivent être calculées à partir d'une dérivée d'ordre supérieur bornée sur l'intervalle. Ne pas annoncer une précision numérique sans cette justification.

### 8.1 Propagation d'erreur

Pour une petite erreur \(\Delta x\), la linéarisation donne
\[
\Delta f\approx f'(x)\Delta x.
\]
En valeur absolue, cela suggère \(|\Delta f|\approx|f'(x)||\Delta x|\). C'est une approximation de premier ordre ; une borne rigoureuse exige un contrôle de \(f'\) sur l'intervalle d'incertitude. Pour une grandeur positive, l'erreur relative de premier ordre est approximativement \(|f'(x)x/f(x)|\cdot|\Delta x/x|\), lorsque \(f(x)\ne0\).

## 9. Optimisation sur un domaine

Une optimisation sérieuse comporte six étapes :
1. définir les variables, unités et contraintes ;
2. établir le domaine admissible ;
3. exprimer l'objectif par une fonction d'une variable lorsque c'est possible ;
4. démontrer l'existence d'un optimum ou justifier l'examen des frontières ;
5. calculer les points critiques et comparer tous les candidats admissibles ;
6. interpréter le résultat et tester sa robustesse.

**Exemple.** Un rectangle a un périmètre fixé \(P>0\). Si sa largeur est \(x\), sa longueur est \(P/2-x\), avec \(0\leq x\leq P/2\). Son aire vaut
\[
A(x)=x(P/2-x).
\]
La dérivée s'annule en \(x=P/4\), et \(A''=-2<0\). L'aire maximale est atteinte pour un carré, de côté \(P/4\), et vaut \(P^2/16\).

Un point critique n'est pas automatiquement un optimum global : comparer les frontières, vérifier les contraintes et examiner l'existence.

## 10. Taux liés

Lorsque plusieurs quantités dépendent du temps et sont reliées par une contrainte, dériver cette contrainte par rapport au temps.

Exemple : un cercle de rayon \(r(t)\) a une aire \(A(t)=\pi r(t)^2\). Alors
\[
\frac{dA}{dt}=2\pi r\frac{dr}{dt}.
\]
Il faut distinguer la valeur instantanée de \(r\) et son taux \(dr/dt\), puis substituer les données au même instant. Les unités doivent être cohérentes : aire par unité de temps.

## 11. Méthode de Newton

Pour résoudre \(f(x)=0\), la tangente au point \(x_n\) coupe l'axe horizontal en
\[
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.
\]
Cette méthode est locale. Elle exige notamment \(f'(x_n)\ne0\) à chaque itération ; la convergence n'est pas garantie pour un point initial arbitraire.

**Exemple.** Pour \(f(x)=x^2-2\), avec \(x_0=1\),
\[
x_{n+1}=\frac12\left(x_n+\frac2{x_n}\right).
\]
On obtient \(x_1=1,5\), \(x_2=1,4166667\), \(x_3\approx1,4142157\), qui approche \(\sqrt2\).

Critères d'arrêt possibles : \(|f(x_n)|\leq\varepsilon_f\), \(|x_{n+1}-x_n|\leq\varepsilon_x(1+|x_n|)\), ou une borne d'erreur démontrée. Un nombre maximal d'itérations est nécessaire en pratique. Un petit résidu ne garantit pas à lui seul une petite erreur sur la racine si la pente est très faible.


### 11.1 Convergence locale près d'une racine simple

Un résultat classique précise les circonstances favorables. Supposons que \(f\) soit de classe \(C^2\) dans un voisinage d'une racine \(\alpha\), que \(f(\alpha)=0\) et \(f'(\alpha)\ne0\). Alors il existe un voisinage de \(\alpha\) tel que, si \(x_0\) est choisi suffisamment près de \(\alpha\), les itérations de Newton restent dans ce voisinage et convergent vers \(\alpha\). Sous ces hypothèses, la convergence est localement quadratique : l'erreur à l'étape suivante est majorée par une constante fois le carré de l'erreur courante, lorsque les itérations sont assez proches.

**Justification de l'ordre.** Écrivons \(e_n=x_n-\alpha\). Le développement de Taylor autour de la racine montre que le terme linéaire est éliminé par la correction de Newton ; le premier terme restant est d'ordre \(e_n^2\). La condition \(f'(\alpha)\ne0\) évite une division par une pente nulle. La régularité \(C^2\) contrôle le reste. Cette conclusion est locale : elle ne garantit pas la convergence depuis un point initial arbitraire, ni en présence d'une racine multiple.

## 12. Applications quantitatives et actuarielles

### 12.1 Sensibilité locale

Pour un indicateur \(R(\theta)\), la dérivée \(R'(\theta)\) décrit la sensibilité locale. Une variation finie se traite mieux par une différence exacte ou par Taylor avec reste. Il faut préciser l'échelle du paramètre, les unités et la zone où l'approximation est acceptable.

### 12.2 Coût, prime et marge

Si \(C(q)\) est un coût en fonction d'un volume \(q\), \(C'(q)\) est le coût marginal local. Si \(P(\theta)\) est une prime calculée par une règle tarifaire, \(P'(\theta)\) décrit la pente locale de cette règle, non une relation causale. Une prime, un coût et un risque attendu sont des objets distincts.

### 12.3 Fonction de risque illustrative

Supposons un indicateur synthétique \(R(\theta)=\theta^2+4/\theta\), pour \(\theta>0\). Alors \(R'(\theta)=2\theta-4/\theta^2\), qui s'annule à \(\theta=\sqrt[3]{2}\). Comme \(R''(\theta)=2+8/\theta^3>0\), c'est le minimum global sur \(]0,+\infty[\), puisque \(R\to+\infty\) aux deux extrémités du domaine. Cet exemple est mathématique et n'est pas un modèle empirique calibré.

### 12.4 Limites de l'analyse

- Une dérivée dépend de la fonction choisie et de ses hypothèses.
- Une sensibilité locale n'est pas une élasticité ; celle-ci est une variation relative.
- Une pente n'établit ni causalité, ni stabilité hors échantillon.
- Les paramètres estimés peuvent être incertains ; leur incertitude doit être propagée séparément.
- Les contraintes réglementaires, commerciales et opérationnelles peuvent rendre l'optimum mathématique non admissible.

## 13. Synthèse des théorèmes et tests

| Outil | Hypothèses essentielles | Conclusion |
|---|---|---|
| Rolle | Continuité sur \([a,b]\), dérivabilité intérieure, \(f(a)=f(b)\) | \(f'(c)=0\) |
| TAF | Continuité sur le segment, dérivabilité intérieure | Une dérivée égale la pente moyenne |
| Fermat | Extremum local intérieur et dérivabilité | \(f'(c)=0\) |
| Weierstrass | Continuité sur compact | Maximum et minimum atteints |
| Test seconde dérivée | \(f'(c)=0\), \(f''(c)\) strictement positif/négatif avec régularité locale | Minimum/maximum local strict |
| Taylor-Lagrange | Dérivabilité suffisante jusqu'à l'ordre \(n+1\) | Polynôme + reste contrôlé |
| Newton | Itérations définies, pente non nulle ; convergence sous conditions supplémentaires | Approximation locale d'une racine |

## 14. Erreurs fréquentes

1. Appliquer le TAF sans vérifier continuité sur le segment et dérivabilité à l'intérieur.
2. Affirmer que \(f'(c)=0\) implique un extremum.
3. Oublier les extrémités d'un intervalle fermé dans une optimisation.
4. Confondre point d'inflexion et simple annulation de \(f''\).
5. Utiliser Taylor sans préciser le degré et le reste.
6. Transformer une approximation de premier ordre en égalité exacte.
7. Résoudre une optimisation sans formaliser le domaine.
8. Confondre taux liés et valeurs instantanées.
9. Supposer Newton convergent pour toute valeur initiale.
10. Interpréter une dérivée de tarif comme une preuve causale.

## 15. Références académiques

1. MIT OpenCourseWare, **18.01 Single Variable Calculus**, Fall 2006 : approximations, étude de courbes, optimisation, taux liés, méthode de Newton, TAF et inégalités. [Notes de cours](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/lecture-notes/).
2. MIT OpenCourseWare, **18.01SC Single Variable Calculus**, Fall 2010 : [Applications of Differentiation](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/).
3. OpenStax, **Calculus Volume 1**, chapitre 4 : [Applications of Derivatives](https://openstax.org/books/calculus-volume-1/pages/4-introduction).
4. James Stewart, **Calculus: Early Transcendentals**, Cengage, chapitres consacrés aux applications de la dérivée et aux approximations.

Le présent cours est une synthèse pédagogique originale. Les références servent à structurer et vérifier le contenu ; elles ne sont pas reproduites intégralement. Les exemples actuariels sont illustratifs et ne constituent pas des recommandations tarifaires.

## 16. Ordre d'étude conseillé

Rolle et TAF → corollaires et inégalités → extrema et convexité → études de fonctions → Taylor et erreurs → optimisation → taux liés → Newton → cas quantitatif. Pour chaque théorème, refaire la preuve, identifier un cas où une hypothèse manque, puis résoudre les exercices sans consulter le corrigé.
