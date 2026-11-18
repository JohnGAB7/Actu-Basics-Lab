# ACTU-BASICS — Protocole de qualité scientifique et éditoriale

Version 1.0 · Proposition de gouvernance · 19 novembre 2026

## 1. Objectif

Rendre chaque affirmation pédagogique vérifiable, chaque exemple numérique reproductible et chaque adaptation bilingue fidèle. Une leçon élégante mais scientifiquement incorrecte n'est pas publiable.

## 2. Registre des sources

Pour chaque source utilisée, enregistrer :
- auteur ou institution ;
- titre exact, édition et date ;
- chapitre, section, page ou numéro de cours ;
- URL stable et date de consultation ;
- type de source : cours, manuel, article, norme, documentation ;
- licence ou conditions de réutilisation ;
- affirmation ou partie de leçon étayée ;
- limites, incertitudes et éventuels désaccords entre sources.

Hiérarchie indicative :
1. article original, norme, documentation officielle ou source primaire pertinente ;
2. manuel universitaire reconnu ou cours institutionnel ;
3. notes de cours professorales publiées ;
4. ressource pédagogique secondaire de qualité ;
5. discussion communautaire, uniquement comme piste à vérifier.

Le prestige de l'institution ne dispense jamais de vérifier l'affirmation précise.

## 3. Registre des affirmations

Les affirmations importantes doivent être reliées à une source et à un emplacement précis. Distinguer :
- définition ou convention ;
- théorème ou résultat mathématique ;
- fait empirique ;
- recommandation méthodologique ;
- illustration fictive créée pour enseigner.

Une illustration fictive ne doit jamais être présentée comme une observation réelle. Une recommandation ne doit pas être déguisée en théorème.

## 4. Vérification des calculs

Pour tout exemple quantitatif :
1. écrire les données, unités, hypothèses et conventions ;
2. résoudre analytiquement lorsque possible ;
3. recalculer indépendamment par une seconde voie ;
4. vérifier les cas limites et les ordres de grandeur ;
5. conserver les valeurs non arrondies pour les contrôles ;
6. expliquer l'arrondi affiché ;
7. ajouter un test automatisé pour les résultats reproductibles.

Pour les simulations : documenter la graine, le nombre de réplications, la méthode et l'erreur Monte-Carlo attendue. Une simulation illustre un résultat ; elle ne remplace pas une preuve lorsqu'une preuve est requise.

## 5. Parité entre Excel, VBA, Python et R

Comparer uniquement lorsque l'atelier apporte une vraie valeur :
- mêmes lignes et mêmes filtres ;
- mêmes règles de valeurs manquantes ;
- mêmes unités et transformations ;
- mêmes conventions (variance d'échantillon/population, quantiles, degrés de liberté, etc.) ;
- mêmes paramètres et tolérances numériques ;
- sorties et écarts expliqués.

Ne pas exiger une égalité bit à bit entre logiciels lorsque les algorithmes ou précisions diffèrent. Définir une tolérance justifiée.

## 6. Contrôle bilingue FR/EN

Le contrôle bilingue vérifie :
- même sens mathématique et mêmes hypothèses ;
- mêmes données, résultats, unités et arrondis ;
- terminologie statistique correcte dans chaque langue ;
- formules, axes, légendes, exemples et corrections cohérents ;
- adaptation naturelle, sans traduction mécanique qui altère le sens.

La version anglaise ne doit pas être considérée comme validée par simple copie de la version française.

## 7. Revue par étapes

- **Design** : objectifs, plan, dépendances et sources identifiés.
- **Draft** : leçon rédigée, statut non publiable.
- **Scientific review** : définitions, démonstrations, hypothèses, exemples et sources vérifiés.
- **Pedagogical review** : intuition, progression, feedback, exercices et transfert évalués.
- **Technical review** : liens, code, calculs, accessibilité, responsive et interactions testés.
- **Bilingual review** : versions FR/EN comparées.
- **Approved** : approbation explicite par la personne habilitée.
- **Published** : publication effective vérifiée.

Un statut ne doit jamais être inféré d'un autre. Une vidéo rendue ne prouve ni la qualité scientifique ni l'approbation.

## 8. Revue des ateliers logiciels

Les fichiers de travail doivent inclure :
- consignes et données ;
- version de logiciel ou environnement ;
- étapes attendues ;
- résultats de référence ;
- solution commentée ;
- erreurs communes ;
- contrôles et limites ;
- licence des données et dépendances.

Un code qui s'exécute une fois n'est pas nécessairement robuste : tester les entrées vides, types inattendus, valeurs manquantes et erreurs usuelles lorsque pertinent.

## 9. Publication et correction

Toute erreur scientifique identifiée après publication doit être consignée avec :
- page et version concernées ;
- gravité et impact sur l'apprenant ;
- correction ;
- recalcul et revue ;
- date de correction et changelog.

Ne jamais corriger silencieusement un résultat qui change le sens d'une leçon ou d'un exercice.

## 10. Statut

Ce protocole définit une cible de qualité. Il n'atteste pas que les leçons existantes ont toutes subi ces revues. Les statuts réels doivent rester ceux des sources et des contrôles effectivement exécutés.
