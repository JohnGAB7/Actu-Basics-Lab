# F03 — Étude universitaire : variations composées et indices

## Compétences visées
Composer des taux, retrouver un taux constant équivalent, rebaser un indice et expliquer les différences entre variations absolues, relatives et en points.

## 1. Théorème de composition

Si \(V_{t+1}=V_t(1+r_t)\), alors par substitutions successives
\(V_n=V_0\prod_{t=0}^{n-1}(1+r_t)\).
Le facteur global est le produit des facteurs périodiques. Le taux global est ce produit moins 1.

Cette formule suppose que chaque taux s'applique à la valeur issue de la période précédente et que la grandeur reste comparable d'une période à l'autre.

## 2. Taux moyen géométrique

Pour des facteurs positifs \(g_1,\ldots,g_n\), le facteur constant équivalent \(\bar g\) vérifie \(\bar g^n=\prod g_i\). Donc \(\bar g=(\prod g_i)^{1/n}\). Le taux composé moyen est \(\bar r=\bar g-1\).

La moyenne arithmétique des taux ne répond généralement pas à cette question. Elle peut être utile pour d'autres objectifs statistiques, mais ne reproduit pas le facteur cumulé.

## 3. Rebasage d'un indice

Si \(I_t=100X_t/X_0\), alors l'indice en base s devient \(I_t^{(s)}=100X_t/X_s=100I_t/I_s\). Le rebasage change l'échelle de référence, pas les rapports entre les niveaux de la série.

## 4. Exemple travaillé

Un montant augmente de 12 %, puis baisse de 10 %. Facteur global : 1,12×0,90=1,008, soit +0,8 %. Le taux arithmétique moyen des deux taux est +1 %, mais le taux géométrique par période vaut \(\sqrt{1,008}-1\approx0,3992\%\). Les deux moyennes répondent à des questions différentes.

## 5. Problèmes progressifs

**P1.** Une série évolue de +5 %, +5 %, puis −8 %. Calculer le taux global.

**P2.** Un indice vaut 96 en base initiale à t=1 et 120 à t=3. Rebaser t=3 à 100 en t=1.

**P3.** Un taux d'impayés passe de 4 % à 5 %. Exprimer l'écart en points de pourcentage et la variation relative.

## 6. Corrigés

**P1.** Facteur global=1,05×1,05×0,92=1,0143, soit +1,43 %.

**P2.** 100×120/96=125. L'indice indique une hausse de 25 % entre t=1 et t=3.

**P3.** Écart=1 point de pourcentage. Variation relative=(5−4)/4=25 %.

## 7. Question de défense orale
Dans quelle situation la moyenne arithmétique de taux peut-elle être pertinente, même si elle ne donne pas le taux composé équivalent ?
