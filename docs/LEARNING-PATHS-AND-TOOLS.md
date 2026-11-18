# Architecture pédagogique — des fondations à l'expertise

## Décision de conception

ACTU-BASICS LAB n'est pas une simple collection de vidéos ou de fiches. C'est une plateforme de formation progressive qui doit permettre à un apprenant de partir de zéro, construire une compréhension mathématique et statistique solide, appliquer les méthodes avec des outils réels, puis démontrer une expertise par des projets reproductibles.

Le programme existant de 320 unités est une source de curriculum, pas une promesse que 320 cours sont déjà rédigés ou publiés. Les statuts de validation et la provenance des contenus restent obligatoires.

## 1. Architecture en cinq paliers

| Palier | Finalité | Compétences attendues | Preuve d'acquisition |
|---|---|---|---|
| 1. Fondations | Comprendre les langages mathématiques | Calcul, fractions, ratios, pourcentages, puissances, algèbre, fonctions, notation, graphiques, unités | Résoudre et expliquer des problèmes élémentaires |
| 2. Socle quantitatif | Décrire et raisonner avec les données et le hasard | Types de variables, populations, échantillons, statistiques descriptives, visualisation, probabilités, distributions, estimation, incertitude | Analyser un jeu de données simple et justifier les conclusions |
| 3. Pratique appliquée | Choisir et mettre en œuvre une méthode | Tests, régression, modèles, simulation, séries temporelles, économétrie, validation, qualité des données | Étude de cas documentée, calculs contrôlés et interprétation |
| 4. Spécialisation | Développer une expertise dans un domaine | Méthodes avancées, hypothèses, diagnostics, limites, décisions sectorielles | Projet spécialisé évalué sur la méthode et le raisonnement |
| 5. Maîtrise | Concevoir un travail de bout en bout | Cadrage, données, méthode, code, validation, reproductibilité, communication et gouvernance | Projet intégrateur/portfolio défendable et reproductible |

Les paliers ne doivent pas être présentés comme des niveaux scolaires rigides. Chaque unité doit déclarer ses prérequis, ses objectifs observables et les compétences qu'elle permet de mobiliser. Des tests de positionnement et des passerelles permettront de ne pas imposer des répétitions inutiles.

## 2. Domaines et passerelles

- **Socle commun :** mathématiques, statistiques, probabilités, programmation et qualité des données.
- **Statistiques, probabilités et data science :** description, inférence, modélisation, simulation, économétrie, séries temporelles et machine learning.
- **Mathématiques financières :** intérêts, actualisation, flux, taux, obligations, valorisation et risque financier.
- **Sciences actuarielles :** fréquence et coût des sinistres, prime pure, mutualisation, tarification, provisionnement, assurance vie/non-vie, réassurance, ALM et gestion des risques.

Les trois spécialisations réutilisent le socle commun. Les prérequis doivent être visibles et les liens entre unités doivent être représentés comme un graphe de dépendances, pas seulement comme un ordre de lecture.

## 3. Les quatre outils comme fils pratiques explicites

Les outils ne sont pas quatre traductions obligatoires de chaque leçon. Ils sont choisis selon le type de travail à apprendre.

### Excel — analyse et communication métier
- Fondations : cellules, références, formules, types, dates, tableaux et contrôles.
- Intermédiaire : tris, filtres, fonctions statistiques, graphiques, tableaux croisés, recherche, nettoyage et analyse de scénarios.
- Avancé : Power Query, modèles de données, contrôles de qualité, tableaux de bord, sensibilité et validation.
- Livrable : classeur documenté, contrôlé, lisible et auditable.

### Excel VBA — automatisation raisonnée
- Fondations : éditeur, macros, variables, types, conditions et boucles.
- Intermédiaire : procédures, fonctions, tableaux, plages, feuilles, classeurs et gestion des erreurs.
- Avancé : automatisation de rapports, contrôles, imports, génération de livrables et maintenance.
- Livrable : outil automatisé avec code commenté, contrôles et procédure d'utilisation.
- Règle : ne pas enseigner VBA pour remplacer une formule simple ou automatiser une tâche qui ne le justifie pas.

