# Atelier Excel — Bloc 1

Les noms de fonctions et séparateurs varient selon la langue et la version d'Excel. Les exemples ci-dessous utilisent les noms français usuels et le séparateur `;`.

## F01 — Bases et précision
- Conversion binaire vers décimal : `=DECIMAL("11010";2)` (disponibilité selon version).
- Conversion décimal vers binaire : `=BASE(26;2)`.
- Ne pas confondre format d'affichage et précision stockée : afficher deux décimales ne signifie pas que la valeur sous-jacente a été arrondie.

## F02 — Fractions et ratios
- Part d'un total : `=Numerateur/Denominateur`.
- Partage pondéré : `=Total*Poids/SOMME(PlagePoids)`.
- Ajouter un contrôle : si la somme des poids est nulle, afficher un message plutôt que diviser.

## F03 — Variations
- Variation relative : `=ValeurFinale/ValeurInitiale-1`.
- Variation en points : `=TauxFinal-TauxInitial`, puis formater en points de pourcentage ou multiplier par 100 selon l'affichage.
- Variation composée de taux successifs en B2:B5 : `=PRODUIT(1+B2:B5)-1` ; selon la version, utiliser une formule matricielle ou une colonne de coefficients `1+taux`.

## F04/F05/F06 — calculs
- Puissance : `=PUISSANCE(A1;B1)`.
- Racine carrée : `=RACINE(A1)` pour A1≥0.
- Logarithme népérien : `=LN(A1)` pour A1>0.
- Équation linéaire ax+b=0 : `=-b/a`, si a≠0.
- Pour une résolution plus générale, utiliser Valeur cible ou Solveur et documenter la fonction objectif et les contraintes.

## F07/F08 — tableaux et graphiques
- Calculer les sorties d'une fonction dans une colonne, puis insérer un nuage de points XY.
- Pour une série temporelle, utiliser une échelle chronologique correcte et afficher l'unité.
- Pour comparer des groupes de tailles différentes, représenter un taux avec son dénominateur plutôt que le seul effectif brut.

## Contrôles de qualité
1. Éviter les références de cellules ambiguës ; nommer les plages importantes.
2. Verrouiller les références qui doivent rester fixes lors de la recopie.
3. Afficher les erreurs de domaine explicitement.
4. Vérifier un échantillon à la main.
5. Documenter les unités et le sens des taux.
