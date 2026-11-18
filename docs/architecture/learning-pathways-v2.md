# ACTU-BASICS — Architecture de progression des connaissances en statistiques

Version 2.0 · 18 novembre 2026

## Décision pédagogique

ACTU-BASICS devient un parcours de maîtrise, et non une simple liste de vidéos. L'apprenant doit savoir formuler une question, identifier et contrôler les données, les décrire, raisonner sur le hasard, quantifier l'incertitude, construire et diagnostiquer des modèles, puis conduire une analyse reproductible et communiquer ses limites.

Principes :
- Comprendre avant de calculer : question concrète, intuition, visualisation, formalisation, pratique.
- Mathématiques à la demande : fractions, ratios, pourcentages, algèbre, logarithmes, dérivées, intégrales et matrices apparaissent au moment utile. Pas de long tunnel préalable.
- Excel, VBA, Python et R sont des voies d'application, jamais des substituts au raisonnement.
- Même jeu de données, définitions, unités, conventions et tolérances dans les quatre logiciels.
- Distinguer leçon publiée, script source, fiche de conception et entrée de syllabus.
- Ne jamais faire dire aux données plus qu'elles ne permettent.
- Apprentissage actif : prédire, manipuler, expliquer, corriger et transférer.
- Sources, éditions, dates, licences et conventions traçables.

## P0 — Socle opérationnel ciblé (diagnostic, pas un cours-barrière)
Compétences mobilisables : calcul numérique ; fractions, ratios et pourcentages ; unités et ordres de grandeur ; lecture de tableaux/graphes ; notation, indices, sommes et équations ; puissances, racines, exponentielle, logarithme ; fonctions, dérivées, intégrales et matrices.

Règle : diagnostic court, capsule contextuelle, mini-exercice. Le cours principal continue dès que le prérequis local est acquis. Le calcul avancé ne bloque pas la statistique descriptive.

## P1 — Littératie statistique et données
Résultat : poser une question mesurable, comprendre ce qui a été observé et repérer les biais de mesure.
1. Question statistique et variabilité.
2. Population, individu, observation, variable et paramètre.
3. Types de variables, échelles de mesure et unités.
4. Provenance, collecte, sondage et recensement.
5. Échantillon, représentativité et biais de sélection.
6. Observation, expérience, randomisation et confusion.
7. Données manquantes, erreurs et valeurs aberrantes.
8. Pourcentages, taux, dénominateurs et points de pourcentage.
9. Lire et critiquer les graphiques.
10. Éthique, confidentialité et reproductibilité.
Évaluation : auditer une affirmation chiffrée et expliquer si les données répondent réellement à la question.

## P2 — Décrire et explorer les données
Résultat : résumer une distribution sans masquer sa forme, sa variabilité ou ses anomalies.
1. Tableaux, fréquences et distributions empiriques.
2. Barres, histogrammes, densités et ECDF.
3. Forme : asymétrie, queues et multimodalité.
4. Moyenne, médiane, mode et quantiles.
5. Variance, écart-type, étendue et écart interquartile.
6. Standardisation et scores z.
7. Valeurs atypiques, influence et robustesse.
8. Comparaison de groupes et stratification.
9. Tableaux croisés, nuages de points et corrélation descriptive.
10. Analyse exploratoire complète.
Évaluation : produire un rapport exploratoire et justifier chaque indicateur.

## P3 — Probabilités et modélisation du hasard
Résultat : passer des fréquences observées à un modèle probabiliste.
1. Fréquence, probabilité, risque et incertitude.
2. Expériences, événements et règles de calcul.
3. Dénombrement utile : principe multiplicatif et combinaisons.
4. Probabilité conditionnelle, arbres et indépendance.
5. Probabilités totales et théorème de Bayes.
6. Variables aléatoires discrètes et continues.
7. Espérance, variance, covariance et quantiles.
8. Bernoulli, binomiale, géométrique et Poisson.
9. Uniforme, normale, exponentielle, Gamma et Beta.
10. Lois jointes, marginales et conditionnelles.
11. Simulation, loi des grands nombres et théorème central limite.
12. Convergence, approximation et limites des modèles.
Évaluation : choisir une loi, justifier les hypothèses, calculer ou simuler, interpréter.

