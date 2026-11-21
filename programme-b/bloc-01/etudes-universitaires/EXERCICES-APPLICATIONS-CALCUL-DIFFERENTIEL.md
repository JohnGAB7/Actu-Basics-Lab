# Exercices corrigés — Applications du calcul différentiel

**Programme B · Bloc 1**  
20 exercices progressifs. Les solutions sont volontairement détaillées : les hypothèses, les domaines et l'interprétation font partie de la réponse.

## Exercice 1 — Rolle

Soit \(f(x)=x^2-4x+3\) sur \([1,3]\). Vérifier les hypothèses de Rolle et déterminer \(c\).

**Corrigé.** Le polynôme est continu sur \([1,3]\) et dérivable sur \(]1,3[\). \(f(1)=0=f(3)\). Or \(f'(x)=2x-4\), donc \(f'(c)=0\) donne \(c=2\), qui appartient bien à l'intervalle ouvert.

## Exercice 2 — Hypothèse manquante

Considérer \(f(x)=|x|\) sur \([-1,1]\). Les valeurs aux bornes sont égales. Pourquoi ne peut-on pas appliquer Rolle ?

**Corrigé.** La fonction est continue, mais non dérivable en zéro. Sa dérivée vaut \(-1\) sur \(]-1,0[\) et \(1\) sur \(]0,1[\). Il n'existe donc aucun point intérieur où une dérivée nulle serait obtenue. L'hypothèse de dérivabilité manque.

## Exercice 3 — Théorème des accroissements finis

Pour \(f(x)=x^2\) sur \([1,3]\), déterminer le point \(c\) fourni par le TAF.

