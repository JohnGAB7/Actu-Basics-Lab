# ACTU-BASICS — recherche et principes de conception pédagogique

**État :** note de conception fondée sur la littérature consultée le 19 novembre 2026.  
**Portée :** recommandations pour la conception future ; ce document ne certifie pas encore l'efficacité de la plateforme auprès de ses apprenants.

## 1. Ce que la recherche soutient

### Récupération active et révisions espacées

La revue de Carpenter, Pan et Butler (2022) synthétise les résultats sur la pratique de récupération et l'espacement. Elle met en avant leur intérêt pour la rétention durable et leur sous-utilisation dans les pratiques d'apprentissage.

**Conséquence produit :**
- chaque notion importante doit être réactivée après sa leçon, pas seulement relue ;
- proposer de courtes questions de rappel sans afficher immédiatement la solution ;
- revoir les notions à plusieurs moments, avec des intervalles qui s'allongent si les réponses restent solides ;
- fournir un feedback explicatif après la tentative.

Source : https://www.nature.com/articles/s44159-022-00089-1

### Pratique distribuée et entrelacée : effets conditionnels

La méta-analyse de Ruitenburg et al. (2026), fondée sur 53 études et 7 303 apprenants en contexte scolaire, rapporte des effets moyens positifs pour la récupération, l'espacement et l'entrelacement. Elle identifie aussi des modérateurs : type de connaissance, format d'évaluation, intervalle, feedback et processus cognitifs réellement sollicités. Les résultats ne justifient donc pas une règle uniforme appliquée à chaque leçon.

**Conséquence produit :**
- pratiquer d'abord un type de problème avec un soutien suffisant lorsque la procédure est nouvelle ;
- entrelacer ensuite des problèmes voisins pour apprendre à reconnaître quelle méthode choisir ;
- faire varier les contextes et les formulations afin de vérifier le transfert ;
- ne pas confondre alternance aléatoire et progression pédagogique.

Source : https://link.springer.com/article/10.1007/s10648-026-10225-5

### Stratégies d'apprentissage en STEM dans l'enseignement supérieur

La revue systématique de 2026 sur les stratégies d'étude fondées sur les preuves en STEM dans l'enseignement supérieur examine 65 études. Elle relève notamment le rôle des tests de pratique, de l'espacement, de l'entrelacement, de l'explication et des exemples concrets, tout en notant des difficultés d'implémentation et des lacunes dans les études disponibles.

**Conséquence produit :**
- utiliser des exemples résolus avant de retirer progressivement les aides ;
- demander à l'apprenant d'expliquer pourquoi une méthode s'applique ;
- relier les formules à des situations concrètes et à des représentations ;
- évaluer l'application dans des problèmes nouveaux, pas seulement la répétition de l'exemple.

Source : https://link.springer.com/article/10.1186/s40594-026-00632-z

### Accessibilité numérique

WCAG 2.2 constitue la référence normative à viser. Pour notre interface, les critères particulièrement pertinents comprennent l'utilisation au clavier, la visibilité du focus, le fait que le focus ne soit pas masqué, le contraste des composants et la possibilité de redimensionner/espacer le texte sans perte de contenu.

**Conséquence produit :**
- liens d'évitement vers le contenu principal ;
- navigation utilisable au clavier et sur mobile ;
- focus visible et jamais caché sous un en-tête fixe ;
- contrastes vérifiés sur les deux thèmes ;
- tailles de cibles et états interactifs vérifiés ;
- tests automatisés complétés par une revue manuelle avec clavier et lecteur d'écran.

Source normative : https://www.w3.org/TR/WCAG22/

## 2. Modèle de leçon recommandé

Une unité n'a pas à contenir mécaniquement neuf sections si le sujet est simple. Elle doit cependant choisir les éléments pédagogiques qui servent son objectif.

1. **Problème et pertinence** — quelle question réelle va-t-on résoudre ?
2. **Activation des prérequis** — une question courte pour réactiver les connaissances utiles.
3. **Intuition** — exemple concret, schéma ou simulation.
4. **Formalisation** — définition, notation, hypothèses, formule ou démonstration.
5. **Exemple résolu** — étapes explicites et justification des choix.
6. **Pratique guidée** — exercice avec indices progressifs.
7. **Pratique autonome** — exercice sans aide immédiate.
8. **Feedback** — correction raisonnée, diagnostic de l'erreur et piste de reprise.
9. **Transfert** — même compétence dans un contexte différent.
10. **Application logicielle** — Excel, VBA, Python ou R lorsque l'outil sert l'objectif.
11. **Limites et synthèse** — hypothèses, pièges, interprétation et prochaine compétence.

## 3. Évaluer la maîtrise plutôt que l'exposition

Le fait d'ouvrir une page, de regarder une vidéo ou de réussir une question isolée ne prouve pas une maîtrise durable.

Pour une compétence importante, distinguer :
- **reconnaissance** : identifier le concept ou le bon outil ;
- **compréhension** : expliquer le sens et les hypothèses ;
- **exécution** : effectuer correctement la procédure ;
- **interprétation** : expliquer le résultat dans le contexte ;
- **diagnostic** : repérer une erreur, une hypothèse violée ou une limite ;
- **transfert** : choisir et appliquer la méthode à un cas nouveau.

Une maîtrise robuste demande plusieurs preuves, dont une tentative différée et au moins une tâche de transfert. Les seuils doivent être définis par compétence, pas inventés globalement.

## 4. Architecture de pratique logicielle

Les quatre outils forment des fils pratiques complémentaires et non quatre versions obligatoires de chaque leçon.

