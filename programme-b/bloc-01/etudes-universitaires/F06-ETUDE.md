# F06 — Étude universitaire : équations, inéquations et systèmes

## Compétences visées
Justifier les transformations, résoudre un système, contrôler les solutions parasites et interpréter une contrainte.

## 1. Équivalence et implication

Si une transformation est réversible sur le domaine considéré, elle conserve l'ensemble des solutions. Ajouter une même quantité aux deux membres est réversible. Élever au carré ne l'est pas sur tout \(\mathbb R\) : de x=−2 et y=2, les carrés sont égaux alors que x et y ne le sont pas.

Il faut donc annoncer le domaine et vérifier dans l'équation initiale toute solution obtenue après une transformation non équivalente.

## 2. Systèmes linéaires : lecture matricielle

Un système \(Ax=b\) possède une solution unique lorsque la matrice carrée A est inversible, c'est-à-dire lorsque son déterminant est non nul. Pour des systèmes rectangulaires ou singuliers, l'existence et l'unicité dépendent du rang de A et du rang de la matrice augmentée.

L'élimination de Gauss repose sur des opérations élémentaires sur les lignes qui préservent l'ensemble des solutions.

## 3. Exemple travaillé : deux tarifs inconnus

On observe \(2a+3b=180\) et \(4a+b=160\). La deuxième équation donne b=160−4a. En remplaçant : 2a+3(160−4a)=180, donc −10a=−300, a=30 et b=40. Vérification dans les deux équations : 60+120=180 et 120+40=160.

## 4. Problèmes progressifs

**P1.** Résoudre \(3x-7=11\) et justifier chaque opération.

**P2.** Résoudre \(\sqrt{x+2}=x\), en commençant par le domaine et en vérifiant les candidats.

**P3.** Résoudre le système \(x+2y=11\), \(3x-y=5\).

## 5. Corrigés

**P1.** Ajouter 7 : 3x=18 ; diviser par 3 : x=6.

**P2.** Domaine et signe : x≥0. En élevant au carré, x+2=x², soit (x−2)(x+1)=0. Candidats 2 et −1 ; seul 2 satisfait x≥0. Vérification : √4=2.

**P3.** De la première équation x=11−2y. Substitution : 33−7y=5, donc y=4 et x=3. Vérification : 3+8=11 et 9−4=5.

## 6. Question de défense orale
Pourquoi l'élimination de Gauss est-elle plus robuste qu'une résolution « à vue » pour un système de grande taille ? Évoquer traçabilité, complexité et stabilité numérique sans confondre ces notions.
