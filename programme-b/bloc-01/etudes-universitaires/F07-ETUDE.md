# F07 — Étude universitaire : fonctions et transformations

## Compétences visées
Analyser domaine, image, injectivité, surjectivité, composition et réciproque ; interpréter une fonction comme modèle.

## 1. Image et antécédents

Pour f:D→E, l'image est \(f(D)=\{f(x):x\in D\}\), sous-ensemble du codomaine E. Un antécédent de y est une valeur x telle que f(x)=y. Un élément du codomaine peut ne pas avoir d'antécédent.

## 2. Injectivité et réciproque

Une fonction est injective si chaque valeur de son image provient d'au plus un x. Si elle est bijective de D vers E, elle possède une réciproque \(f^{-1}:E\to D\). Une fonction non injective peut parfois le devenir après restriction de son domaine.

Exemple : f(x)=x² n'est pas injective sur R, mais elle est bijective de [0,+∞[ vers [0,+∞[ ; sa réciproque est la racine carrée.

## 3. Composition et ordre des opérations

Si une grandeur x est transformée par f puis g, le résultat est g(f(x)). La composition n'est généralement pas commutative. Les domaines doivent être compatibles : l'image de f doit se situer dans le domaine de g.

## 4. Exemple travaillé : tarif après conversion

Une distance m en miles est convertie en kilomètres par k(m)=1,609m. Un tarif vaut c(d)=4+0,35d. La composition est c(k(m))=4+0,56315m. La pente exprime un coût par mile ; l'ordonnée à l'origine est un forfait fixe. Cette fonction est affine, non proportionnelle si le forfait vaut 4.

## 5. Problèmes progressifs

**P1.** Donner domaine et image de f(x)=√(x−3).

**P2.** Étudier l'injectivité de f(x)=3x−5 sur R et déterminer sa réciproque.

**P3.** Une quantité est d'abord multipliée par 1,2 puis on ajoute 7. Écrire la fonction composée et la comparer à l'ordre inverse.

## 6. Corrigés

**P1.** Domaine [3,+∞[ ; image [0,+∞[.

**P2.** Injective car 3x1−5=3x2−5 implique x1=x2. En posant y=3x−5, on obtient x=(y+5)/3 ; donc f⁻¹(y)=(y+5)/3.

**P3.** Première opération puis seconde : g(f(x))=1,2x+7. Ordre inverse : 1,2(x+7)=1,2x+8,4. Les résultats diffèrent de 1,4.

## 7. Question de défense orale
Pourquoi une corrélation élevée entre deux variables ne suffit-elle pas à démontrer que l'une est une fonction déterministe de l'autre ?
