# F01 — Étude universitaire : nombres, ensembles et précision

## Compétences visées
Démontrer une propriété élémentaire, utiliser les ensembles comme langage de contraintes, raisonner sur l'ordre et distinguer exactitude mathématique et approximation informatique.

## 1. Démonstration : un rationnel a une écriture décimale finie sous une condition précise

Soit \(p/q\) irréductible, avec \(q>0\). Son écriture décimale est finie si et seulement si il existe un entier \(n\geq0\) tel que \(q\mid10^n\). Or \(10^n=2^n5^n\). Les seuls facteurs premiers possibles de \(q\) sont donc 2 et 5.

Réciproquement, si \(q=2^a5^b\), prenons \(n=\max(a,b)\). Alors \(q\mid10^n\), donc \(p/q=m/10^n\) pour un entier \(m\), ce qui donne une écriture décimale finie.

**Conséquence :** 7/80 est fini puisque 80=2^4·5 ; 7/60 ne l'est pas puisque 60=2^2·3·5.

## 2. Valeur absolue comme distance

Pour \(a,b\in\mathbb R\), \(d(a,b)=|a-b|\). L'inégalité triangulaire donne \(|a-c|\leq|a-b|+|b-c|\) : le trajet direct entre deux points sur la droite ne dépasse pas un trajet passant par un point intermédiaire.

Une condition \(|x-a|\leq r\), avec \(r\geq0\), décrit la boule fermée centrée en a et de rayon r, soit \([a-r,a+r]\). En dimension supérieure, la notion de distance dépend du choix de norme ; la distance euclidienne n'est pas la seule possible.

## 3. Exactitude, arrondi et stabilité

L'erreur absolue est \(|\hat x-x|\). L'erreur relative, lorsque \(x\ne0\), est \(|\hat x-x|/|x|\). La première est pertinente pour une tolérance fixe en unité ; la seconde mesure l'erreur à l'échelle de la valeur.

Un algorithme peut être exact pour les données représentées mais produire une réponse éloignée de la réponse au problème initial si les données sont elles-mêmes approximatives. Il faut donc séparer erreur de mesure, erreur de représentation, erreur d'arrondi et erreur de modèle.

## 4. Exemple travaillé : arrondis et cumul

Trois remboursements théoriques valent chacun 0,335 €. Si chaque montant est arrondi au centime selon la règle commerciale « demi vers le haut », chaque remboursement devient 0,34 €, soit 1,02 € au total. Si on additionne d'abord les montants exacts, on obtient 1,005 €, puis l'arrondi au centime donne 1,01 €. La règle d'arrondi et son moment d'application font partie de la spécification métier. En pratique, vérifier aussi la règle légale et le type numérique utilisés.

## 5. Problèmes progressifs

**P1 — Preuve.** Montrer que tout entier pair au carré est divisible par 4.

**P2 — Ensembles.** Un score admissible satisfait simultanément \(x\in[0,100]\), \(x>35\) et \(|x-60|\leq15\). Donner l'ensemble admissible et expliquer chaque intersection.

**P3 — Approximation.** Une mesure vraie est inconnue, mais appartient à [49,5 ; 50,5]. On affiche 50. Calculer la borne de l'erreur absolue et discuter si une erreur relative est définie avec certitude.

## 6. Corrigés

**P1.** Si n est pair, il existe k entier tel que n=2k. Alors n²=4k², donc 4 divise n².

**P2.** \([0,100]\cap(35,+\infty)\cap[45,75]=[45,75]\). La dernière contrainte est un intervalle centré en 60 de rayon 15.

**P3.** Puisque x appartient à [49,5 ; 50,5], \(|50-x|\leq0,5\). La valeur vraie est strictement positive, donc l'erreur relative est définie, mais sa valeur exacte est inconnue ; elle est au plus 0,5/49,5, soit environ 1,01 %.

## 7. Question de défense orale
Pourquoi l'affichage de 12 décimales ne prouve-t-il pas qu'une mesure est exacte à 12 décimales ? Distinguer format, précision de mesure et exactitude.
