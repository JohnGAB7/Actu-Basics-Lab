# Exercices corrigés — AL01 Vecteurs et géométrie

Les exercices sont progressifs. Pour chacun, les coordonnées et les dimensions doivent être explicites ; une réponse sans raisonnement ne suffit pas.

## Exercice 1 — Déplacement

Soient \(A=(2,-3)\) et \(B=(-1,5)\). Calculer \(\overrightarrow{AB}\) et sa norme.

**Corrigé.** \(\overrightarrow{AB}=B-A=(-3,8)\). Sa norme vaut \(\sqrt{(-3)^2+8^2}=\sqrt{73}\).

## Exercice 2 — Opérations

Soient \(u=(1,-2,3)\), \(v=(4,0,-1)\). Calculer \(2u-3v\).

**Corrigé.** \(2u=(2,-4,6)\), \(3v=(12,0,-3)\). Donc \(2u-3v=(-10,-4,9)\).

## Exercice 3 — Norme et distance

Calculer la distance entre \(x=(1,2,2)\) et \(y=(4,6,2)\).

**Corrigé.** \(x-y=(-3,-4,0)\), donc \(d(x,y)=\sqrt{9+16}=5\).

## Exercice 4 — Produit scalaire et orthogonalité

Déterminer si \(u=(2,1,-1)\) et \(v=(1,-1,1)\) sont orthogonaux.

**Corrigé.** \(\langle u,v\rangle=2-1-1=0\). Ils sont orthogonaux.

## Exercice 5 — Angle

Calculer le cosinus de l'angle entre \(u=(1,0)\) et \(v=(1,\sqrt3)\).

**Corrigé.** \(\langle u,v\rangle=1\), \(\|u\|=1\), \(\|v\|=2\). Donc \(\cos\theta=1/2\), soit \(\theta=\pi/3\).

## Exercice 6 — Cauchy-Schwarz

Vérifier Cauchy-Schwarz pour \(u=(1,2)\), \(v=(2,-1)\).

**Corrigé.** \(|\langle u,v\rangle|=|2-2|=0\leq\sqrt5\sqrt5=5\). Il y a égalité seulement lorsque l'un des vecteurs est nul ou lorsqu'ils sont dépendants ; ici ils sont non nuls et orthogonaux, donc inégalité stricte.

## Exercice 7 — Dépendance linéaire

Les vecteurs \(u=(1,2)\) et \(v=(3,6)\) sont-ils indépendants ?

**Corrigé.** Non, car \(v=3u\). Ils sont linéairement dépendants et engendrent une droite vectorielle.

## Exercice 8 — Combinaison linéaire

Peut-on écrire \(w=(5,1)\) comme combinaison linéaire de \(u=(1,1)\) et \(v=(2,-1)\) ? Déterminer les coefficients.

**Corrigé.** Chercher \(a,b\) tels que \(au+bv=w\), soit \(a+2b=5\), \(a-b=1\). On obtient \(b=4/3\), \(a=7/3\). Donc \(w=(7/3)u+(4/3)v\).

## Exercice 9 — Droite paramétrique

Écrire la droite passant par \(A=(1,-2)\) de direction \(v=(3,4)\).

**Corrigé.** \((x,y)=(1,-2)+t(3,4)\), donc \(x=1+3t\), \(y=-2+4t\).

## Exercice 10 — Forme cartésienne

Convertir la droite de l'exercice 9 en équation cartésienne.

**Corrigé.** Un vecteur normal est \(n=(4,-3)\), car \(4(3)-3(4)=0\). L'équation est \(4(x-1)-3(y+2)=0\), soit \(4x-3y-10=0\).

## Exercice 11 — Plan dans l'espace

Déterminer une équation du plan passant par \(A=(1,0,2)\) de normale \(n=(2,-1,3)\).

**Corrigé.** \(2(x-1)-y+3(z-2)=0\), donc \(2x-y+3z-8=0\).

## Exercice 12 — Distance à un point

Calculer la distance entre \(x=(2,-1,4)\) et l'origine dans \(\mathbb R^3\).

**Corrigé.** \(\|x\|=\sqrt{4+1+16}=\sqrt{21}\).

## Exercice 13 — Inégalité triangulaire

Pour \(u=(1,2)\) et \(v=(3,-1)\), vérifier numériquement \(\|u+v\|\leq\|u\|+\|v\|\).

**Corrigé.** \(u+v=(4,1)\), norme \(\sqrt{17}\). À droite, \(\sqrt5+\sqrt{10}\approx5,398\), tandis que \(\sqrt{17}\approx4,123\). L'inégalité est vérifiée.

## Exercice 14 — Mise à l'échelle

Soit \(u=(2,-3,6)\). Calculer \(\|-2u\|\) et vérifier l'homogénéité.

**Corrigé.** \(\|u\|=\sqrt{4+9+36}=7\). Donc \(\|-2u\|=\sqrt{16+36+144}=14=|-2|\times7\).

## Exercice 15 — Interprétation des distances

Deux observations sont \(x=(20,1)\) et \(y=(30,0)\), les coordonnées représentant respectivement un âge en années et un indicateur binaire. Pourquoi la distance euclidienne brute doit-elle être interprétée avec prudence ?

**Corrigé.** Les deux coordonnées n'ont ni la même unité ni la même nature. La différence d'âge domine numériquement le changement de variable binaire. Il faut définir une métrique adaptée au problème, éventuellement standardiser la variable continue et traiter la variable binaire selon une distance appropriée. Une transformation ne doit pas être appliquée automatiquement : elle dépend de la signification et du but de la comparaison.

## Exercice 16 — Synthèse

Soient \(u=(1,1,0)\), \(v=(1,-1,0)\), \(w=(0,0,2)\). Montrer que les trois vecteurs sont deux à deux orthogonaux et calculer leurs normes.

**Corrigé.** \(\langle u,v\rangle=1-1=0\), \(\langle u,w\rangle=0\), \(\langle v,w\rangle=0\). Normes : \(\|u\|=\sqrt2\), \(\|v\|=\sqrt2\), \(\|w\|=2\). Les trois vecteurs forment trois directions orthogonales de l'espace.

## Auto-évaluation

- 0–8 exercices correctement résolus : reprendre les opérations, normes et produits scalaires.
- 9–12 : consolider les équations de droites et plans, ainsi que les justifications.
- 13–15 : niveau satisfaisant ; reprendre les erreurs d'interprétation.
- 16 : expliquer oralement les preuves et les limites des métriques.

Ces repères sont indicatifs et ne remplacent pas une évaluation complète.
