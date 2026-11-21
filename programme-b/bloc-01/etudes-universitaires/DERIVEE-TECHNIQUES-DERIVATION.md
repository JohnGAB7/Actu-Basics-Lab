# Dérivée et techniques de dérivation — étude universitaire

**Programme B · Bloc 1 · Extension préparatoire à l'analyse réelle**  
Niveau : calcul différentiel introductif/intermédiaire, avec définition rigoureuse et démonstrations fondamentales.  
Charge indicative : 14 à 18 heures de cours, puis 8 à 12 heures d'exercices.  
Prérequis : limites et continuité, algèbre, fonctions usuelles, trigonométrie et composition.

> Ce document ouvre l'étude du calcul différentiel dans la continuité préparatoire du Bloc 1. Il ne constitue pas l'ouverture administrative du Bloc 2. Les applications approfondies (optimisation, méthode de Newton, étude complète des courbes, Taylor et inégalités) feront l'objet d'une unité distincte.

## 1. Objectifs d'apprentissage

À la fin du cours, l'apprenant doit pouvoir :
1. interpréter un taux de variation moyen et instantané ;
2. définir la dérivée comme limite d'un taux d'accroissement ;
3. calculer une dérivée à partir de la définition dans des cas élémentaires ;
4. démontrer que la dérivabilité implique la continuité et comprendre la réciproque fausse ;
5. appliquer et justifier les règles de dérivation ;
6. dériver des compositions, fonctions réciproques et fonctions définies implicitement ;
7. déterminer les domaines de dérivabilité et repérer les points singuliers ;
8. interpréter les dérivées premières et secondes ;
9. contrôler un calcul symbolique par une méthode indépendante et interpréter ses unités.

## 2. Taux de variation moyen et instantané

Pour une fonction \(f\) et deux points distincts \(a\) et \(a+h\), le taux de variation moyen est
\[
\frac{f(a+h)-f(a)}{h}.
\]
Il représente la pente de la sécante passant par \((a,f(a))\) et \((a+h,f(a+h))\).

Lorsque \(h\to0\), si cette quantité admet une limite finie, on obtient le taux de variation instantané :
\[
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}.
\]
Géométriquement, \(f'(a)\) est la pente de la tangente au graphe en \((a,f(a))\). Dans un modèle temporel \(s(t)\), si \(s\) est une position, \(s'(t)\) est la vitesse instantanée.

Attention aux unités : si \(f\) mesure des euros et \(x\) des contrats, \(f'(x)\) s'exprime en euros par contrat. Si \(s\) est en mètres et \(t\) en secondes, \(s'(t)\) est en mètres par seconde.

## 3. Définition formelle de la dérivée

Soit \(f\) définie dans un voisinage de \(a\). La fonction est dérivable en \(a\) si la limite finie
\[
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}
\]
existe. La forme équivalente est
\[
f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}.
\]

La dérivée est donc une limite de quotients, et non une simple pente « lue » sur un dessin. La dérivée \(f'\) est la fonction qui associe à chaque point dérivable \(x\) la valeur \(f'(x)\).

### 3.1 Exemple : dérivée de \(f(x)=x^2\)

