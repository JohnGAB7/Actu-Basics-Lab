# Limites de fonctions et continuité — étude universitaire

**Programme B · Bloc 1 · Extension préparatoire à l'analyse réelle**  
Niveau visé : universitaire introductif à intermédiaire, avec premières preuves epsilon-delta.  
Charge indicative : 12 à 16 heures de cours et démonstrations, puis 8 à 10 heures d'exercices.  
Prérequis : fonctions et domaines (F07), suites convergentes, complétude de \(\mathbb R\), topologie élémentaire de \(\mathbb R\).

> Ce document prolonge les fondements du Bloc 1. Il ne lance pas le Bloc 2 et n'aborde pas encore les dérivées ni les intégrales.

## 1. Objectifs d'apprentissage

À la fin de ce dossier, l'apprenant doit pouvoir :

1. définir une limite finie en un point avec les quantificateurs \(\varepsilon\)-\(\delta\) ;
2. construire un \(\delta\) adapté à un \(\varepsilon\) dans des preuves élémentaires ;
3. distinguer limite, valeur de la fonction et comportement au voisinage ;
4. utiliser les limites latérales, à l'infini et infinies ;
5. caractériser une limite par les suites ;
6. appliquer les lois de limites, le théorème des gendarmes et les limites de compositions sous leurs hypothèses ;
7. définir la continuité en un point, sur un intervalle et uniformément ;
8. classer les discontinuités et construire des contre-exemples ;
9. énoncer et utiliser les théorèmes des valeurs intermédiaires et des extrema ;
10. expliquer le rôle de la compacité et les limites des conclusions tirées d'un graphique ou d'un calcul numérique.

## 2. La limite : l'idée et la définition exacte

### 2.1 L'idée fondamentale

Dire que \(\lim_{x\to a}f(x)=L\), c'est dire que les valeurs de \(f(x)\) peuvent être rendues aussi proches que souhaité de \(L\), en imposant à \(x\) d'être suffisamment proche de \(a\), mais distinct de \(a\).

La valeur \(f(a)\), lorsqu'elle existe, ne décide pas de la limite. La limite décrit le comportement *autour* de \(a\), non nécessairement *en* \(a\).

Exemple :
\[
f(x)=\begin{cases}
(x^2-1)/(x-1),&x\ne1,\\
17,&x=1.
\end{cases}
\]
Pour \(x\ne1\), \(f(x)=x+1\). Ainsi \(\lim_{x\to1}f(x)=2\), alors que \(f(1)=17\).

### 2.2 Définition epsilon-delta

Soit \(f:D\to\mathbb R\), et soit \(a\) un point d'accumulation de \(D\). On écrit
\[
\lim_{x\to a}f(x)=L
\]
si et seulement si
\[
\forall\varepsilon>0,\ \exists\delta>0,\ \forall x\in D,\quad
0<|x-a|<\delta\Longrightarrow |f(x)-L|<\varepsilon.
\]

Lecture attentive :
- \(\varepsilon\) est une tolérance verticale arbitraire ;
- \(\delta\) est une tolérance horizontale choisie en fonction de \(\varepsilon\) ;
- le quantificateur « pour tout \(x\) » interdit de vérifier seulement quelques valeurs ;
- la condition \(0<|x-a|\) exclut le point \(a\) lui-même ;
- \(a\) doit être un point d'accumulation du domaine pour que l'approche soit possible.

L'ordre des quantificateurs est essentiel : pour chaque \(\varepsilon\), on doit pouvoir choisir un \(\delta\), qui fonctionne ensuite pour tous les \(x\) admissibles.

### 2.3 Exemple de preuve complète

Montrons que \(\lim_{x\to3}(2x+1)=7\).

Soit \(\varepsilon>0\). On veut
\[
|(2x+1)-7|=2|x-3|<\varepsilon.
\]
Il suffit donc de choisir \(\delta=\varepsilon/2\). Si \(0<|x-3|<\delta\), alors
\[
|(2x+1)-7|=2|x-3|<2\delta=\varepsilon.
\]
La limite vaut donc 7.

### 2.4 Exemple nécessitant une restriction locale

Montrons que \(\lim_{x\to2}x^2=4\).

