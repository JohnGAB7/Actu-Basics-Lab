# Exercices corrigés — limites de fonctions et continuité

**Programme B · Bloc 1 · Extension préparatoire à l'analyse réelle**  
20 exercices progressifs. Les premières questions testent le calcul ; les suivantes exigent une preuve ou un contre-exemple. Les corrigés sont détaillés pour permettre l'auto-correction.

## Énoncés

### A. Calcul et définition

**1. Limite par factorisation.** Calculer \(\lim_{x\to2}(x^2-4)/(x-2)\). Justifier pourquoi la simplification est licite.

**2. Rationalisation.** Calculer \(\lim_{x\to0}(\sqrt{4+x}-2)/x\).

**3. Limite rationnelle à l'infini.** Calculer \(\lim_{x\to+\infty}(5x^2-3x+1)/(2x^2+x-4)\).

**4. Limite latérale.** Pour \(f(x)=1/(x-3)\), déterminer les limites à gauche et à droite en 3. La limite bilatérale existe-t-elle ?

**5. Preuve epsilon-delta.** Démontrer directement que \(\lim_{x\to-1}(4x+2)=-2\).

**6. Preuve epsilon-delta quadratique.** Démontrer que \(\lim_{x\to1}x^2=1\), en construisant explicitement un \(\delta(\varepsilon)\).

### B. Raisonnement séquentiel et contre-exemples

**7. Absence de limite.** Montrer que \(f(x)=\sin(1/x)\) n'a pas de limite lorsque \(x\to0\).

**8. Caractérisation séquentielle.** Soit \(f(x)=x/|x|\) pour \(x\ne0\). Utiliser deux suites pour montrer que la limite en zéro n'existe pas.

**9. Fonction de Dirichlet.** Montrer que \(D(x)=1\) si \(x\in\mathbb Q\), et \(D(x)=0\) sinon, est discontinue en tout réel.

**10. Fonction oscillante amortie.** Montrer que \(f(x)=x\sin(1/x)\) pour \(x\ne0\), avec \(f(0)=0\), est continue en zéro.

### C. Continuité et discontinuités

**11. Paramètre de raccordement.** Déterminer \(c\) pour que
\[
f(x)=\begin{cases}(x^2-1)/(x-1),&x\ne1,\\c,&x=1\end{cases}
\]
soit continue en 1.

**12. Classification.** Classer la discontinuité en zéro de chacune des fonctions : (a) \(1/x\) ; (b) la fonction signe \(x/|x|\) ; (c) \(x\sin(1/x)\) pour \(x\ne0\), avec valeur 0 en zéro ; (d) \((x^2-1)/(x-1)\) pour \(x\ne1\), avec valeur 0 en 1.

**13. Continuité sur un domaine.** Déterminer le domaine et les points de continuité de \(f(x)=\ln(x^2-1)\).

**14. Composition.** Si \(g(x)\to2\) lorsque \(x\to a\), et si \(h\) est continue en 2 avec \(h(2)=5\), déterminer \(\lim_{x\to a}h(g(x))\). Énoncer l'hypothèse essentielle.

### D. Théorèmes d'existence et compacité

**15. Application du TVI.** Montrer que l'équation \(x^3+x-1=0\) possède au moins une solution dans \((0,1)\).

**16. Attention à l'unicité.** Donner un exemple de fonction continue sur \([0,1]\) dont une équation \(f(x)=0\) possède plusieurs solutions. Expliquer pourquoi le TVI ne garantit pas l'unicité.

**17. Théorème de Weierstrass.** Expliquer pourquoi \(f(x)=x\) atteint ses extrema sur \([0,1]\), mais pas sur \(]0,1[\). Préciser les bornes et extrema.

**18. Hypothèse manquante.** Donner un exemple de fonction continue sur un intervalle non fermé et borné qui n'atteint pas son supremum.

### E. Continuité uniforme

**19. Fonction lipschitzienne.** Montrer que \(f(x)=7x-4\) est uniformément continue sur \(\mathbb R\).

**20. Échec de continuité uniforme.** Montrer que \(f(x)=x^2\) n'est pas uniformément continue sur \(\mathbb R\), à l'aide de deux suites.

---

## Corrigés détaillés

### 1. Limite par factorisation

Pour \(x\ne2\),
\[
\frac{x^2-4}{x-2}=\frac{(x-2)(x+2)}{x-2}=x+2.
\]
La limite ne dépend que des valeurs dans un voisinage ponctué de 2 ; le point \(x=2\) est exclu de la définition de la limite. Donc
\[
\boxed{\lim_{x\to2}\frac{x^2-4}{x-2}=4.}
\]

### 2. Rationalisation

Pour \(x\ne0\), multiplions par le conjugué :
\[
\frac{\sqrt{4+x}-2}{x}
=\frac{(\sqrt{4+x}-2)(\sqrt{4+x}+2)}{x(\sqrt{4+x}+2)}
=\frac{1}{\sqrt{4+x}+2}.
\]
La limite vaut donc
\[
\boxed{\frac14}.
\]