Pour \(h\ne0\),
\[
\frac{(x+h)^2-x^2}{h}
=\frac{2xh+h^2}{h}=2x+h.
\]
En faisant tendre \(h\) vers zéro :
\[
\boxed{f'(x)=2x.}
\]

### 3.2 Exemple : dérivée de \(f(x)=1/x\)

Pour \(x\ne0\), et \(h\) assez proche de zéro pour que \(x+h\ne0\),
\[
\frac{1/(x+h)-1/x}{h}
=\frac{-h}{x(x+h)h}
=-\frac{1}{x(x+h)}.
\]
La limite donne
\[
\boxed{f'(x)=-1/x^2,\quad x\ne0.}
\]

### 3.3 Dérivées unilatérales et extrémités

Sur un domaine fermé, une dérivée à une extrémité peut être définie unilatéralement. Pour parler de dérivabilité usuelle sur un intervalle ouvert, on considère les limites bilatérales. Aux points intérieurs, les dérivées à gauche et à droite doivent exister et être égales.

## 4. Dérivabilité et continuité

**Théorème.** Si \(f\) est dérivable en \(a\), alors \(f\) est continue en \(a\).

**Preuve.** Pour \(h\ne0\),
\[
f(a+h)-f(a)
=h\frac{f(a+h)-f(a)}{h}.
\]
Quand \(h\to0\), le premier facteur tend vers zéro et le second vers \(f'(a)\), donc leur produit tend vers zéro. Ainsi \(f(a+h)\to f(a)\), ce qui établit la continuité.

La réciproque est fausse. Exemple : \(f(x)=|x|\) est continue en zéro, mais
\[
\frac{|h|-0}{h}=
\begin{cases}1,&h>0,\\-1,&h<0,\end{cases}
\]
n'a pas de limite bilatérale. La fonction n'est pas dérivable en zéro.

Autres causes possibles de non-dérivabilité : angle, cuspide, tangente verticale ou discontinuité. Il faut examiner la définition, pas seulement le dessin.

## 5. Règles fondamentales de dérivation

Dans les domaines où les fonctions sont dérivables :

### 5.1 Constante, somme et facteur constant
\[
(c)'=0,\quad (cf)'=cf',\quad (f+g)'=f'+g'.
\]
La règle de différence découle de la linéarité de la limite.

### 5.2 Produit
\[
(fg)'=f'g+fg'.
\]
**Justification :** écrire
\[
\frac{f(x+h)g(x+h)-f(x)g(x)}h
=f(x+h)\frac{g(x+h)-g(x)}h
+g(x)\frac{f(x+h)-f(x)}h.
\]
La continuité de \(f\), conséquence de sa dérivabilité, permet de passer à la limite.

### 5.3 Quotient
Si \(g(a)\ne0\),
\[
\left(\frac fg\right)'(a)
=\frac{f'(a)g(a)-f(a)g'(a)}{g(a)^2}.
\]
La condition \(g(a)\ne0\) est indispensable.

### 5.4 Puissance entière
Pour \(n\in\mathbb N\), \((x^n)'=nx^{n-1}\), par factorisation de \( (x+h)^n-x^n\) ou par récurrence et règle du produit. Les puissances négatives se traitent par quotient sur leur domaine.

Pour une puissance réelle \(x^\alpha\), le domaine réel dépend de \(\alpha\). Sur \(x>0\), on peut écrire \(x^\alpha=e^{\alpha\ln x}\), puis dériver par composition :
\[
(x^\alpha)'=\alpha x^{\alpha-1}.
\]
Cette formule ne dispense pas d'examiner le domaine aux valeurs négatives ou en zéro.

## 6. Dérivation en chaîne

Si \(g\) est dérivable en \(a\), et \(f\) dérivable en \(g(a)\), alors
\[
(f\circ g)'(a)=f'(g(a))g'(a).
\]

**Interprétation :** la variation de la sortie par rapport à l'entrée intermédiaire est multipliée par la variation de l'entrée intermédiaire par rapport à la variable initiale. Les unités se multiplient et se simplifient en conséquence.

Exemple :
\[
y=(3x^2+1)^5
\quad\Longrightarrow\quad
y'=5(3x^2+1)^4\cdot6x
=30x(3x^2+1)^4.
\]

Erreur fréquente : dériver la fonction extérieure sans multiplier par la dérivée de l'intérieur.

## 7. Fonctions exponentielles, logarithmiques et trigonométriques

Les formules suivantes s'appliquent sur les domaines correspondants.

### 7.1 Exponentielle et logarithme
\[
(e^x)'=e^x,\qquad (a^x)'=a^x\ln a\quad(a>0),
\]
\[
(\ln x)'=1/x\quad(x>0),\qquad
(\log_a x)'=\frac{1}{x\ln a}.
\]
Par composition :
\[
(e^{u(x)})'=u'(x)e^{u(x)},\qquad
(\ln u(x))'=\frac{u'(x)}{u(x)}
\]
lorsque \(u(x)>0\).

### 7.2 Trigonométrie
\[
(\sin x)'=\cos x,\quad
(\cos x)'=-\sin x,\quad
(\tan x)'=1/\cos^2x
\]
sur les domaines où ces fonctions sont définies. Les angles sont mesurés en radians ; les formules usuelles de dérivation trigonométrique reposent sur cette convention.

### 7.3 Fonctions hyperboliques
\[
(\sinh x)'=\cosh x,\qquad
(\cosh x)'=\sinh x,\qquad
(\tanh x)'=1/\cosh^2x.
\]
Elles interviennent dans certains modèles et équations, mais ne sont pas nécessaires pour les premiers exercices de calcul différentiel.

## 8. Fonction réciproque et dérivation implicite

### 8.1 Dérivée d'une fonction réciproque

Si \(f\) est bijective dans un voisinage pertinent, dérivable en \(a\), et \(f'(a)\ne0\), alors, sous les hypothèses locales usuelles,
\[
(f^{-1})'(f(a))=\frac{1}{f'(a)}.
\]
La condition de dérivée non nulle garantit ici que l'inversion locale possède une pente finie.

Exemple : pour \(f(x)=e^x\), la réciproque est \(\ln x\). On retrouve \((\ln x)'=1/x\).

### 8.2 Dérivation implicite

Une relation \(F(x,y)=0\) peut définir localement \(y\) comme fonction de \(x\). En dérivant les deux membres, \(y\) est traité comme une fonction de \(x\), donc chaque occurrence de \(y\) produit un facteur \(y'\).

Exemple :
\[
x^2+y^2=25
\quad\Longrightarrow\quad
2x+2yy'=0
\quad\Longrightarrow\quad
y'=-x/y
\]
lorsque \(y\ne0\). Cette expression est locale et ne prétend pas définir une pente finie aux points où \(y=0\).

## 9. Dérivées d'ordre supérieur

La dérivée seconde est \(f''=(f')'\), si cette dérivée existe. Plus généralement, \(f^{(n)}\) désigne la dérivée d'ordre \(n\).

- \(f'\) décrit le taux de variation local.
- \(f''\) décrit la variation du taux de variation.
- En mécanique, position, vitesse et accélération correspondent respectivement à \(s\), \(s'\) et \(s''\).
- En économie, une dérivée seconde peut décrire la courbure d'une fonction de coût ou de profit, mais l'interprétation dépend du modèle et des unités.

Exemple : \(f(x)=x^3-2x^2+x\), donc
\[
f'(x)=3x^2-4x+1,\qquad f''(x)=6x-4.
\]

## 10. Tangente et approximation locale

Si \(f\) est dérivable en \(a\), la tangente au graphe en \((a,f(a))\) a pour équation
\[
y=f(a)+f'(a)(x-a).
\]
Cette droite fournit une approximation locale :
\[
f(a+h)=f(a)+f'(a)h+o(h)\quad(h\to0).
\]
Le terme \(o(h)\) signifie que le reste, divisé par \(h\), tend vers zéro. Il ne signifie pas que l'approximation est exacte pour une valeur finie de \(h\).

Exemple : pour \(f(x)=\sqrt{x}\) autour de \(a=4\),
\[
f(4)=2,\quad f'(4)=1/4,\quad
\sqrt{4+h}\approx2+h/4
\]
pour \(h\) petit et compatible avec le domaine.

## 11. Lecture qualitative de la dérivée

Sur un intervalle, si \(f'(x)>0\) partout, \(f\) est strictement croissante ; si \(f'(x)<0\) partout, elle est strictement décroissante. Une dérivée nulle en un point n'implique pas à elle seule un extremum : \(f(x)=x^3\) a \(f'(0)=0\), sans maximum ni minimum local en zéro.

Si \(f''>0\) sur un intervalle, la dérivée est croissante et le graphe est convexe ; si \(f''<0\), il est concave. Les formulations globales exigent les hypothèses de dérivabilité correspondantes.

Une étude de variations complète, la classification des extrema et les critères du second ordre seront approfondis dans l'unité suivante avec le théorème des accroissements finis.

## 12. Applications quantitatives et actuarielles

### 12.1 Coût marginal

Si \(C(q)\) est le coût total de production pour une quantité \(q\), \(C'(q)\) représente le coût marginal instantané au niveau \(q\). Il s'exprime en unités monétaires par unité produite. Il s'agit d'une approximation locale, non nécessairement du coût exact d'une unité supplémentaire pour un changement important.

### 12.2 Sensibilité d'un indicateur

Si \(R(\theta)\) est un indicateur de risque dépendant d'un paramètre \(\theta\), \(R'(\theta)\) mesure la sensibilité locale à une petite variation de ce paramètre. Il faut préciser l'unité, l'échelle du paramètre et le domaine de validité.

### 12.3 Prime et fréquence

Si une prime modélisée \(P(x)\) dépend d'un facteur tarifaire \(x\), \(P'(x)\) mesure la variation marginale locale du tarif. La dérivée ne démontre pas que la relation causale est correctement spécifiée ; elle analyse la fonction choisie.

### 12.4 Contrôle numérique

Une dérivée peut être approximée par différences finies :
\[
f'(x)\approx\frac{f(x+h)-f(x)}h.
\]
Pour une fonction suffisamment régulière, une différence centrée
\[
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\]
est souvent plus précise en erreur de troncature. Mais un \(h\) trop petit amplifie les erreurs d'arrondi ; un \(h\) trop grand dégrade l'approximation locale. Le choix de \(h\) est un compromis numérique, non une formalité.

## 13. Erreurs fréquentes

1. Oublier la limite dans la définition de la dérivée.
2. Confondre taux de variation moyen et instantané.
3. Conclure que continuité implique dérivabilité.
4. Oublier la règle de chaîne.
5. Utiliser la règle du quotient avec un dénominateur nul.
6. Oublier les restrictions de domaine des logarithmes, racines et fonctions rationnelles.
7. Appliquer les formules trigonométriques avec des angles en degrés.
8. Traiter \(y\) comme une constante lors d'une dérivation implicite.
9. Conclure à un extremum du seul fait que \(f'(a)=0\).
10. Interpréter une tangente comme une approximation exacte loin du point.
11. Confondre dérivée analytique et estimation numérique.
12. Négliger les unités de la dérivée.

## 14. Fiche de formules

| Fonction | Dérivée |
|---|---|
| \(c\) | \(0\) |
| \(x^n\) | \(nx^{n-1}\) |
| \(cf\) | \(cf'\) |
| \(f+g\) | \(f'+g'\) |
| \(fg\) | \(f'g+fg'\) |
| \(f/g\) | \((f'g-fg')/g^2\), \(g\ne0\) |
| \(f\circ g\) | \((f'\circ g)g'\) |
| \(e^x\) | \(e^x\) |
| \(\ln x\) | \(1/x\), \(x>0\) |
| \(\sin x\) | \(\cos x\) |
| \(\cos x\) | \(-\sin x\) |
| \(\tan x\) | \(1/\cos^2x\) |

## 15. Références académiques

1. MIT OpenCourseWare, **18.01 Single Variable Calculus**, Fall 2005/2006 : taux de variation, définition de la dérivée, règles, chaîne, fonctions exponentielles/logarithmiques, approximations, extrema et théorème des accroissements finis. [Notes de cours 2005](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2005/pages/lecture-notes/) · [Notes de cours 2006](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/lecture-notes/).
2. OpenStax, **Calculus Volume 1**, chapitre 3 : définition de la dérivée, dérivée comme fonction et règles de dérivation. [Définition](https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative) · [Règles](https://openstax.org/books/calculus-volume-1/pages/3-3-differentiation-rules).
3. MIT OpenCourseWare, **18.01SC Single Variable Calculus**, programme et ressources d'apprentissage. [Cours](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/).
4. James Stewart, **Calculus: Early Transcendentals**, Cengage, référence complémentaire classique pour le calcul différentiel et ses applications.

Le cours est une synthèse pédagogique originale. Les références indiquent les sources de structuration et de vérification ; elles ne sont pas reproduites intégralement. Les applications actuarielles sont illustratives et ne constituent pas des modèles calibrés.
