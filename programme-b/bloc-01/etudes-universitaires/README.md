# Études universitaires — Bloc 1

Ce dossier fait passer les huit cours de fondation vers une pratique plus universitaire : formalisation, démonstration, étude de cas, analyse des hypothèses et résolution argumentée.

## Parcours
1. Lire le dossier du cours en comprenant les hypothèses.
2. Refaire les exemples sans regarder la solution.
3. Résoudre les problèmes de transfert.
4. Comparer son raisonnement au corrigé et noter les erreurs.
5. Défendre oralement le modèle choisi et ses limites.

| Dossier | Axe de travail |
|---|---|
| [F01](F01-ETUDE.md) | Ensembles, ordre, approximation et numération |
| [F02](F02-ETUDE.md) | Rapports, taux, proportionnalité et exposition |
| [F03](F03-ETUDE.md) | Variations composées, indices et taux moyens |
| [F04](F04-ETUDE.md) | Exponentielle, logarithme et croissance |
| [F05](F05-ETUDE.md) | Identités, factorisation et domaines |
| [F06](F06-ETUDE.md) | Équations, inéquations et systèmes |
| [F07](F07-ETUDE.md) | Fonctions, réciproques et composition |
| [F08](F08-ETUDE.md) | Géométrie analytique, unités et visualisation |
| [Cas intégrateur](EVALUATION-TRANSVERSALE.md) | Analyse d'un portefeuille, décomposition et limites |
| [Corrigés détaillés des 24 problèmes](CORRIGES-PROBLEMES.md) | Démonstrations, calculs, vérifications et interprétations |
| [Examen final (2 h)](EXAMEN-FINAL-BLOC-1.md) | Évaluation individuelle sur 100 points |
| [Feuille de réponses vierge](FEUILLE-REPONSES-EXAMEN.md) | Copie structurée sans les solutions |
| [Corrigé et barème de l'examen](CORRIGE-EXAMEN-FINAL.md) | Solutions détaillées et grille de notation |
| [Diagnostic et remédiation](DIAGNOSTIC-ET-REMEDIATION.md) | Identifier les lacunes et organiser la reprise |
| [Passerelle vers l'analyse mathématique](PASSERELLE-ANALYSE-FONDAMENTALE.md) | Logique, preuves, suites, limites et continuité |
| [Exercices et corrigés de la passerelle](EXERCICES-PASSERELLE-ANALYSE.md) | 16 exercices progressifs et problèmes de synthèse |
| [Complétude de R, supremum et Cauchy](COMPLETUDE-REELS-SUPREMUM-CAUCHY.md) | Structure ordonnée, propriété de la borne supérieure, densité et complétude |
| [Exercices sur la complétude](EXERCICES-COMPLETUDE-REELS.md) | 16 exercices et corrigés détaillés |
| [Suites et séries numériques](SUITES-SERIES-CONVERGENCE.md) | Sous-suites, Bolzano–Weierstrass, séries, critères et convergence absolue/conditionnelle |
| [Exercices corrigés — suites et séries](EXERCICES-SUITES-SERIES.md) | 20 exercices progressifs avec solutions détaillées |
| [Topologie élémentaire de R](TOPOLOGIE-ELEMENTAIRE-R.md) | Ouverts, fermés, adhérence, compacité, connexité et continuité |
| [Exercices corrigés — topologie de R](EXERCICES-TOPOLOGIE-R.md) | 20 exercices avec preuves et contre-exemples |
| [Limites de fonctions et continuité](LIMITES-FONCTIONS-CONTINUITE.md) | Epsilon-delta, limites latérales, caractérisation séquentielle, continuité, TVI, extrema et continuité uniforme |
| [Exercices corrigés — limites et continuité](EXERCICES-LIMITES-CONTINUITE.md) | 20 exercices progressifs avec preuves et corrigés détaillés |

## Modalités de travail recommandées

- **Étape 1 — Apprentissage :** étudier les huit fiches F01 à F08 et refaire les exemples.
- **Étape 2 — Entraînement :** résoudre les 24 problèmes sans consulter les corrigés.
- **Étape 3 — Évaluation :** imprimer ou copier la feuille de réponses, puis passer l'examen final en 2 heures, sans cours, avec calculatrice scientifique simple.
- **Étape 4 — Correction active :** comparer les démarches, pas seulement les résultats ; consigner les erreurs récurrentes.
- **Étape 5 — Remédiation :** utiliser le diagnostic pour reprendre les compétences déficitaires et passer un mini-test de transfert.

## Passerelle préparatoire — analyse mathématique

La passerelle est une extension préparatoire du Bloc 1, et non l'ouverture du Bloc 2. Elle formalise les outils nécessaires à l'analyse réelle : logique, quantificateurs, méthodes de démonstration, suites réelles, convergence, limites de fonctions et continuité.

Un second dossier approfondit maintenant la complétude de R : supremum, infimum, propriété archimédienne, densité de Q, intervalles emboîtés et suites de Cauchy. Il explicite pourquoi les propriétés de convergence dépendent de l'ensemble numérique dans lequel on travaille.

Ordre conseillé : lire les cours, refaire les démonstrations à la main, résoudre les exercices sans consulter les corrigés, puis vérifier les hypothèses et les preuves. La nouvelle étude sur les limites et la continuité approfondit les notions évoquées dans la passerelle : epsilon-delta, limites latérales, caractérisation séquentielle, discontinuités, TVI, extrema et continuité uniforme. Les dérivées et intégrales restent hors périmètre.

## Vérification numérique

Des scripts indépendants contrôlent les principaux résultats numériques de l'examen :
- [Python — vérification du Bloc 1](../ateliers/python/verification_bloc1.py)
- [R — vérification du Bloc 1](../ateliers/r/verification_bloc1.R)

Le script Python utilise uniquement la bibliothèque standard. Le script R utilise R de base. Ils vérifient des valeurs de référence et des identités numériques ; ils ne corrigent pas une copie et ne remplacent pas une démonstration. Le script Python a été exécuté avec succès dans l'environnement de travail. Le script R n'a pas été exécuté dans un environnement R au cours de cette étape.

## Niveau et limites

Les dossiers F01–F08 proposent un approfondissement de niveau universitaire introductif/intermédiaire. La passerelle ajoute une initiation rigoureuse aux preuves et à l'analyse réelle élémentaire. Ces documents ne constituent pas un traité exhaustif d'analyse, d'algèbre ou de calcul numérique.

## Règle de qualité

Toute réponse doit distinguer : données, hypothèses, définition du modèle, calcul, résultat, interprétation et limites. Une valeur numérique correcte obtenue par un raisonnement invalide ne vaut pas validation complète.

Les seuils de notation figurant dans les documents sont des conventions pédagogiques proposées pour ce cursus, et non des normes académiques universelles.
