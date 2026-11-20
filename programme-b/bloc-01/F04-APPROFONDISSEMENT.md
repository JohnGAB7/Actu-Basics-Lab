# F04 — Approfondissement : puissances, racines et logarithmes

## 1. Lois des exposants et conditions

Pour \(a,b>0\), \(a^x a^y=a^{x+y}\), \((a^x)^y=a^{xy}\), et \(a^{-x}=1/a^x\). Les extensions aux bases négatives demandent des précautions lorsque l'exposant est réel.

La racine carrée principale \(\sqrt{x}\) est non négative et définie pour \(x\geq0\). Ainsi \(\sqrt{x^2}=|x|\), pas toujours \(x\).

## 2. Logarithme : définition et conséquences

Pour \(a>0\), \(a\ne1\), \(\log_a(x)=y\) signifie \(a^y=x\), avec \(x>0\). Les identités \(\log(xy)=\log x+\log y\) et \(\log(x^r)=r\log x\) supposent des arguments positifs dans le cadre réel.

Le changement de base donne \(\log_a x=\ln(x)/\ln(a)\).

## 3. Résoudre une équation exponentielle

Si \(a>0,a\ne1\) et \(a^{f(x)}=c\) avec \(c>0\), alors \(f(x)=\log_a c\), car la fonction exponentielle de base \(a\) est injective. Si \(c\leq0\), il n'existe pas de solution réelle.

## 4. Croissance exponentielle et intérêts composés

Un capital suit \(C_n=C_0(1+r)^n\) avec capitalisation périodique constante. Le modèle suppose un taux identique à chaque période et le réinvestissement des intérêts. En temps continu, \(C(t)=C_0e^{rt}\). Les deux modèles ne sont pas identiques à horizon fini ; ils se rapprochent sous des conditions de capitalisation de plus en plus fréquente.

## 5. Échelle logarithmique

Le logarithme transforme les produits en sommes et compresse les grandes amplitudes. Une différence de logarithmes \(\ln y_2-\ln y_1\) vaut \(\ln(y_2/y_1)\), un changement relatif multiplicatif. Pour de petites variations, \(\ln(1+t)\approx t\), mais cette approximation devient moins précise quand \(|t|\) augmente.

## 6. Exercices avancés

1. Résoudre \(3^{2x-1}=7\) et vérifier le domaine.
2. Montrer que \(\sqrt{(x-2)^2}=|x-2|\), puis résoudre \(\sqrt{(x-2)^2}=3\).
3. Calculer le taux continu équivalent à un facteur annuel \(1,05\).
4. Comparer \(\ln(1,02)\) à 0,02 et expliquer l'approximation.
5. Un capital croît de 3 % par an. Déterminer le nombre d'années nécessaire pour dépasser 150 % du capital initial.

**À maîtriser :** domaines de définition, lois des puissances, valeur absolue dans les racines, logarithme inverse de l'exponentielle et modélisation de la croissance.