On factorise :
\[
|x^2-4|=|x-2||x+2|.
\]
Si l'on impose d'abord \(|x-2|<1\), alors \(1<x<3\), donc \(|x+2|<5\). Pour obtenir \(|x^2-4|<\varepsilon\), il suffit de prendre
\[
\delta=\min(1,\varepsilon/5).
\]
Alors \(0<|x-2|<\delta\) implique \(|x^2-4|<5\delta\le\varepsilon\).

**Méthode générale :** factoriser ou transformer l'expression, contrôler les facteurs qui dépendent de \(x\) par une restriction locale, puis choisir \(\delta\) comme le minimum des contraintes.

## 3. Limites latérales et limites à l'infini

### 3.1 Limites à gauche et à droite

\[
\lim_{x\to a^-}f(x)=L
\]
signifie que \(x<a\) s'approche de \(a\), et
\[
\lim_{x\to a^+}f(x)=L
\]
que \(x>a\) s'approche de \(a\).

Une limite bilatérale finie existe si et seulement si les deux limites latérales existent et sont égales.

Exemple :
\[
f(x)=\begin{cases}-1,&x<0,\\1,&x\ge0.\end{cases}
\]
En zéro, la limite à gauche vaut \(-1\), celle à droite vaut \(1\). La limite bilatérale n'existe pas.

### 3.2 Limite lorsque \(x\to+\infty\)

On écrit \(\lim_{x\to+\infty}f(x)=L\) si
\[
\forall\varepsilon>0,\ \exists A\in\mathbb R,\ \forall x\in D,\quad
x>A\Longrightarrow |f(x)-L|<\varepsilon.
\]
La définition en \(-\infty\) est analogue, avec \(x<A\).

Exemple :
\[
\lim_{x\to+\infty}\frac{3x+1}{x+2}=3,
\]
car
\[
\left|\frac{3x+1}{x+2}-3\right|
=\frac{5}{|x+2|}\to0.
\]

### 3.3 Limites infinies

\(\lim_{x\to a}f(x)=+\infty\) signifie :
\[
\forall M>0,\ \exists\delta>0,\quad
0<|x-a|<\delta\Longrightarrow f(x)>M.
\]
On définit de même \(-\infty\). Ces expressions décrivent une divergence non bornée ; elles ne sont pas des limites réelles finies.

Exemple : \(\lim_{x\to0^+}1/x=+\infty\), tandis que \(\lim_{x\to0^-}1/x=-\infty\). La limite bilatérale n'existe pas, même au sens d'une même divergence infinie.

## 4. Lois de limites et outils de calcul

Si \(f(x)\to L\) et \(g(x)\to M\) lorsque \(x\to a\), alors, sous les conditions usuelles :

- \(\lim(f+g)=L+M\) ;
- \(\lim(cf)=cL\) ;
- \(\lim(fg)=LM\) ;
- \(\lim(f/g)=L/M\) si \(M\ne0\) et le quotient est défini près de \(a\) ;
- \(\lim |f|=|L|\) ;
- pour une composition, si \(g(x)\to M\) et \(h\) est continue en \(M\), alors \(h(g(x))\to h(M)\).

Ces lois ne permettent pas de conclure automatiquement dans les formes indéterminées \(0/0\), \(\infty/\infty\), \(0\times\infty\), \(\infty-\infty\), \(1^\infty\), \(0^0\), \(\infty^0\). Une forme indéterminée signale qu'une transformation supplémentaire est nécessaire.

### 4.1 Factorisation

\[
\lim_{x\to1}\frac{x^2-1}{x-1}
=\lim_{x\to1}(x+1)=2,
\]
la simplification étant valable pour \(x\ne1\), précisément dans le voisinage ponctué utilisé pour la limite.

### 4.2 Rationalisation

\[
\lim_{x\to0}\frac{\sqrt{1+x}-1}{x}
=\lim_{x\to0}\frac{1}{\sqrt{1+x}+1}=\frac12.
\]
La multiplication par le conjugué transforme l'expression sans modifier les valeurs là où l'expression initiale est définie.

### 4.3 Théorème des gendarmes

Si \(g(x)\le f(x)\le h(x)\) près de \(a\) et si \(g(x)\to L\), \(h(x)\to L\), alors \(f(x)\to L\).

Exemple :
\[
-|x|\le x\sin(1/x)\le |x| \quad (x\ne0),
\]
donc \(\lim_{x\to0}x\sin(1/x)=0\).