### 3. Limite rationnelle à l'infini

Divisons le numérateur et le dénominateur par \(x^2\) :
\[
\frac{5-3/x+1/x^2}{2+1/x-4/x^2}\longrightarrow\frac52.
\]
Le dénominateur tend vers 2, non nul. Résultat : \(\boxed{5/2}\).

### 4. Limite latérale

Si \(x\to3^-\), alors \(x-3\to0^-\), donc \(1/(x-3)\to-\infty\). Si \(x\to3^+\), le dénominateur tend vers zéro par valeurs positives, donc la limite vaut \(+\infty\). Il n'existe pas de limite bilatérale commune.

### 5. Preuve epsilon-delta affine

Soit \(\varepsilon>0\). On veut :
\[
|(4x+2)-(-2)|=4|x+1|<\varepsilon.
\]
Choisissons \(\delta=\varepsilon/4\). Si \(0<|x+1|<\delta\), alors
\[
|(4x+2)+2|=4|x+1|<4\delta=\varepsilon.
\]
La limite est bien \(-2\).

### 6. Preuve epsilon-delta quadratique

On factorise :
\[
|x^2-1|=|x-1||x+1|.
\]
Imposons \(|x-1|<1\). Alors \(0<x<2\), donc \(|x+1|<3\). Posons
\[
\delta=\min(1,\varepsilon/3).
\]
Si \(0<|x-1|<\delta\), alors
\[
|x^2-1|<3|x-1|<3\delta\le\varepsilon.
\]
La limite vaut 1.

### 7. Absence de limite de \(\sin(1/x)\)

Prenons
\[
x_n=\frac{1}{\pi/2+2n\pi},\qquad
y_n=\frac{1}{3\pi/2+2n\pi}.
\]
Les deux suites tendent vers zéro, mais
\[
\sin(1/x_n)=1,\qquad \sin(1/y_n)=-1.
\]
La caractérisation séquentielle impose que toute suite tendant vers zéro ait une suite image convergeant vers la même limite. C'est impossible : la limite n'existe pas.

### 8. Deux suites pour la fonction signe

Posons \(x_n=1/n\) et \(y_n=-1/n\). Elles tendent toutes deux vers zéro. Pourtant \(f(x_n)=1\) et \(f(y_n)=-1\). Les limites séquentielles diffèrent, donc la limite en zéro n'existe pas.

### 9. Discontinuité partout de la fonction de Dirichlet

Fixons \(a\in\mathbb R\). Par densité de \(\mathbb Q\) et de \(\mathbb R\setminus\mathbb Q\), il existe une suite rationnelle \(r_n\to a\) et une suite irrationnelle \(s_n\to a\). Alors \(D(r_n)=1\) et \(D(s_n)=0\). Les images ne peuvent tendre vers une même valeur. La limite en \(a\) n'existe pas, quelle que soit la valeur \(D(a)\). Ainsi \(D\) est discontinue en tout réel.

### 10. Continuité de \(x\sin(1/x)\)

Pour \(x\ne0\), \(|\sin(1/x)|\le1\), donc
\[
-|x|\le x\sin(1/x)\le|x|.
\]
Les deux bornes tendent vers zéro lorsque \(x\to0\). Par le théorème des gendarmes, la limite vaut zéro. Comme \(f(0)=0\), la fonction est continue en zéro.

### 11. Paramètre de raccordement

Pour \(x\ne1\),
\[
\frac{x^2-1}{x-1}=x+1.
\]
La limite en 1 vaut 2. La continuité impose \(f(1)=c=2\). Valeur unique : \(\boxed{c=2}\).

### 12. Classification

(a) \(1/x\) : discontinuité infinie en zéro (les limites latérales sont de signes opposés).  
(b) \(x/|x|\) : discontinuité par saut, avec limites latérales -1 et 1.  
(c) \(x\sin(1/x)\), prolongée par 0 : aucune discontinuité en zéro ; la fonction y est continue.  
(d) quotient prolongé par 0 en 1 : discontinuité amovible, car la limite vaut 2 mais la valeur vaut 0.

### 13. Domaine et continuité de \(\ln(x^2-1)\)

Il faut \(x^2-1>0\), soit \(x<-1\) ou \(x>1\). Le domaine est
\[
D=(-\infty,-1)\cup(1,+\infty).
\]
Le polynôme \(x^2-1\) est continu et strictement positif sur ce domaine ; le logarithme est continu sur \(]0,+\infty[\). Par composition, \(f\) est continue en tout point de son domaine. Les points \(\pm1\) ne sont pas dans le domaine.

### 14. Composition

