# F05 — Étude universitaire : algèbre, factorisation et domaines

## Compétences visées
Distinguer identité et équation, transformer une expression en préservant son domaine, factoriser pour révéler une structure et contrôler les unités.

## 1. Identité et équation

Une identité est vraie pour toutes les valeurs admissibles des variables. Une équation demande les valeurs qui rendent une égalité vraie. Ainsi \((x+1)^2=x^2+2x+1\) est une identité ; \((x+1)^2=9\) est une équation.

## 2. Simplification rationnelle et domaine

Considérons \(f(x)=(x^2-1)/(x-1)\). Le domaine initial est \(\mathbb R\setminus\{1\}\). Pour x différent de 1, factoriser donne \((x-1)(x+1)/(x-1)=x+1\). La fonction est donc égale à x+1 sur son domaine, mais elle n'est toujours pas définie en 1.

La simplification algébrique ne répare pas rétroactivement une division par zéro.

## 3. Identités remarquables et preuve

\((a+b)^2=a^2+2ab+b^2\) découle de la distributivité : \((a+b)(a+b)=a^2+ab+ba+b^2\). Cette démonstration explique l'apparition du terme double 2ab, souvent oublié.

## 4. Exemple travaillé : seuil de rentabilité

Un résultat est \(R(q)=-q^2+10q-16\). Factoriser : \(R(q)=-(q-2)(q-8)\). Les zéros sont 2 et 8. Comme la parabole est tournée vers le bas, R(q)>0 pour 2<q<8. Il faut encore vérifier si q peut être continu, entier, borné ou soumis à d'autres contraintes opérationnelles.

## 5. Problèmes progressifs

**P1.** Développer \((2x-3)^2\), puis vérifier le résultat pour x=2.

**P2.** Simplifier \((x^2-9)/(x^2-3x)\), en précisant les exclusions du domaine initial.

**P3.** Factoriser \(P(x)=x^2-7x+12\) et déterminer son signe.

## 6. Corrigés

**P1.** \(4x^2-12x+9\). Pour x=2, le carré vaut 1 ; l'expression développée vaut 16−24+9=1.

**P2.** Domaine initial : x différent de 0 et 3. Pour ces valeurs, expression simplifiée \((x+3)/x\). La valeur 3 reste exclue.

**P3.** \((x-3)(x-4)\). Le produit est positif pour x<3 ou x>4, nul en 3 et 4, négatif entre les deux racines.

## 7. Question de défense orale
Pourquoi deux expressions algébriquement égales sur un domaine peuvent-elles définir des fonctions différentes si leurs domaines ne sont pas identiques ?