**Corrigé.** La pente moyenne vaut \((9-1)/(3-1)=4\). Comme \(f'(x)=2x\), \(2c=4\), donc \(c=2\).

## Exercice 4 — Borne Lipschitz

Montrer que \(|\sin y-\sin x|\leq|y-x|\) pour tous réels \(x,y\).

**Corrigé.** Si \(x\ne y\), le TAF donne un \(c\) entre les deux tel que \((\sin y-\sin x)/(y-x)=\cos c\). Comme \(|\cos c|\leq1\), l'inégalité suit. Le cas \(x=y\) est immédiat.

## Exercice 5 — Monotonie et unicité

Montrer que l'équation \(x^3+x=1\) possède une unique solution réelle.

**Corrigé.** Posons \(g(x)=x^3+x-1\). Elle est continue, \(g(0)=-1\), \(g(1)=1\), donc le TVI donne au moins une racine dans \(]0,1[\). De plus \(g'(x)=3x^2+1>0\) partout : \(g\) est strictement croissante et ne peut avoir deux racines. Existence et unicité sont établies.

## Exercice 6 — Extrema et points critiques

Étudier les extrema locaux de \(f(x)=x^3-3x\).

**Corrigé.** \(f'(x)=3(x^2-1)=3(x-1)(x+1)\). Le signe est positif sur \(]-\infty,-1[\), négatif sur \(]-1,1[\), positif sur \(]1,+\infty[\). Maximum local en \(-1\), valeur \(2\) ; minimum local en \(1\), valeur \(-2\).

## Exercice 7 — Limites du test de la dérivée seconde

Étudier les trois fonctions \(x^4\), \(-x^4\), \(x^3\) au voisinage de zéro par le test de la dérivée seconde.

**Corrigé.** Pour les trois fonctions, \(f'(0)=0\) et \(f''(0)=0\) : le test est inconclusif. Pourtant \(x^4\) a un minimum strict, \(-x^4\) un maximum strict, et \(x^3\) n'a pas d'extremum. Il faut revenir au signe de \(f'\) ou à la définition.

## Exercice 8 — Convexité

Étudier la convexité de \(f(x)=x^4-2x^2\).

**Corrigé.** \(f''(x)=12x^2-4=4(3x^2-1)\). La fonction est convexe pour \(|x|>1/\sqrt3\), concave pour \(|x|<1/\sqrt3\). Les deux points \(x=\pm1/\sqrt3\) sont des points d'inflexion car le signe change de part et d'autre.

## Exercice 9 — Étude complète

Étudier \(f(x)=x+1/x\).

**Corrigé.** Domaine \(\mathbb R\setminus\{0\}\). \(f'(x)=(x^2-1)/x^2\), donc croissance sur \(]-\infty,-1[\) et \(]1,+\infty[\), décroissance sur \(]-1,0[\) et \(]0,1[\). Maximum local en \(-1\), valeur \(-2\) ; minimum local en \(1\), valeur \(2\). \(f''(x)=2/x^3\) : concave à gauche de zéro, convexe à droite. \(x=0\) est asymptote verticale et \(y=x\) asymptote oblique aux infinis.

## Exercice 10 — Asymptote oblique

Montrer que \(f(x)=(2x^2+3x+1)/(x+1)\) admet une asymptote oblique et préciser le point exclu.

**Corrigé.** Pour \(x\ne-1\), division ou factorisation donne \(f(x)=2x+1\). Le domaine exclut \(-1\), mais \(f(x)-(2x+1)=0\) sur le domaine. La droite \(y=2x+1\) est l'asymptote oblique aux deux infinis ; le graphe comporte un trou au point d'abscisse \(-1\), de limite \(-1\).

## Exercice 11 — Taylor d'ordre 2

Écrire le polynôme de Taylor d'ordre 2 de \(e^x\) en zéro et majorer le reste pour \(x\in[0,0,2]\).

**Corrigé.** \(T_2(x)=1+x+x^2/2\). La dérivée troisième de \(e^x\) est \(e^x\), majorée par \(e^{0,2}\) sur l'intervalle. Taylor-Lagrange donne
\[
|R_2(x)|\leq e^{0,2}\frac{x^3}{6}\leq e^{0,2}\frac{0,2^3}{6}\approx0,00163.
\]

## Exercice 12 — Approximation logarithmique

Approcher \(\ln(1,05)\) par le développement d'ordre 2 de \(\ln(1+x)\) en zéro et donner une borne du reste.

**Corrigé.** \(T_2(x)=x-x^2/2\), donc à \(x=0,05\), l'approximation vaut \(0,04875\). La dérivée troisième est \(2/(1+x)^3\), de valeur absolue au plus 2 sur \([0,0,05]\). Ainsi \(|R_2|\leq2(0,05)^3/6\approx0,00004167\).

## Exercice 13 — Optimisation géométrique

Un rectangle de périmètre 40 m a une aire maximale. Déterminer ses dimensions.

**Corrigé.** Si un côté vaut \(x\), l'autre vaut \(20-x\), avec \(0\leq x\leq20\). \(A(x)=x(20-x)\), \(A'(x)=20-2x\), donc \(x=10\). Comme \(A''=-2<0\) et que les aires aux bornes sont nulles, le maximum global est obtenu pour 10 m par 10 m, soit 100 m².

## Exercice 14 — Optimisation avec coût

Une activité produit \(q\in[0,100]\) unités. Le profit (en euros) est \(\Pi(q)=60q-q^2-200\). Déterminer le profit maximal.

**Corrigé.** \(\Pi'(q)=60-2q\), donc le seul point critique admissible est \(q=30\). \(\Pi''=-2<0\). Comparaison : \(\Pi(0)=-200\), \(\Pi(30)=700\), \(\Pi(100)=-4200\). Le maximum global est 700 € pour 30 unités.

## Exercice 15 — Taux liés

Le rayon d'un cercle augmente à raison de 0,2 cm/s. À \(r=5\) cm, à quelle vitesse son aire augmente-t-elle ?

**Corrigé.** \(A=\pi r^2\). En dérivant par rapport au temps : \(dA/dt=2\pi r\,dr/dt\). À l'instant considéré : \(2\pi\times5\times0,2=2\pi\) cm²/s.

## Exercice 16 — Newton

Appliquer trois itérations de Newton à \(f(x)=x^2-3\), avec \(x_0=2\).

**Corrigé.** \(x_{n+1}=(x_n+3/x_n)/2\). \(x_1=1,75\), \(x_2=1,732142857\), \(x_3\approx1,73205081\), proche de \(\sqrt3\). La suite est ici bien initialisée ; ce résultat ne prouve pas que Newton converge depuis tout point initial.

## Exercice 17 — Échec possible de Newton

Pourquoi la méthode de Newton ne peut-elle pas démarrer en \(x_0=0\) pour \(f(x)=x^2+1\) ? Et que révèle cette fonction ?

**Corrigé.** \(f'(0)=0\), donc la formule divise par zéro et l'itération n'est pas définie. En outre \(x^2+1>0\) sur \(\mathbb R\) : aucune racine réelle n'existe. Un algorithme de recherche de racine ne peut produire une racine réelle inexistante.

## Exercice 18 — Sensibilité

Un indicateur \(R(\theta)=\theta^2+4/\theta\), \(\theta>0\). Déterminer le point de minimum et commenter la sensibilité.

**Corrigé.** \(R'=2\theta-4/\theta^2\). \(R'=0\) équivaut à \(\theta^3=2\), donc \(\theta_*=\sqrt[3]2\). \(R''=2+8/\theta^3>0\), donc minimum strict. \(R'(\theta)\) mesure la sensibilité absolue locale de l'indicateur, pas une élasticité ni un effet causal.

## Exercice 19 — Erreur de mesure

On mesure \(x=2\) avec une incertitude \(|\Delta x|\leq0,01\). Pour \(f(x)=\sqrt{x}\), donner une borne rigoureuse de l'erreur de sortie.

**Corrigé.** Sur \([1,99;2,01]\), \(f'(t)=1/(2\sqrt t)\leq1/(2\sqrt{1,99})\). Par le TAF,
\[
|\Delta f|\leq\frac{0,01}{2\sqrt{1,99}}\approx0,00355.
\]
La linéarisation donne environ \(0,01/(2\sqrt2)\approx0,00354\), proche mais pas identique à la borne.

## Exercice 20 — Synthèse actuarielle

Une charge modélisée par \(L(\theta)=1000e^{0,04\theta}+200\theta^2\), pour \(\theta\in[0,2]\), représente un indicateur pédagogique. Calculer \(L'(0)\), \(L''(\theta)\), puis expliquer ce que l'on peut et ne peut pas conclure.

**Corrigé.**
\[
L'(\theta)=40e^{0,04\theta}+400\theta,
\qquad
L''(\theta)=1,6e^{0,04\theta}+400>0.
\]
Donc \(L'(0)=40\), en unités de charge par unité de paramètre. La fonction est strictement convexe sur le domaine. La pente initiale mesure une sensibilité locale du modèle. Elle ne permet pas d'affirmer que le paramètre cause la charge observée, ni que le modèle est empiriquement bien spécifié. Il faudrait données, validation, incertitude paramétrique et analyse de stabilité.

## Barème d'entraînement indicatif

Chaque exercice peut être noté sur 5 points : hypothèses/domaine (1), méthode et justification (2), calcul (1), interprétation ou contrôle (1). Total sur 100. Pour les exercices de preuve, la logique de l'argument prime sur la seule conclusion numérique.

## Questions de défense orale

1. Pourquoi le TAF n'est-il pas une formule permettant toujours de calculer explicitement \(c\) ?
2. Pourquoi un point où \(f'=0\) n'est-il pas nécessairement un extremum ?
3. Comment distinguer une inflexion d'une annulation de \(f''\) ?
4. Quelle information apporte le reste de Taylor ?
5. Pourquoi un optimum intérieur ne suffit-il pas pour un problème contraint ?
6. Pourquoi un petit résidu Newton ne garantit-il pas une petite erreur sur la racine ?
7. Quelle différence entre dérivée, élasticité et causalité ?
