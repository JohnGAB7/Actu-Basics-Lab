# Évaluation transversale — Bloc 1

## Cas intégrateur : analyse d'un portefeuille simplifié

Un portefeuille est observé sur deux périodes. Les données sont :

| Indicateur | Période 1 | Période 2 |
|---|---:|---:|
| Contrats moyens exposés | 1 000 | 1 200 |
| Exposition (années-contrats) | 900 | 1 080 |
| Nombre de sinistres | 54 | 70 |
| Coût moyen par sinistre (€) | 420 | 450 |
| Frais fixes (€) | 8 000 | 8 500 |

Le coût total des sinistres est le nombre de sinistres multiplié par le coût moyen. La charge totale considérée dans l'exercice est le coût des sinistres augmenté des frais fixes.

## Travail demandé

1. Vérifier la cohérence des grandeurs et préciser leurs unités.
2. Calculer la fréquence par année-contrat pour chaque période.
3. Calculer la variation relative de la fréquence.
4. Calculer le coût total des sinistres et la charge totale de chaque période.
5. Décomposer la variation de la charge totale entre effet du nombre de sinistres, effet du coût moyen et frais fixes. Présenter une décomposition séquentielle et préciser que l'attribution dépend de l'ordre retenu.
6. Construire un indice base 100 de la charge totale.
7. Construire un graphique comparant fréquence et charge, en expliquant pourquoi les unités nécessitent deux axes ou deux graphiques.
8. Écrire une fonction de calcul de fréquence avec validation du dénominateur strictement positif (pseudo-code, Python ou R).
9. Énoncer au moins trois limites de l'analyse : deux périodes seulement, exposition agrégée, absence de segmentation, incertitude statistique, changements de définition ou de mix.

## Corrigé indicatif

### 1. Fréquences

Période 1 : 54/900=0,06 sinistre par année-contrat. Période 2 : 70/1 080≈0,0648148 sinistre par année-contrat.

Variation relative : 0,0648148/0,06−1≈8,02 %.

### 2. Charges

Période 1 : sinistres=54×420=22 680 €. Charge totale=22 680+8 000=30 680 €.

Période 2 : sinistres=70×450=31 500 €. Charge totale=31 500+8 500=40 000 €.

Variation de la charge totale : 40 000/30 680−1≈30,38 %.

### 3. Indice

Base 100 en période 1 : période 1=100 ; période 2=100×40 000/30 680≈130,38.

### 4. Décomposition séquentielle

En passant d'abord le nombre de sinistres de 54 à 70 au coût moyen initial : effet volume=(70−54)×420=6 720 €.

Puis en passant le coût moyen de 420 à 450 sur 70 sinistres : effet coût=70×(450−420)=2 100 €.

Effet frais fixes=500 €. Total des effets=6 720+2 100+500=9 320 €, égal à 40 000−30 680.

Cette décomposition est exacte mais dépend de l'ordre : appliquer d'abord le changement de coût moyen au nombre initial de sinistres attribuerait différemment le terme d'interaction. Il faut documenter la convention.

### 5. Limites

Les chiffres ne permettent pas à eux seuls d'inférer une tendance durable, d'expliquer les causes de la hausse, de quantifier l'incertitude, ni de contrôler la composition du portefeuille. La fréquence est un ratio observé ; l'interprétation causale exige des données et une méthode supplémentaires.

## Barème proposé sur 100

| Critère | Points |
|---|---:|
| Unités, définitions et contrôles de cohérence | 10 |
| Calculs de fréquence et variation | 15 |
| Calcul des charges et indice | 15 |
| Décomposition et vérification | 20 |
| Qualité du graphique et interprétation | 10 |
| Fonction de calcul et validation | 10 |
| Analyse critique des limites | 15 |
| Clarté, traçabilité et présentation | 5 |

## Règles de validation

- 80/100 est un seuil pédagogique proposé, pas une norme académique universelle.
- Toute erreur de dénominateur ou d'unité doit être corrigée avant validation.
- Une réponse numérique sans méthode ne reçoit pas tous les points.
- Les résultats arrondis doivent conserver suffisamment de précision pendant les calculs.
- Les choix de décomposition et de visualisation doivent être explicités.