## P4 — Échantillonnage et inférence
Résultat : quantifier l'incertitude et distinguer estimation, intervalle et décision.
1. Population, échantillon, paramètre et statistique.
2. Mécanismes d'échantillonnage et biais.
3. Distribution d'échantillonnage et erreur standard.
4. TCL appliqué à l'inférence.
5. Estimateurs : biais, variance, EQM et consistance.
6. Vraisemblance et maximum de vraisemblance.
7. Intervalles de confiance.
8. Tests d'hypothèses, statistique et région critique.
9. P-value et mésinterprétations.
10. Erreurs de type I/II, puissance et taille d'échantillon.
11. Inférence sur une et deux moyennes/proportions.
12. Khi-deux et test exact de Fisher.
13. Tests non paramétriques et permutation.
14. Bootstrap et rééchantillonnage.
15. Comparaisons multiples.
Évaluation : sélectionner une procédure, justifier ses hypothèses et rédiger une conclusion proportionnée.

## P5 — Modèles statistiques et relations
Résultat : construire, interpréter et diagnostiquer des modèles sans confondre association, prédiction et causalité.
1. Association, corrélation et causalité.
2. Régression linéaire simple : géométrie et moindres carrés.
3. Résidus, ajustement et prédiction.
4. Inférence sur les coefficients.
5. Régression multiple et interprétation conditionnelle.
6. Multicolinéarité, interactions et variables catégorielles.
7. Hétéroscédasticité, dépendance et diagnostics.
8. Sélection, validation et surapprentissage.
9. ANOVA et comparaisons de groupes.
10. Régression logistique et odds ratios.
11. GLM : composante aléatoire, prédicteur et lien.
12. Poisson, binomiale négative, Gamma et Tweedie.
13. Modèles robustes, régularisation, quantile et GAM.
14. Validation croisée, calibration et performance.
Évaluation : défendre un modèle et diagnostiquer ses limites.

## P6 — Méthodes avancées et spécialités
- Bayésien : prior, vraisemblance, posterior, prédiction, modèles hiérarchiques.
- Multivarié : ACP, analyse factorielle, discriminante, clustering.
- Séries temporelles : tendance, saisonnalité, stationnarité, ARIMA, volatilité.
- Survie : censure, Kaplan–Meier, log-rank, Cox.
- Causalité : randomisation, DAG, variables instrumentales, différences-de-différences.
- Calcul scientifique : Monte-Carlo, bootstrap avancé, optimisation.
- Processus stochastiques : chaînes de Markov, processus de Poisson.
- Apprentissage statistique : régularisation, arbres, ensembles, validation, interprétabilité.

Évaluation : problème ouvert, choix méthodologique, analyse reproductible et discussion des limites.

## P7 — Expertise, recherche et communication
Livrables : protocole documenté, dictionnaire de données, plan de contrôle qualité, analyse reproductible, rapport technique, synthèse pour décideur, revue critique d'un article, réplication ou extension d'un résultat. L'expertise se démontre par des projets.

## Mathématiques sans tunnel
| Rencontre avec… | Capsule utile |
|---|---|
| Taux et proportions | fractions, ratios, pourcentages, dénominateurs |
| Moyenne et variance | sommes, indices, carré, racine |
| Loi binomiale | factorielle et combinaisons |
| Densité continue | aire, intégrale, fonction de répartition |
| Vraisemblance | produit, logarithme, dérivée, optimisation |
| Régression multiple | vecteurs, matrices, projection |
| GLM exponentiel | exponentielle, logarithme, lien |
| Asymptotique | suites, convergence, approximation |

Chaque capsule justifie son utilité, donne le minimum indispensable, distingue extension facultative et inclut un exercice de transfert.

## Les quatre voies logicielles
**Excel :** fonctions statistiques, tableaux structurés, filtres, TCD, graphiques, validation, Power Query, Analysis ToolPak, audit du classeur.

**Excel VBA :** modèle objet Excel, variables, conditions, boucles, procédures, automatisation de nettoyages/calculs/rapports, gestion d'erreurs et tests. VBA est optionnel et ciblé sur l'automatisation.

**Python :** bases utiles, NumPy, pandas, Matplotlib, SciPy, statsmodels, scikit-learn, notebooks reproductibles.

**R :** objets, vecteurs, facteurs, data frames, base R, tidyverse, ggplot2, distributions, tests, modèles, diagnostics, Quarto/R Markdown.

Règle : voie principale recommandée et autres ateliers pertinents. Ne pas forcer les quatre environnements pour une notion purement conceptuelle. Si comparaison, conserver données, traitements, conventions, paramètres et tolérances identiques.

