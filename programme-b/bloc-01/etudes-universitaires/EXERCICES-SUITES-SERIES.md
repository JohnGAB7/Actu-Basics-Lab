# Exercices corrigés — Suites et séries numériques

**Programme B · Bloc 1 · Extension préparatoire d'analyse réelle**  
**Consigne :** essayer chaque exercice sans consulter le corrigé. Toute application d'un théorème doit être accompagnée de ses hypothèses. Les indices commencent à 1 sauf mention contraire.

---

## Partie A — Sous-suites et convergence

### Exercice 1 — Extraire les sous-suites

Soit \(u_n=(-1)^n+1/n\), pour \(n\geq1\).

1. Déterminer les limites des sous-suites de rang pair et impair.
2. La suite \( (u_n) \) converge-t-elle ?
3. Donner ses valeurs d'adhérence.

**Corrigé.**

Pour les indices pairs, \(u_{2k}=1+1/(2k)\to1\). Pour les indices impairs, \(u_{2k-1}=-1+1/(2k-1)\to-1\). Deux sous-suites ont des limites différentes ; la suite ne converge donc pas. Ses valeurs d'adhérence sont exactement -1 et 1 : les termes pairs et impairs se rapprochent de ces deux valeurs et aucune autre accumulation n'est possible.

### Exercice 2 — Une sous-suite convergente ne suffit pas

Construire une suite non convergente ayant une sous-suite convergente. Expliquer pourquoi cela ne contredit pas le théorème sur les sous-suites d'une suite convergente.

**Corrigé.**

Prendre \(u_n=(-1)^n\). La sous-suite \(u_{2k}=1\) est constante, donc convergente vers 1 ; la suite entière oscille entre -1 et 1. Le théorème dit que toute sous-suite d'une suite convergente converge vers la même limite ; il ne dit pas qu'une seule sous-suite convergente force la convergence de la suite initiale.

### Exercice 3 — Bolzano–Weierstrass

Soit \(u_n=\sin(n)\). Sans chercher à calculer une limite de la suite, que peut-on affirmer ?

**Corrigé.**

On sait que \( -1\leq\sin(n)\leq1\), donc la suite est bornée. Par Bolzano–Weierstrass, elle possède au moins une sous-suite convergente. Ce théorème ne donne pas ici la valeur de la limite extraite et ne garantit pas la convergence de la suite entière.

### Exercice 4 — Convergence monotone

On définit \(u_0=0\) et \(u_{n+1}=\sqrt{2+u_n}\).

1. Montrer que \(0\leq u_n\leq2\).
2. Montrer que la suite est croissante.
3. En déduire sa convergence et calculer sa limite.

**Corrigé.**

Par récurrence, si \(0\leq u_n\leq2\), alors \(u_{n+1}=\sqrt{2+u_n}\) appartient à \([\sqrt2,2]\), donc à \([0,2]\). L'initialisation est immédiate.

Pour la croissance, \(u_1=\sqrt2\geq u_0\). La fonction \(x\mapsto\sqrt{2+x}\) est croissante sur \([0,2]\) ; si \(u_n\geq u_{n-1}\), alors \(u_{n+1}\geq u_n\). La suite est donc croissante et majorée par 2 : elle converge.

Si sa limite est \(L\), la continuité de la racine donne \(L=\sqrt{2+L}\), donc \(L^2-L-2=0\). Les racines sont -1 et 2 ; comme \(L\in[0,2]\), \(L=2\).

---

## Partie B — Définition et séries de référence

### Exercice 5 — Condition nécessaire

Étudier la convergence de \(\sum_{n=1}^{\infty}\frac{n}{n+1}\).

**Corrigé.**

Le terme général vérifie \(n/(n+1)\to1\ne0\). La condition nécessaire de convergence n'est pas satisfaite : la série diverge.

### Exercice 6 — Série géométrique

Étudier et, lorsqu'elle existe, calculer
\[
\sum_{n=0}^{\infty}3\left(-\frac12\right)^n.
\]

**Corrigé.**

C'est une série géométrique de premier terme 3 et de raison \(r=-1/2\), avec \( |r|<1\). Elle converge et sa somme vaut
\[
\frac{3}{1-(-1/2)}=\frac{3}{3/2}=2.
\]

### Exercice 7 — Série télescopique

Calculer
\[
\sum_{n=1}^{\infty}\frac{2}{n(n+2)}.
\]

