# ACTU-BASICS LAB

**Un laboratoire indépendant pour perfectionner ACTU-BASICS.**

Le dépôt source `JohnGAB7/Actu-Basics` reste la référence pédagogique et éditoriale. Ce laboratoire développe une expérience web plus aboutie, sans modifier le dépôt source ni sa publication.

## Direction de conception

- Direction visuelle : ivoire, turquoise profond et or doux.
- Titres serif, interface sans-serif, mise en page responsive.
- Signature FR : « Éveiller par les chiffres. » ; EN : « Enlightening through numbers. »
- Éditions FR/EN, thèmes clair/sombre, recherche et filtres.
- Méthode pédagogique : question → intuition → formalisation → pratique.

## Produit actuel

Treize leçons disposent de pages web bilingues :
- **Fondations mathématiques** : M0.01 à M0.03 — fractions, pourcentages, ordres de grandeur et lecture de graphiques.
- **Statistiques** : S1.01 à S1.07 — données, population, unités, variables, sources, biais de sélection, randomisation et interprétation.
- **Pilotes actuariels** : A0.01 — introduction et prime pure ; A1.01 — intérêts composés et actualisation ; A2.01 — mutualisation des risques.

Les pages A1.01, A2.01 et M0.01 intègrent des calculateurs ou simulateurs interactifs. Les pages M0.02, M0.03 et S1.04 à S1.07 présentent les séquences et narrations des scripts source, avec révélation interactive des corrections.

### Ressources pédagogiques désormais visibles

- **Parcours des fondations** : la page `parcours/` distingue les trois leçons M0 publiées des unités M1 (algèbre et fonctions) et M2 (analyse) encore au programme. Les liens et statuts ne présentent pas les unités futures comme des cours déjà disponibles.
- **Carte interactive des connaissances** : `connaissances/` et `en/knowledge-map/` exposent un prototype de 26 nœuds et 32 relations. La carte filtre les relations, permet d'explorer les dépendances et renvoie vers les leçons disponibles dans le catalogue. Le graphe conserve le statut `design` et ne constitue pas encore un parcours approuvé ni un moteur de progression apprenant.
- **Ateliers logiciels** : `ateliers/` et `en/workshops/` proposent un premier atelier bilingue avec un jeu de données d'assurance entièrement synthétique. Il comprend des exercices et des exemples exécutables pour Excel, Excel VBA, Python et R, ainsi qu'un CSV téléchargeable. Il s'agit d'un atelier pilote, pas encore d'une série complète de formations par outil.
- Les deux ressources sont accessibles depuis la page d'accueil et les pages de parcours, en FR et EN.

## Catalogue pédagogique et statuts

`data/catalogue.json` est extrait des sept fichiers de catalogue du programme de référence. Il contient **320 unités** avec titres, questions, modules, niveaux, durées indicatives, prérequis et références de provenance.

Au dernier état validé :
- **10 unités du catalogue** disposent d'une page web bilingue (M0.01–M0.03 et S1.01–S1.07) ;
- **20 unités** disposent d'un script source référencé, mais pas encore d'une page web dans le laboratoire ;
- **290 unités** restent au programme sans script ou page intégrés ;
- **30 scripts sources** sont référencés dans le catalogue.
- Trois pilotes actuariels supplémentaires (A0.01, A1.01 et A2.01) sont publiés hors de ces 320 unités.

Les statuts sont distincts : page disponible, script source disponible, ou unité au programme. Un script, une fiche de conception, une vidéo rendue et une leçon web sont quatre artefacts différents et ne doivent pas être confondus.

## Rapport au dépôt source

Ce laboratoire doit être un perfectionnement, pas un fork aveugle ni une réécriture déconnectée. Les contenus sont repris depuis les sources du dépôt de référence en conservant :
- titres, objectifs, prérequis et niveaux ;
- définitions, raisonnements, formules et hypothèses ;
- sources, dates, unités, périmètres et incertitudes ;
- exemples, exercices, corrections et limites ;
- états de validation éditoriale.

Les leçons A1.01 et A2.01 sont adaptées des scripts FR/EN validés par le propriétaire du projet. Les pages M0.01–M0.03 et S1.01–S1.07 sont adaptées de scripts marqués validés par JG le 8 novembre 2026. Les autres scripts ne sont pas automatiquement publiés : leur statut de validation est respecté.

## Qualité

Deux workflows GitHub Actions contrôlent le produit :

- `.github/workflows/quality.yml` : structure HTML, titres, langue, viewport, identifiants, attributs `alt`, liens et fragments locaux, catalogue JSON, existence des routes publiées, recalculs mathématiques et intégrité du graphe de connaissances.
- `.github/workflows/browser.yml` : tests Playwright sous Chromium pour la navigation, le catalogue et ses filtres, les calculateurs A1.01/M0.01, le simulateur binomial A2.01, les exercices S1.01/S1.05, la carte de connaissances, les parcours M0–M2, les quatre ateliers logiciels, les routes anglaises et l'affichage mobile.

Ces contrôles automatisés ne remplacent pas une revue visuelle multi-navigateurs, une validation manuelle approfondie au clavier ou une validation scientifique humaine.

## Publication et gouvernance

- Laboratoire : https://github.com/JohnGAB7/Actu-Basics-Lab
- Dépôt de référence : https://github.com/JohnGAB7/Actu-Basics
- Site GitHub Pages : https://johngab7.github.io/Actu-Basics-Lab/
- PR #1 fusionnée dans `master` (squash merge).
- Les ajouts ultérieurs sont effectués directement dans le dépôt laboratoire et déployés par `.github/workflows/pages.yml`.
- Le dernier commit doit toujours être vérifié dans les Actions avant de considérer la dernière version comme publiée.
- Le dépôt source n'a pas été modifié par le laboratoire.
- Les logos officiels et une revue visuelle fondée sur le lien de prévisualisation Blink restent à intégrer ; aucun logo n'est recréé artificiellement.
