# ACTU-BASICS LAB

**Un laboratoire indépendant pour perfectionner ACTU-BASICS.**

Le dépôt source `JohnGAB7/Actu-Basics` reste la référence pédagogique et éditoriale. Ce laboratoire développe une expérience web plus aboutie, sans modifier le dépôt source ni sa publication.

## Direction de conception

- Direction visuelle : ivoire, turquoise profond et or doux.
- Typographie : titres serif et interface sans-serif lisible.
- Signature FR : « Éveiller par les chiffres. » ; EN : « Enlightening through numbers. »
- Expérience : navigation responsive, éditions FR/EN, thèmes clair/sombre, recherche et filtres.
- Méthode : question → intuition → formalisation → pratique.

## Parcours et pages web intégrées

- Statistiques, probabilités et économétrie : catalogue issu du programme de référence (320 unités).
- Mathématiques financières : A1.01, intérêts composés et actualisation.
- Sciences actuarielles : A0.01, introduction et prime pure ; A2.01, mutualisation des risques.
- Les trois leçons actuarielles A0.01, A1.01 et A2.01 disposent de pages FR/EN dans le laboratoire.
- Les pages A1.01 et A2.01 intègrent des calculateurs interactifs.

## Catalogue pédagogique et statuts

`data/catalogue.json` est extrait des sept fichiers de catalogue du programme de référence. Il contient 320 unités avec titres, questions, modules, niveaux, durées indicatives, prérequis et références de provenance.

Les statuts sont volontairement distincts :
- **Leçon disponible** : une page web complète existe dans le laboratoire.
- **Script source disponible** : un script existe dans le dépôt de référence, mais n'est pas automatiquement une page web publiée ici.
- **Au programme** : l'unité figure dans le syllabus, mais sa page et son script ne sont pas encore intégrés.

Le catalogue recense actuellement 30 scripts sources pour les unités du programme. Les trois pilotes du parcours actuariat sont référencés séparément. Un script, une fiche de conception, une vidéo rendue et une leçon web sont quatre artefacts différents : ils ne doivent pas être confondus.

## Rapport au dépôt source

Ce laboratoire doit être un perfectionnement, pas un fork aveugle ni une réécriture déconnectée. Les contenus sont repris depuis les sources du dépôt de référence en conservant :
- titres, objectifs, prérequis et niveaux ;
- définitions, raisonnements, formules et hypothèses ;
- sources, dates, unités, périmètres et incertitudes ;
- exemples, exercices, corrections et limites ;
- états de validation éditoriale.

Les leçons A1.01 et A2.01 sont adaptées des scripts FR/EN validés par le propriétaire du projet dans le dépôt source. Les montants sont présentés en euros dans les deux éditions du laboratoire pour garder une lecture homogène. Les hypothèses simplificatrices des modèles sont explicites.

## Qualité

Le workflow `.github/workflows/quality.yml` s'exécute sur les pull requests. Le script `scripts/validate_site.py` contrôle :
- structure HTML minimale, langue, titre et viewport ;
- identifiants HTML uniques et attributs `alt` ;
- chemins et fragments des liens locaux ;
- structure et unicité des 320 unités du catalogue ;
- présence des pages bilingues A0.01, A1.01 et A2.01 ;
- recalculs des principaux exemples actuariels et financiers, dont les probabilités binomiales du pilote A2.01.

Ces contrôles automatisés ne remplacent pas une revue visuelle, un test réel au clavier ou une validation scientifique humaine.

## Publication et gouvernance

- Le dépôt source n'est pas modifié par ce laboratoire.
- La branche de travail est `chatgpt/premium-editorial-v1`.
- La PR #1 est maintenue ouverte jusqu'à réussite des contrôles et vérifications visuelles.
- Aucune fusion vers le dépôt source n'est prévue.
- Aucun déploiement public n'est annoncé tant que le workflow Pages n'a pas publié cette version avec succès.
- GitHub Pages doit utiliser **GitHub Actions** comme source dans les paramètres du dépôt.

## Dépôts

- Laboratoire : https://github.com/JohnGAB7/Actu-Basics-Lab
- Référence : https://github.com/JohnGAB7/Actu-Basics