## Contrat éditorial d'une leçon
1. Question authentique.
2. Prédiction avant réponse.
3. Expérience, graphique ou simulation.
4. Intuition expliquée clairement.
5. Définition formelle et notations.
6. Démonstration raisonnée sans saut algébrique inutile.
7. Exemple numérique intégral, unités et interprétation.
8. Contre-exemple ou cas limite.
9. Ateliers logiciels pertinents.
10. Interprétation de la sortie : ce qui est calculé et non prouvé.
11. Erreurs conceptuelles, numériques, de code et de communication.
12. Exercices gradués et corrections détaillées.
13. Synthèse : quoi retenir et quand utiliser la méthode.
14. Sources et prolongements.

La vidéo n'est qu'une modalité : page de leçon, interaction, notebook/classeur et exercices corrigés forment l'expérience.

## Production audiovisuelle
Vidéo conceptuelle de 6–12 minutes si une narration continue apporte une valeur ; tutoriels logiciels séparés de 4–12 minutes. Voix off claire, textes discrets synchronisés, graphiques fidèles, axes et unités explicites, sous-titres et transcription. Une version muette est complémentaire, jamais le seul cours final. Chaque animation doit enseigner.

## Évaluation de maîtrise
A : reconnaître et expliquer. B : calculer et appliquer. C : choisir et justifier. D : diagnostiquer, comparer et critiquer. E : transférer à un problème nouveau et produire une analyse autonome. La maîtrise se démontre sur un contexte différent de l'exemple guidé.

## Première tranche de production
1. S1.01 — Qu'est-ce qu'une donnée ?
2. S1.02 — Population, individu, variable.
3. S1.03 — Types de variables et échelles de mesure.
4. S1.04 — D'où viennent les données ?
5. S1.05 — Échantillon et biais de sélection.
6. S1.06 — Observer ou expérimenter.
7. S1.07 — Données manquantes, erreurs et définitions changeantes.
8. S2.01 — Fréquences et tableaux.
9. S2.02 — Barres et histogrammes.
10. S2.03 — Forme d'une distribution.
11. S2.04 — La moyenne.
12. S2.05 — Moyenne ou médiane ?
13. S2.06 — Quantiles, quartiles et boxplot.
14. S2.07 — Dispersion.
15. S2.08 — Variance et écart-type.

La nature de la donnée et les limites de mesure précèdent le résumé des distributions. Pourcentages et lecture graphique sont enseignés quand ils sont utilisés : aucun module mathématique complet n'est préalable aux statistiques descriptives.

## Sources universitaires et techniques vérifiées le 18 novembre 2026
- MIT OpenCourseWare, 18.05 Introduction to Probability and Statistics (Spring 2022) : https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
- Harvard Statistics 110, Joe Blitzstein : https://stat110.hsites.harvard.edu/about
- Harvard Department of Statistics, undergraduate FAQ : https://statistics.fas.harvard.edu/frequently-asked-questions
- Penn State STAT 200 : https://online.stat.psu.edu/stat200/
- Penn State Lesson 0 : https://online.stat.psu.edu/stat200/Lesson00
- OpenIntro Statistics : https://www.openintro.org/book/os/
- NIST/SEMATECH e-Handbook : https://www.itl.nist.gov/div898/handbook/
- An Introduction to Statistical Learning, R/Python : https://www.statlearning.com/
- R Project, An Introduction to R : https://cran.r-project.org/doc/manuals/r-release/R-intro.html
- Microsoft Analysis ToolPak : https://support.microsoft.com/fr-fr/excel/use-the-analysis-toolpak-to-perform-complex-data-analysis
- Microsoft Excel VBA reference : https://learn.microsoft.com/en-us/office/vba/api/overview/excel

MIT structure probabilité, Bayes, tests, intervalles, rééchantillonnage et régression, avec R/simulation ; Harvard Stat 110 développe le langage probabiliste, variables, distributions, moments et limites ; Penn State articule collecte, description, intervalles, tests, normalité, inférence, ANOVA, khi-deux et régression, avec prérequis brefs ; OpenIntro propose des laboratoires R/Python ; NIST insiste sur EDA, anomalies et hypothèses ; ISLR/ISLP relie statistique et apprentissage statistique. Cette architecture est une synthèse originale et non le syllabus officiel d'une université.

## Gouvernance des sources
Privilégier cours officiels, manuels ouverts, notes professorales publiées, normes et documentations officielles. Remonter à la source primaire lorsque possible. Relever auteur, institution, édition, chapitre, URL, licence et date. Vérifier formules et exemples par calcul indépendant. Ne pas copier les supports propriétaires. Signaler conventions alternatives : variance n/n−1, quantiles, degrés de liberté, tests exacts/asymptotiques. Toute affirmation empirique ou historique doit être contextualisée et sourcée.
