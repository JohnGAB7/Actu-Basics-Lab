# ACTU-BASICS LAB

Une version indépendante et expérimentale d'ACTU-BASICS, développée en parallèle du site de référence.

## Vision

Faire des statistiques, des probabilités et de l'actuariat des disciplines compréhensibles, rigoureuses et vivantes. L'expérience relie trois gestes : découvrir une notion, approfondir la méthode, puis pratiquer.

## Principes de conception

- Identité visuelle ivoire, vert profond / turquoise et or doux.
- Typographies éditoriales Newsreader, Manrope et DM Sans.
- Parcours bilingue français / anglais.
- Interface responsive, navigation clavier, contraste soigné et prise en charge de la réduction des animations.
- Bibliothèque avec recherche et filtres.
- Aucune donnée personnelle ni compte utilisateur requis pour cette première version.

## État

La première expérience web est disponible dans `index.html`. Elle constitue une base de travail visuelle et fonctionnelle, pas encore la migration intégrale de toutes les leçons de la version de référence.

### Prochaines étapes

1. Importer les pages de cours complètes et leurs ressources depuis la version validée.
2. Relier chaque carte de la bibliothèque à sa leçon FR/EN réelle.
3. Auditer les graphiques, les formules, les unités, les sources et les exercices.
4. Ajouter les parcours guidés, la progression locale et les exercices interactifs utiles.
5. Renforcer les tests de liens, d'accessibilité, de responsive et de publication.

## Publication

Le workflow GitHub Pages est défini dans `.github/workflows/pages.yml`. Il publie le contenu du dépôt à chaque mise à jour de `master`, sous réserve que GitHub Pages soit autorisé à utiliser GitHub Actions dans les paramètres du dépôt.

Dépôt indépendant : https://github.com/JohnGAB7/Actu-Basics-Lab