Puisque \(g(x)\to2\) et que \(h\) est continue en 2,
\[
\lim_{x\to a}h(g(x))=h(2)=\boxed5.
\]
L'hypothèse essentielle est la continuité de \(h\) au point limite de \(g\), avec la composition définie dans un voisinage pertinent.

### 15. Existence d'une racine

Soit \(f(x)=x^3+x-1\), polynôme donc continu sur \([0,1]\). On a \(f(0)=-1<0\) et \(f(1)=1>0\). Par le corollaire de Bolzano, il existe \(c\in(0,1)\) tel que \(f(c)=0\). Le théorème ne donne pas ici une expression explicite de \(c\).

### 16. Le TVI ne garantit pas l'unicité

Prenons \(f(x)=x(x-1/2)(x-1)\), continue sur \([0,1]\). Elle possède trois zéros : 0, 1/2 et 1. Le TVI garantit que les valeurs intermédiaires sont prises, mais plusieurs antécédents peuvent correspondre à la même valeur. L'unicité exige une hypothèse supplémentaire, par exemple une stricte monotonie sur l'intervalle.

### 17. Extrema sur un segment et sur un intervalle ouvert

Sur \([0,1]\), \(f(x)=x\) atteint son minimum 0 en \(x=0\) et son maximum 1 en \(x=1\). Sur \(]0,1[\), son infimum est 0 et son supremum est 1, mais aucune de ces valeurs n'est atteinte. La continuité seule ne suffit pas : le compact \([0,1]\) est l'hypothèse déterminante du théorème de Weierstrass.

### 18. Exemple sans maximum

Sur \(D=]0,1[\), \(f(x)=x\) est continue et bornée. Son supremum est 1, mais aucun \(x\in D\) ne vérifie \(f(x)=1\). Le domaine est borné mais non fermé, donc non compact dans \(\mathbb R\).

### 19. Continuité uniforme d'une fonction affine

Pour tous \(x,y\in\mathbb R\),
\[
|f(x)-f(y)|=|7x-4-(7y-4)|=7|x-y|.
\]
Soit \(\varepsilon>0\). Choisissons \(\delta=\varepsilon/7\). Si \(|x-y|<\delta\), alors \(|f(x)-f(y)|<\varepsilon\). Le même \(\delta\) fonctionne pour tous les points : \(f\) est uniformément continue.

### 20. \(x^2\) n'est pas uniformément continue sur \(\mathbb R\)

Prenons \(x_n=n\) et \(y_n=n+1/n\). Alors
\[
|x_n-y_n|=1/n\to0,
\]
mais
\[
|x_n^2-y_n^2|
=|(n+1/n)^2-n^2|
=2+1/n^2\ge2.
\]
En choisissant \(\varepsilon_0=1\), aucune tolérance \(\delta\) ne peut fonctionner uniformément pour toutes les paires de points. Donc \(x^2\) n'est pas uniformément continue sur \(\mathbb R\).

## Barème indicatif et maîtrise

| Domaine | Exercices | Points |
|---|---:|---:|
| Limites et preuves epsilon-delta | 1–6 | 30 |
| Raisonnement séquentiel | 7–10 | 20 |
| Continuité et domaine | 11–14 | 20 |
| Théorèmes d'existence | 15–18 | 20 |
| Continuité uniforme | 19–20 | 10 |
| **Total** | **20** | **100** |

Proposition pédagogique : viser 80/100, sans erreur majeure sur les quantificateurs, les limites latérales ou les hypothèses des théorèmes. Une note élevée obtenue par calcul mécanique, sans justification, ne suffit pas à valider la maîtrise.

## Questions de défense orale

1. Pourquoi la valeur \(f(a)\) n'intervient-elle pas dans la définition de \(\lim_{x\to a}f(x)\) ?
2. Pourquoi faut-il que \(a\) soit un point d'accumulation du domaine ?
3. Comment une suite peut-elle réfuter l'existence d'une limite ?
4. Quelle hypothèse du théorème de Weierstrass échoue sur \(]0,1[\) ?
5. Pourquoi une fonction continue n'est-elle pas nécessairement uniformément continue ?
6. Pourquoi le TVI ne prouve-t-il pas l'unicité d'une racine ?
7. Quelle différence y a-t-il entre une limite infinie et une limite réelle ?
8. Pourquoi un graphique calculé sur un nombre fini de points ne prouve-t-il pas la continuité ?

## Références

- MIT OpenCourseWare, [18.100A Real Analysis — cours](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/) et [notes de cours](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/pages/lecture-notes-and-readings/).
- OpenStax, [Calculus Volume 1 — chapitre 2](https://openstax.org/books/calculus-volume-1/pages/2-key-concepts).
- Stephen Abbott, *Understanding Analysis*, 2e édition, Springer, [référence](https://link.springer.com/book/10.1007/978-1-4939-2712-8).
- Jiří Lebl, *Basic Analysis I*, [ressource libre](https://www.jirka.org/ra/).
