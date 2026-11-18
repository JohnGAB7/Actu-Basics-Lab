# ACTU-BASICS — Moteur de connaissances et graphe de prérequis

Version 1.0 · Proposition d'architecture · 19 novembre 2026

## 1. Rôle dans le produit

Le graphe de connaissances complète l'architecture globale déjà retenue en cinq paliers. Il ne la remplace pas et ne crée pas un deuxième syllabus.

- Les **cinq paliers** décrivent le chemin global : fondations, socle quantitatif, pratique appliquée, spécialisation, maîtrise.
- Les **parcours statistiques P0–P7** décrivent une progression disciplinaire interne au socle et à ses prolongements.
- Le **catalogue de 320 unités** demeure la source de référence pour les identifiants, titres, statuts, durées et provenances des unités.
- Le **graphe** explicite les relations entre concepts, compétences, outils, évaluations et projets. Il aide à naviguer dans le catalogue sans dupliquer ses contenus.

## 2. Entités du graphe

| Type | Rôle | Exemple |
|---|---|---|
| concept | Idée à comprendre | médiane, variance, indépendance |
| skill | Action observable | calculer, interpréter, diagnostiquer |
| learning_unit | Leçon ou unité du catalogue | identifiant catalogue existant |
| tool_practice | Mise en œuvre dans un outil | calculer une médiane dans R |
| assessment | Preuve d'acquisition | exercice de transfert |
| project | Mobilisation de plusieurs compétences | audit exploratoire d'un portefeuille |

Chaque nœud doit avoir un identifiant stable, un titre, une langue indépendante du titre, un type, un statut éditorial et des références de provenance. Les nœuds concepts ne doivent pas devenir des doublons de pages de cours.

## 3. Types de relations

- `requires` : prérequis strict. L'absence de cette compétence empêche raisonnablement de comprendre ou d'exécuter la tâche.
- `recommends` : prérequis utile mais contournable par une capsule ou un diagnostic.
- `supports` : notion qui aide à comprendre une autre notion sans être une condition obligatoire.
- `applies` : compétence ou concept mobilisé dans un cas, un outil ou un projet.
- `assessed_by` : preuve permettant d'évaluer un résultat d'apprentissage.
- `continues_to` : suite naturelle ou approfondissement, sans prétendre qu'il s'agit d'un prérequis.

Ne jamais utiliser une relation générique « lié à » pour masquer une relation pédagogique inconnue.

## 4. Règles de construction

1. Un prérequis strict doit être justifié par une dépendance cognitive ou mathématique précise.
2. Éviter les chaînes artificiellement longues : si une capsule de cinq minutes suffit, déclarer un prérequis recommandé et proposer cette capsule.
3. Le graphe des relations `requires` doit être acyclique. Tout cycle est une erreur de conception à résoudre.
4. Une unité peut appartenir à plusieurs parcours et spécialités.
5. Les relations doivent être traçables à un objectif d'apprentissage ou à une justification pédagogique.
6. Les identifiants du catalogue ne sont ajoutés qu'après vérification du catalogue source ; ne jamais inventer un identifiant d'unité.
7. Les liens logiciels sont attachés à la compétence concernée, pas imposés systématiquement à chaque concept.
8. Le graphe n'infère jamais qu'un apprenant maîtrise une notion parce qu'il a ouvert ou regardé une page.

## 5. Diagnostic et personnalisation transparente

Le positionnement doit évaluer des compétences, pas demander uniquement à l'apprenant de s'auto-déclarer « débutant » ou « avancé ».

- Une réponse correcte avec raisonnement valide peut permettre de franchir un prérequis.
- Une réponse correcte par hasard ne suffit pas à certifier la maîtrise.
- Une lacune ciblée propose une capsule courte et un nouvel essai.
- L'apprenant peut consulter pourquoi une notion est recommandée ou requise.
- Les exemptions et raccourcis doivent être explicables et réversibles.

Ne pas enfermer l'apprenant dans un niveau global unique : il peut être avancé en visualisation et débutant en probabilités.

## 6. Exemple de lecture

Pour étudier un intervalle de confiance sur une moyenne, le parcours peut nécessiter la compréhension d'un échantillon, de la moyenne, de la variabilité et d'une distribution d'échantillonnage. L'algèbre nécessaire peut être vérifiée par un diagnostic local plutôt qu'imposée comme un long module préalable.

Pour une régression linéaire, l'apprenant réutilise les nuages de points, la covariance, la moyenne, les résidus et l'algèbre. La visualisation et le diagnostic restent des compétences évaluées en plus du calcul du coefficient.

## 7. Contrat de données

Le fichier `data/knowledge-graph/statistics-core-v1.json` est un prototype pédagogique limité. Il ne prétend pas être le graphe complet du catalogue et ne modifie aucun statut de validation des leçons.

Avant tout branchement au site :
- vérifier chaque correspondance avec `data/catalogue.json` ;
- contrôler l'unicité des identifiants et l'intégrité référentielle ;
- détecter les cycles dans `requires` ;
- valider les relations et les traductions FR/EN ;
- ajouter des tests automatisés et une visualisation accessible ;
- ne pas exposer les nœuds « design » comme des leçons publiées.

## 8. Statut

Cette spécification et son petit graphe de démonstration sont des propositions de conception. Ils ne sont ni une migration du catalogue, ni un moteur fonctionnel, ni une validation officielle de nouvelles leçons.