| Outil | Quand il est pertinent | Preuve de compétence |
|---|---|---|
| Excel | exploration rapide, calcul tabulaire, contrôles, restitution métier | classeur vérifiable et documenté |
| Excel VBA | répétition, automatisation, rapports et interactions avec Excel | macro maintenable, contrôlée et expliquée |
| Python | transformation, simulation, automatisation, ML et pipelines | notebook/script reproductible et testé |
| R | analyse statistique, inférence, modélisation et rapports | analyse reproductible avec diagnostics et interprétation |

Chaque atelier doit déclarer : objectif, prérequis, données, environnement/version, étapes, livrable, critères de correction, erreurs courantes et limites. Les comparaisons multi-outils doivent réutiliser un problème comparable afin de distinguer la méthode statistique de son implémentation.

## 5. Architecture de l'évaluation

Pour les exercices et projets, une grille commune peut couvrir :

- justesse conceptuelle ;
- exactitude de calcul ou de code ;
- adéquation de la méthode à la question ;
- respect des hypothèses et qualité des données ;
- interprétation et communication ;
- reproductibilité ;
- capacité à détecter les limites.

Les pondérations varient selon le niveau et le domaine. Un calcul exact ne doit pas compenser une interprétation fausse ou un modèle inadapté.

## 6. Mesures produit à instrumenter plus tard

Lorsque le produit disposera d'un système de progression et d'un consentement approprié, mesurer avec minimisation des données :
- réussite au premier essai et après feedback ;
- rétention différée ;
- transfert vers un exercice inédit ;
- temps et nombre d'indices nécessaires, sans en faire une métrique de classement ;
- erreurs récurrentes par compétence ;
- progression par compétence plutôt que score global unique.

Ne pas collecter de données personnelles inutiles. Ne pas présenter une métrique d'engagement (clics, durée de session, pages vues) comme une preuve d'apprentissage.

## 7. Limites et gouvernance

- Les articles cités étayent des principes généraux, pas l'efficacité déjà mesurée d'ACTU-BASICS.
- Les résultats de méta-analyses dépendent des populations, matières, interventions, comparateurs et modalités d'évaluation.
- Les prérequis stricts du graphe doivent être justifiés ; les prérequis simplement utiles restent recommandés ou facultatifs.
- Les contenus scientifiques doivent être revus indépendamment : exactitude des formules, conventions, unités, sources, exemples, corrections et traductions.
- Aucun contenu « design » ni script en attente de validation ne devient automatiquement une leçon publiée.


## 9. Référentiels disciplinaires : statistique et actuariat

### GAISE College Report — American Statistical Association

Le rapport GAISE College de l'ASA est une ressource vivante révisée par étapes ; sa version actuelle comprend des recommandations pour les cours introductifs de statistique et de data science, ainsi que des orientations d'évaluation.

**Traduction pour ACTU-BASICS :**
- enseigner la statistique comme un processus d'investigation, et non comme une liste de formules ;
- partir de questions et de données contextualisées ;
- faire travailler la variabilité, l'incertitude, l'interprétation et l'argumentation ;
- intégrer la technologie à l'analyse quand elle permet d'explorer ou de raisonner ;
- faire correspondre l'évaluation aux compétences réellement visées.

Ce rapport est un référentiel de conception de cours introductifs ; il ne remplace pas le syllabus disciplinaire du projet.

Sources :
- https://asacollegegaise.org/
- https://amstat.quarto.pub/college-gaise/index.html

### Society of Actuaries — progression de compétences professionnelles

Le parcours ASA de la SOA présente des blocs distincts : fondations (mathématiques financières, probabilités), puis mathématiques actuarielles, statistique pour le risque, analyse prédictive et pratique actuarielle. La SOA précise aussi que l'examen FAM suppose des acquis en probabilité, statistique mathématique et mathématiques financières.

**Traduction pour ACTU-BASICS :**
- garder les mathématiques financières et les probabilités comme fondations parallèles, liées mais distinctes ;
- construire les méthodes actuarielles après les fondations de probabilités/statistique et de finance ;
- ne pas réduire l'actuariat à la seule tarification : intégrer assurance, prestations contingentes, réserves, risques et analyse prédictive ;
- créer une passerelle d'orientation vers les compétences professionnelles, sans prétendre préparer officiellement à une certification ni recopier un syllabus protégé.

Sources :
- https://www.soa.org/education/associate-of-the-society-of-actuaries-asa/
- https://www.soa.org/education/exam-req/edu-exam-fam/
- https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-fam-syllabus.pdf

## 8. Références consultées

1. Carpenter, S. K., Pan, S. C. & Butler, A. C. (2022). *The science of effective learning with spacing and retrieval practice*. Nature Reviews Psychology. https://www.nature.com/articles/s44159-022-00089-1
2. Ruitenburg, S. K. et al. (2026). *A Meta-Analysis of the Effectiveness and Boundary Conditions of Retrieval Practice, Distributed Practice, and Interleaved Practice in Authentic School Classrooms*. Educational Psychology Review. https://link.springer.com/article/10.1007/s10648-026-10225-5
3. *STEMing evidence-based study strategies: a systematic review of literature* (2026). International Journal of STEM Education. https://link.springer.com/article/10.1186/s40594-026-00632-z
4. W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/

5. American Statistical Association. *GAISE College Report* (version évolutive, révision 2025/2026). https://asacollegegaise.org/
6. Society of Actuaries. *ASA Educational Pathway* and *Fundamentals of Actuarial Mathematics (FAM) Exam*. https://www.soa.org/education/associate-of-the-society-of-actuaries-asa/ and https://www.soa.org/education/exam-req/edu-exam-fam/
7. Society of Actuaries. *FAM July 2026 syllabus*. https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-fam-syllabus.pdf