### Python — programmation, données et systèmes
- Fondations : syntaxe, variables, structures, conditions, boucles, fonctions, modules et environnements.
- Intermédiaire : notebooks, fichiers, NumPy, pandas, visualisation, SQL et tests.
- Avancé : simulation, statistiques, machine learning, APIs, pipelines, performance et déploiement.
- Livrable : analyse ou pipeline reproductible, testé et documenté.

### R — statistique, modélisation et recherche reproductible
- Fondations : objets, vecteurs, data frames, fonctions, import et transformations.
- Intermédiaire : tidyverse/data.table, visualisation, statistique descriptive et inférentielle, rapports Quarto/R Markdown.
- Avancé : modèles, GLM/GAM, simulation, séries temporelles, méthodes spécialisées et validation.
- Livrable : rapport statistique reproductible avec code, diagnostics, hypothèses et interprétation.

## 4. Gabarit de chaque leçon

Chaque unité publiée doit, selon sa nature, suivre le fil :
1. Question concrète et objectif d'apprentissage.
2. Intuition, exemple et représentation visuelle.
3. Définition et formalisation mathématique/statistique.
4. Exemple résolu pas à pas.
5. Pratique guidée, puis exercice autonome.
6. Correction argumentée et erreurs fréquentes.
7. Atelier logiciel pertinent (Excel, VBA, Python ou R — pas nécessairement les quatre).
8. Interprétation, hypothèses, limites et vérification.
9. Synthèse, prérequis et liens vers la suite du parcours.

Les ateliers logiciels doivent employer les mêmes données ou un problème comparable afin de faire comprendre ce qui est transférable et ce qui dépend de l'outil.

## 5. Progression de l'expertise

La complexité doit augmenter sur plusieurs axes, pas seulement par la difficulté des formules :
- autonomie dans le choix d'une méthode ;
- taille, qualité et complexité des données ;
- rigueur des hypothèses et diagnostics ;
- reproductibilité et qualité du code ;
- capacité à expliquer l'incertitude et les limites ;
- conséquences de la décision prise à partir de l'analyse.

Un cours avancé n'est pas simplement un cours plus long : il exige un jugement méthodologique plus autonome.

## 6. Règles éditoriales et de qualité

- Préserver les contenus sources, hypothèses, unités, exemples, corrections et statuts de validation.
- Ne publier comme leçon que les contenus dont le statut source autorise la publication.
- Distinguer explicitement unité au programme, script, vidéo, atelier logiciel et leçon web.
- Ne jamais gonfler les statistiques de publication : les 320 unités sont le programme cible, pas 320 leçons finalisées.
- Ajouter les ateliers logiciels progressivement, avec fichiers d'exercice, corrigés et tests.
- Valider les exemples numériques indépendamment et maintenir une parité FR/EN.
- Mesurer l'acquisition par des exercices et projets, pas seulement par le visionnage.

## 7. Ordre de réalisation recommandé

1. Stabiliser les fondations M0/M1 et cartographier les prérequis.
2. Construire le socle statistique et probabiliste en progression cohérente.
3. Ajouter les premiers ateliers Excel au moment où les données et tableaux deviennent pertinents.
4. Introduire VBA pour l'automatisation de cas répétitifs.
5. Développer les fils Python et R en parallèle, en explicitant leurs rôles respectifs.
6. Construire les passerelles vers l'économétrie, la finance quantitative et l'actuariat.
7. Créer des projets intégrateurs et une grille d'évaluation de l'expertise.

## 8. État de livraison

Cette architecture définit la cible pédagogique. Elle ne signifie pas que tous les modules, ateliers ou projets existent déjà. La bibliothèque doit continuer à distinguer le contenu publié, les scripts sources et les unités à développer. Les prochaines intégrations seront réalisées par lots validés et testés.