## 5. Caractérisation séquentielle

Soit \(a\) un point d'accumulation de \(D\). Alors
\[
\lim_{x\to a}f(x)=L
\]
si et seulement si, pour toute suite \((x_n)\) de points de \(D\setminus\{a\}\) telle que \(x_n\to a\), on a \(f(x_n)\to L\).

Cette caractérisation relie directement les limites de fonctions à la théorie des suites étudiée précédemment.

**Utilité pour démontrer une absence de limite :** il suffit de trouver deux suites \(x_n\to a\) et \(y_n\to a\) telles que \(f(x_n)\) et \(f(y_n)\) aient des limites différentes, ou qu'une des suites d'images ne converge pas vers une même valeur.

Exemple : \(f(x)=\sin(1/x)\) n'a pas de limite en zéro. On peut choisir des suites positives tendant vers zéro telles que \(1/x_n=\pi/2+2n\pi\) et \(1/y_n=3\pi/2+2n\pi\). Les images valent respectivement 1 et -1.

## 6. Continuité en un point

Une fonction \(f:D\to\mathbb R\) est continue en \(a\in D\) si
\[
\lim_{x\to a,\ x\in D}f(x)=f(a).
\]
Équivalent à :
\[
\forall\varepsilon>0,\ \exists\delta>0,\quad
x\in D,\ |x-a|<\delta\Longrightarrow |f(x)-f(a)|<\varepsilon.
\]
Ici, contrairement à la définition de la limite, le cas \(x=a\) est autorisé.

Trois conditions doivent être réunies :
1. \(f(a)\) est définie ;
2. la limite en \(a\) existe ;
3. cette limite est égale à \(f(a)\).

Une fonction est continue sur un intervalle si elle est continue en chaque point de cet intervalle. Sur un intervalle fermé \([a,b]\), la continuité aux extrémités est définie relativement au domaine : à droite en \(a\), à gauche en \(b\).

### 6.1 Continuité et suites

\(f\) est continue en \(a\) si et seulement si, pour toute suite \(x_n\in D\) telle que \(x_n\to a\), on a \(f(x_n)\to f(a)\).

### 6.2 Fonctions usuelles

Les polynômes sont continus sur \(\mathbb R\). Les fonctions rationnelles sont continues sur leur domaine de définition. Les fonctions racine, exponentielle, logarithme, sinus et cosinus sont continues sur leurs domaines respectifs. Les sommes, produits, quotients (dénominateur non nul) et compositions de fonctions continues restent continues là où ils sont définis.

Attention : la continuité d'une formule ne rend pas son expression définie hors de son domaine. Par exemple \(\ln x\) n'est pas une fonction réelle définie pour \(x\le0\).

## 7. Types de discontinuité

### 7.1 Discontinuité amovible

La limite existe et est finie, mais la fonction n'est pas définie au point ou prend une valeur différente.

Exemple : \(f(x)=(x^2-1)/(x-1)\) pour \(x\ne1\), avec \(f(1)=0\). La limite vaut 2 ; remplacer la valeur en 1 par 2 rend la fonction continue.

### 7.2 Discontinuité par saut

Les limites latérales existent et sont finies mais différentes. Exemple : la fonction indicatrice de \([0,+\infty)\) présente un saut en zéro.

### 7.3 Discontinuité infinie

Au moins une limite latérale est infinie. Exemple : \(f(x)=1/x\) en zéro.

### 7.4 Discontinuité oscillatoire

Le comportement ne se stabilise pas, sans être simplement une divergence vers l'infini. Exemple : \(\sin(1/x)\) en zéro.

### 7.5 Fonction de Dirichlet

\[
D(x)=\begin{cases}1,&x\in\mathbb Q,\\0,&x\notin\mathbb Q.\end{cases}
\]
Tout intervalle contient rationnels et irrationnels. En tout point, on peut donc construire des suites rationnelles et irrationnelles convergeant vers ce point, dont les images valent respectivement 1 et 0. La fonction est discontinue partout.

Cette fonction rappelle qu'une apparence graphique ou un échantillonnage numérique ne suffit pas à établir la continuité.

## 8. Théorèmes fondamentaux de continuité

### 8.1 Théorème des valeurs intermédiaires (TVI)

