# F04 — Étude universitaire : exponentielle et logarithme

## Compétences visées
Résoudre une équation exponentielle, établir un temps de seuil, relier croissance discrète et continue et analyser les conditions du modèle.

## 1. Fonction exponentielle

Pour une base a strictement positive, \(a\ne1\), la fonction \(x\mapsto a^x\) est strictement monotone : croissante si a>1, décroissante si 0<a<1. Elle est donc injective. Le logarithme en base a est sa fonction réciproque sur les réels positifs.

## 2. Résolution logarithmique

Pour \(a>0,a\ne1,c>0\), l'équation \(a^{f(x)}=c\) équivaut à \(f(x)=\ln(c)/\ln(a)\). La condition c>0 est nécessaire car une exponentielle réelle est strictement positive.

## 3. Croissance discrète et continue

Avec un taux effectif annuel r, \(C_n=C_0(1+r)^n\). En croissance continue, \(C(t)=C_0e^{\delta t}\). Pour avoir le même facteur après une année, il faut \(e^\delta=1+r\), donc \(\delta=\ln(1+r)\).

Le taux continu n'est pas simplement le taux effectif ; il s'agit de son logarithme. Pour r=5 %, \(\delta=\ln(1,05)\approx4,879\%\).

## 4. Exemple travaillé : atteindre un seuil

Un capital croît de 3 % par période. Pour dépasser 150 % du capital initial, il faut \(1,03^n>1,5\), soit \(n>\ln(1,5)/\ln(1,03)\approx13,72\). Le premier nombre entier de périodes est 14. Vérifier directement les périodes 13 et 14 évite une erreur d'arrondi sur le seuil.

## 5. Problèmes progressifs

**P1.** Résoudre \(5^{2x-1}=13\).

**P2.** Un capital croît de 2,5 % par an. Combien d'années entières faut-il pour augmenter de 30 % ?

**P3.** Déterminer le taux continu équivalent à 4,5 % effectif.

## 6. Corrigés

**P1.** \(2x-1=\ln13/\ln5\), donc \(x=(1+\ln13/\ln5)/2\approx1,299\).

**P2.** Chercher \(1,025^n\geq1,30\). Le seuil réel vaut \(\ln1,30/\ln1,025\approx10,62\), donc 11 années entières.

**P3.** \(\delta=\ln1,045\approx0,04402\), soit environ 4,402 % en taux continu.

## 7. Question de défense orale
Pourquoi un modèle exponentiel peut-il convenir sur une période et devenir inadapté à long terme ? Citer au moins deux mécanismes possibles.
