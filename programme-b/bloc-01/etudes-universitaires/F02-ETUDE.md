# F02 — Étude universitaire : rapports, proportions et exposition

## Compétences visées
Construire un indicateur cohérent, prouver une formule de répartition, reconnaître un modèle proportionnel et justifier le dénominateur.

## 1. Taux : la dimension est constitutive de l'indicateur

Un taux s'écrit comme un quotient de grandeurs. Si N est un nombre de sinistres et E une exposition en années-contrats, \(N/E\) a pour unité « sinistre par année-contrat ». Un taux de 0,08 sinistre par année-contrat n'est pas une probabilité individuelle de 8 % sans hypothèses supplémentaires sur le processus générateur des sinistres.

## 2. Propriété : conservation d'un partage proportionnel

Soient des poids \(w_i\geq0\), avec somme strictement positive, et un total T. Posons \(T_i=T w_i/\sum_jw_j\). Alors
\(\sum_iT_i=T\sum_iw_i/\sum_jw_j=T\).
La formule conserve le total et attribue des parts dans le même rapport que les poids.

## 3. Distinguer modèle proportionnel et modèle affine

Le modèle proportionnel \(C(q)=kq\) impose \(C(0)=0\). Le modèle affine \(C(q)=a+kq\) autorise un coût fixe a. Le quotient \(C(q)/q=a/q+k\) varie avec q si a est non nul. Il serait donc erroné de conclure à une proportionnalité en observant seulement que le coût augmente avec le volume.

## 4. Exemple travaillé : fréquence comparée

Portefeuille A : 72 sinistres pour 1 200 années-contrats, soit 0,06 par année-contrat. Portefeuille B : 45 pour 600, soit 0,075. B présente une fréquence observée 25 % plus élevée que A, puisque 0,075/0,06−1=0,25. Ce constat descriptif ne prouve pas que le risque sous-jacent de B est supérieur : composition, période, définition des sinistres et incertitude d'échantillonnage doivent être étudiées.

## 5. Problèmes progressifs

**P1 — Dénominateur.** Un portefeuille compte 80 sinistres et 2 000 contrats, dont l'exposition totale est 1 500 années-contrats. Calculer les deux ratios possibles et dire lequel mesure la fréquence par année d'exposition.

**P2 — Proportionnalité.** Le coût total est \(C(q)=25+1,8q\). Calculer le coût moyen par unité pour q=10 et q=100. Expliquer la convergence vers le coût variable unitaire.

**P3 — Répartition.** Répartir 18 000 € selon les poids 2, 3, 7. Vérifier la conservation du total et discuter le cas où un poids vaut zéro.

## 6. Corrigés

**P1.** 80/2 000=0,04 sinistre par contrat ; 80/1 500≈0,0533 sinistre par année-contrat. Le second utilise l'exposition temporelle et son unité doit être conservée.

**P2.** Pour q=10 : C=43 €, soit 4,30 €/unité. Pour q=100 : C=205 €, soit 2,05 €/unité. Le coût moyen vaut 25/q+1,8 et tend vers 1,8 lorsque q augmente sans borne.

**P3.** Somme des poids=12. Parts : 3 000 €, 4 500 €, 10 500 €. Leur somme vaut 18 000 €. Un poids nul reçoit une part nulle, sans invalider la formule si la somme des poids reste strictement positive.

## 7. Question de défense orale
Pourquoi une fréquence observée de 0,06 sinistre par année-contrat n'est-elle pas automatiquement une probabilité de sinistre de 6 % ?