Si \(f\) est continue sur \([a,b]\), alors, pour tout \(y\) compris entre \(f(a)\) et \(f(b)\), il existe \(c\in[a,b]\) tel que \(f(c)=y\).

Corollaire de Bolzano : si \(f\) est continue sur \([a,b]\) et \(f(a)f(b)<0\), alors il existe \(c\in(a,b)\) tel que \(f(c)=0\).

Le TVI garantit une existence, pas nécessairement l'unicité. Pour établir l'unicité, il faut une information supplémentaire, par exemple la stricte monotonie.

**Application :** si \(P\) est un polynôme et \(P(a)P(b)<0\), il possède au moins une racine dans \((a,b)\). La méthode de dichotomie exploite ce résultat pour encadrer numériquement une racine, sous maintien d'un changement de signe et de la continuité.

### 8.2 Théorème des bornes atteintes (Weierstrass)

Si \(f\) est continue sur un compact non vide \(K\subset\mathbb R\), alors \(f\) est bornée et atteint son minimum et son maximum sur \(K\).

En particulier, sur \([a,b]\), une fonction continue possède un minimum global et un maximum global.

La fermeture et la bornitude de l'intervalle sont importantes. Sur \(]0,1[\), la fonction \(f(x)=x\) est bornée mais n'atteint ni 0 ni 1. Sur \(]0,1]\), \(f(x)=1/x\) n'est pas bornée.

### 8.3 Conséquence : existence ne signifie pas calcul explicite

Le théorème garantit un point où l'extremum est atteint, mais ne donne pas automatiquement sa valeur ni sa localisation. Il faut une méthode supplémentaire pour le déterminer.

## 9. Continuité uniforme

### 9.1 Définition

Une fonction \(f:D\to\mathbb R\) est uniformément continue sur \(D\) si
\[
\forall\varepsilon>0,\ \exists\delta>0,\ \forall x,y\in D,\quad
|x-y|<\delta\Longrightarrow |f(x)-f(y)|<\varepsilon.
\]

Différence centrale :
- continuité en chaque point : \(\delta\) peut dépendre du point \(a\) ;
- continuité uniforme : pour une tolérance \(\varepsilon\), un seul \(\delta\) fonctionne pour toutes les paires de points du domaine.

La continuité uniforme implique la continuité. La réciproque est fausse en général.

### 9.2 Exemples

- \(f(x)=3x+2\) est uniformément continue sur \(\mathbb R\), car \(|f(x)-f(y)|=3|x-y|\).
- \(f(x)=x^2\) est continue sur \(\mathbb R\), mais non uniformément continue sur \(\mathbb R\). En prenant \(x_n=n\), \(y_n=n+1/n\), on a \(|x_n-y_n|\to0\), tandis que \(|x_n^2-y_n^2|=2+1/n^2\) ne tend pas vers zéro.
- \(x^2\) est uniformément continue sur tout intervalle fermé borné \([a,b]\), par le théorème suivant.

### 9.3 Théorème de Heine-Cantor

Toute fonction continue sur un compact est uniformément continue.

Sur un segment fermé borné, la continuité point par point se renforce donc en continuité uniforme. La compacité, étudiée dans le dossier de topologie, est la charnière de ce résultat.

### 9.4 Critère séquentiel de non-uniformité

Une fonction n'est pas uniformément continue sur \(D\) s'il existe \(\varepsilon_0>0\) et deux suites \(x_n,y_n\in D\) telles que \(|x_n-y_n|\to0\), mais \(|f(x_n)-f(y_n)|\ge\varepsilon_0\) pour tout \(n\).

Ce critère est particulièrement efficace pour réfuter une uniformité.

## 10. Applications quantitatives et numériques

### 10.1 Encadrement d'une solution

Pour \(f(x)=x^3+x-1\), on a \(f(0)=-1\), \(f(1)=1\). Par continuité et TVI, une racine existe dans \((0,1)\). Comme \(f\) est strictement croissante (ce fait pourra être justifié plus tard par les outils de dérivation, ou ici par comparaison algébrique), cette racine est unique. La dichotomie peut ensuite produire un encadrement numérique.

### 10.2 Sensibilité locale

La continuité en \(a\) signifie que pour toute tolérance de sortie \(\varepsilon\), il existe une tolérance d'entrée \(\delta\). Elle formalise une stabilité locale, mais ne fournit pas nécessairement une borne uniforme valable sur tout le domaine.