**Corrigé.**

La décomposition en éléments simples donne
\[
\frac{2}{n(n+2)}=\frac1n-\frac1{n+2}.
\]
La somme partielle est
\[
S_N=1+\frac12-\frac1{N+1}-\frac1{N+2}.
\]
En passant à la limite, \(S=3/2\).

### Exercice 8 — Série de Riemann

Étudier \(\sum_{n=1}^{\infty}1/n^{3/2}\) et \(\sum_{n=1}^{\infty}1/\sqrt n\).

**Corrigé.**

Ce sont des p-séries. La première a \(p=3/2>1\), donc converge. La seconde a \(p=1/2\leq1\), donc diverge.

---

## Partie C — Critères de convergence

### Exercice 9 — Comparaison directe

Étudier
\[
\sum_{n=1}^{\infty}\frac1{n^2+3n}.
\]

**Corrigé.**

Pour \(n\geq1\), \(n^2+3n\geq n^2\), donc
\[
0\leq\frac1{n^2+3n}\leq\frac1{n^2}.
\]
La série \(\sum1/n^2\) converge (p-série avec \(p=2\)). Par comparaison, la série demandée converge.

### Exercice 10 — Équivalence

Étudier
\[
\sum_{n=1}^{\infty}\frac{5n+1}{n^3+2}.
\]

**Corrigé.**

On compare à \(1/n^2\) :
\[
\lim_{n\to\infty}
\frac{(5n+1)/(n^3+2)}{1/n^2}
=\lim_{n\to\infty}\frac{5n^3+n^2}{n^3+2}=5.
\]
La limite appartient à \( (0,+\infty)\). Les deux séries sont de même nature ; \(\sum1/n^2\) converge, donc la série donnée converge.

### Exercice 11 — Critère du quotient

Étudier
\[
\sum_{n=1}^{\infty}\frac{n!}{3^n}.
\]

**Corrigé.**

Avec \(a_n=n!/3^n\),
\[
\frac{a_{n+1}}{a_n}=\frac{n+1}{3}\longrightarrow+\infty.
\]
Le terme général ne tend d'ailleurs pas vers zéro ; la série diverge. Le critère du quotient donne aussi la divergence puisque la limite du quotient est strictement supérieure à 1.

### Exercice 12 — Critère de la racine

Étudier
\[
\sum_{n=1}^{\infty}\left(\frac{2n+1}{5n+4}\right)^n.
\]

**Corrigé.**

La racine n-ième du terme vaut
\[
\sqrt[n]{a_n}=\frac{2n+1}{5n+4}\longrightarrow\frac25<1.
\]
Le critère de la racine conclut à la convergence absolue (ici les termes sont positifs, donc à la convergence).

### Exercice 13 — Cas où le quotient ne conclut pas

Étudier \(\sum_{n=1}^{\infty}1/n\) en calculant la limite du quotient \(a_{n+1}/a_n\). Pourquoi faut-il une autre méthode ?

**Corrigé.**

On obtient
\[
\frac{a_{n+1}}{a_n}=\frac{n}{n+1}\longrightarrow1.
\]
Le critère du quotient est muet. Il ne permet ni de conclure à la convergence, ni à la divergence. La série harmonique diverge, par exemple par regroupement des termes en blocs de tailles doublantes.

---

## Partie D — Alternance et convergence absolue

### Exercice 14 — Leibniz et erreur

On considère
\[
S=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}.
\]

1. Justifier la convergence.
2. Donner une borne de l'erreur après 10 termes.
3. La convergence est-elle absolue ?

**Corrigé.**

Les valeurs absolues \(b_n=1/n^2\) sont positives, décroissantes et tendent vers zéro. Leibniz assure la convergence. Après 10 termes,
\[
|S-S_{10}|\leq b_{11}=\frac1{121}\approx0.0082645.
\]
Enfin, \(\sum|a_n|=\sum1/n^2\) converge : la convergence est absolue.

### Exercice 15 — Convergence conditionnelle

Étudier
\[
\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}n.
\]

**Corrigé.**

Les valeurs absolues \(1/n\) décroissent vers zéro ; Leibniz donne la convergence. La série des valeurs absolues est la série harmonique, divergente. La convergence est donc conditionnelle.

### Exercice 16 — Distinguer les trois conclusions

Pour chacune des séries suivantes, donner la nature et le critère pertinent :