### 10.3 Modèles quantitatifs

Dans un modèle \(y=f(x)\), la continuité exprime l'absence de saut local de la sortie lorsque l'entrée varie légèrement. Elle ne garantit ni que le modèle est bien spécifié, ni qu'il est robuste aux erreurs de données, ni que son extrapolation est fiable. Une fonction continue peut varier très rapidement ; une fonction uniformément continue offre un contrôle global plus fort, mais pas forcément une faible sensibilité au sens pratique.

## 11. Erreurs fréquentes à éviter

1. Confondre \(f(a)\) et \(\lim_{x\to a}f(x)\).
2. Inclure \(x=a\) dans la condition de limite.
3. Inverser les quantificateurs de la définition epsilon-delta.
4. Conclure à l'existence d'une limite à partir d'un tableau de valeurs fini.
5. Supposer qu'une limite bilatérale existe lorsque seule une limite latérale a été calculée.
6. Simplifier une expression sans préciser où l'égalité est valable.
7. Appliquer une loi de quotient lorsque la limite du dénominateur vaut zéro.
8. Confondre une forme indéterminée avec une absence de limite.
9. Affirmer que le TVI garantit une racine unique.
10. Appliquer Weierstrass à un intervalle ouvert ou non compact.
11. Confondre continuité et continuité uniforme.
12. Déduire la continuité d'un graphe échantillonné ou d'un calcul informatique.

## 12. Synthèse des implications

- Dérivabilité en un point \(\Rightarrow\) continuité en ce point (la preuve sera développée avec le calcul différentiel).
- Continuité en un point \(\not\Rightarrow\) dérivabilité en ce point.
- Continuité uniforme \(\Rightarrow\) continuité.
- Continuité sur un compact \(\Rightarrow\) continuité uniforme.
- Continuité sur un compact \(\Rightarrow\) bornitude et extrema atteints.
- Continuité sur un intervalle \(\Rightarrow\) propriété des valeurs intermédiaires.
- Continuité sur un intervalle ne garantit pas la monotonie ni l'injectivité.

## 13. Parcours conseillé

1. Refaire les deux preuves epsilon-delta des sections 2.3 et 2.4.
2. Étudier les limites latérales puis les limites à l'infini.
3. Résoudre les limites algébriques en identifiant explicitement les formes indéterminées.
4. Refaire la caractérisation séquentielle et les contre-exemples.
5. Classer les discontinuités.
6. Démontrer et appliquer TVI et Weierstrass en vérifiant chaque hypothèse.
7. Comparer continuité ponctuelle et uniforme.
8. Résoudre les exercices sans consulter les corrigés.

## 14. Références académiques et ressources ouvertes

1. MIT OpenCourseWare, **18.100A Real Analysis**, Fall 2020 : cours de niveau undergraduate, avec démonstrations, limites de fonctions, caractérisation séquentielle, continuité, fonction de Dirichlet, extrema, TVI et continuité uniforme. [Page du cours](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/) · [Notes de cours et lectures](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/pages/lecture-notes-and-readings/).
2. MIT OpenCourseWare, **Basic Analysis: Introduction to Real Analysis**, notes associées au cours 18.100A, notamment les sections sur les limites de fonctions et la continuité uniforme. [PDF](https://live.ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_basic_analysis.pdf).
3. OpenStax, **Calculus Volume 1**, chapitre 2 : lois de limites, continuité, TVI et définition précise epsilon-delta. [Concepts clés](https://openstax.org/books/calculus-volume-1/pages/2-key-concepts) · [Continuité](https://openstax.org/books/calculus-volume-1/pages/2-4-continuity).
4. Stephen Abbott, **Understanding Analysis**, 2e édition, Springer, chapitres consacrés aux limites, à la continuité et à la topologie de \(\mathbb R\). [Référence éditoriale](https://link.springer.com/book/10.1007/978-1-4939-2712-8).
5. Jiří Lebl, **Basic Analysis I: Introduction to Real Analysis**, ressource libre mobilisée dans les lectures du MIT. [Ouvrage](https://www.jirka.org/ra/).

Les références servent de base à la structuration et à la vérification des théorèmes. Le présent texte, ses exemples appliqués et ses exercices sont une synthèse pédagogique originale ; il ne remplace pas les ouvrages cités.