(a) \(\sum_{n=1}^{\infty}(-1)^n/\sqrt n\) ;  
(b) \(\sum_{n=1}^{\infty}1/(n\sqrt n)\) ;  
(c) \(\sum_{n=1}^{\infty}(-1)^n\).

**Corrigé.**

(a) Les modules \(1/\sqrt n\) décroissent vers zéro : Leibniz donne la convergence. La série absolue \(\sum1/\sqrt n\) diverge (p = 1/2). Donc convergence conditionnelle.

(b) \(1/(n\sqrt n)=1/n^{3/2}\), p-série avec p = 3/2 > 1 : convergence absolue, puisque les termes sont positifs.

(c) Le terme général \( (-1)^n\) ne tend pas vers zéro. La série diverge par condition nécessaire.

---

## Partie E — Synthèse et raisonnement

### Exercice 17 — Choisir le bon critère

Étudier
\[
\sum_{n=1}^{\infty}\frac{n^2}{2^n}.
\]

**Corrigé.**

Posons \(a_n=n^2/2^n\). Alors
\[
\frac{a_{n+1}}{a_n}
=\frac{(n+1)^2}{2n^2}
\longrightarrow\frac12<1.
\]
Le critère du quotient assure la convergence absolue.

### Exercice 18 — Contrôle d'une erreur numérique

On approche la somme de
\[
\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}
\]
par ses \(N\) premiers termes. Quel entier \(N\) suffit pour garantir une erreur strictement inférieure à \(10^{-5}\), en utilisant uniquement la borne de Leibniz ?

**Corrigé.**

Le reste vérifie \( |R_N|\leq1/(N+1)^2\). Il suffit donc d'imposer
\[
\frac1{(N+1)^2}<10^{-5}
\quad\Longleftrightarrow\quad
N+1>\sqrt{100000}\approx316.228.
\]
Le plus petit entier qui satisfait cette condition est \(N=316\), car \(317^2=100489>100000\). La borne est alors strictement inférieure à \(10^{-5}\).

### Exercice 19 — Preuve par sommes partielles

Montrer que \(\sum_{n=1}^{\infty}1/[n(n+1)]\) converge et calculer sa somme. Puis expliquer pourquoi la seule condition \(a_n\to0\) n'aurait pas suffi.

**Corrigé.**

On écrit
\[
\frac1{n(n+1)}=\frac1n-\frac1{n+1}.
\]
La somme partielle vaut
\[
S_N=1-\frac1{N+1}\longrightarrow1.
\]
La série converge donc vers 1. Le fait que le terme général tende vers zéro est seulement une condition nécessaire ; la série harmonique fournit un contre-exemple à la réciproque.

### Exercice 20 — Détecter une preuve invalide

Un étudiant écrit : « \(a_n=1/n^2\to0\). Donc \(\sum a_n\) converge par le critère du terme général. » Identifier précisément l'erreur et proposer une preuve valide.

**Corrigé.**

Il n'existe pas de critère affirmant que la limite nulle du terme général suffit à établir la convergence. La limite nulle est nécessaire, non suffisante. Pour cette série précise, on reconnaît une p-série avec \(p=2>1\), qui converge. On peut aussi utiliser le critère intégral puisque \(f(x)=x^{-2}\) est positive, continue et décroissante sur \([1,+\infty)\), et que \(\int_1^{\infty}x^{-2}dx=1\) est finie.

---

## Grille d'auto-évaluation

| Compétence | À valider |
|---|---|
| Construire une sous-suite et analyser ses limites | Exercices 1–3 |
| Appliquer convergence monotone et Bolzano–Weierstrass | Exercices 3–4 |
| Calculer des sommes géométriques et télescopiques | Exercices 6–7, 19 |
| Reconnaître les séries de référence | Exercices 8, 13 |
| Choisir et justifier une comparaison | Exercices 9–10 |
| Appliquer quotient et racine sans surinterpréter | Exercices 11–13, 17 |
| Distinguer absolue et conditionnelle | Exercices 14–16 |
| Contrôler une erreur et critiquer une preuve | Exercices 18–20 |

**Critère pédagogique proposé :** viser au moins 16 exercices maîtrisés sur 20, dont obligatoirement les exercices 4, 9, 14, 15 et 20. Ce seuil est une convention de progression du Programme B, pas une norme académique universelle.
