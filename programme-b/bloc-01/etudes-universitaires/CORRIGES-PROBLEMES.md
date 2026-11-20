# Corrigés détaillés — 24 problèmes des études universitaires

Ce document développe les solutions des trois problèmes de chacun des huit dossiers F01 à F08. Il complète les corrigés synthétiques déjà présents dans les fiches, sans les remplacer.

## Méthode attendue

Pour chaque problème, une solution solide comporte : (1) les données et le domaine, (2) la propriété ou le modèle utilisé, (3) les transformations justifiées, (4) le résultat avec unité ou domaine, (5) une vérification ou une interprétation. Une réponse numérique seule ne démontre pas la maîtrise.

---

## F01 — Nombres, ensembles et précision

### P1 — Carré d'un entier pair

**Énoncé.** Montrer que tout entier pair au carré est divisible par 4.

**Démonstration.** Par définition, un entier pair n s'écrit n=2k pour un entier k. En élevant au carré :
\[
n^2=(2k)^2=4k^2.
\]
Comme k² est un entier, n² est un multiple entier de 4. Donc 4 divise n².

**Point de méthode.** La preuve part de la définition de « pair » et transforme la propriété à démontrer en une factorisation explicite par 4.

### P2 — Intersection de contraintes

**Énoncé.** Déterminer les x tels que x appartient à [0,100], x>35 et |x−60|≤15.

**Étape 1 — Traduire la valeur absolue.**
\[
|x-60|\leq15 \iff 45\leq x\leq75.
\]

**Étape 2 — Intersecter les contraintes.**
\[
[0,100]\cap(35,+\infty)\cap[45,75]=[45,75].
\]

L'intervalle [45,75] satisfait déjà x>35 et [0,100]. Les bornes 45 et 75 sont incluses, car l'inégalité de distance est large.

**Vérification des bornes.** x=45 et x=75 sont admissibles ; x=44 ne l'est pas.

### P3 — Erreur d'approximation

La mesure vraie x appartient à [49,5 ; 50,5] et l'affichage est 50.

L'erreur absolue vaut |50−x|. Sur l'intervalle donné, son maximum est 0,5 :
\[
0\leq|50-x|\leq0,5.
\]
L'erreur relative est |50−x|/|x|. Comme x≥49,5>0, elle est bien définie pour toute valeur possible. On peut la borner :
\[
\frac{|50-x|}{|x|}\leq\frac{0,5}{49,5}\approx0,010101=1,01\%.
\]
La valeur exacte de l'erreur relative reste inconnue, puisque la valeur vraie n'est pas connue.

**Nuance.** La borne supérieure est atteinte à x=49,5. À x=50, l'erreur est nulle.

---

## F02 — Rapports, proportions et exposition

### P1 — Choix du dénominateur

Données : 80 sinistres, 2 000 contrats, 1 500 années-contrats d'exposition.

Par contrat :
\[
\frac{80}{2000}=0,04\text{ sinistre par contrat}.
\]
Par année-contrat :
\[
\frac{80}{1500}=0,053333\ldots\text{ sinistre par année-contrat}.
\]

Le second ratio mesure la fréquence rapportée à l'exposition temporelle. Le premier est un ratio par contrat observé, qui ne tient pas compte de la durée d'exposition de chaque contrat.

**Interprétation.** Il ne faut pas remplacer « année-contrat » par « contrat » dans le libellé : les deux indicateurs n'ont pas le même dénominateur ni la même unité.

### P2 — Coût moyen avec composante fixe

\[
C(q)=25+1,8q.
\]
Pour q=10 :
\[
C(10)=25+18=43,\qquad C(10)/10=4,30.
\]
Pour q=100 :
\[
C(100)=25+180=205,\qquad C(100)/100=2,05.
\]

En général, pour q>0 :
\[
\frac{C(q)}q=\frac{25}{q}+1,8.
\]
Lorsque q augmente sans borne, 25/q tend vers 0 et le coût moyen tend vers 1,8 par unité. Le coût total n'est pas proportionnel à q, car C(0)=25 et non 0.

### P3 — Partage proportionnel

Somme des poids : 2+3+7=12. Pour un total T=18 000 €, les parts sont :
- poids 2 : 18 000×2/12=3 000 € ;
- poids 3 : 18 000×3/12=4 500 € ;
- poids 7 : 18 000×7/12=10 500 €.

Contrôle :
\[
3000+4500+10500=18000\text{ €}.
\]
Un poids nul reçoit une part nulle. La formule reste valide si tous les poids sont non négatifs et si leur somme est strictement positive. Si tous les poids sont nuls, la répartition est indéfinie.

---

## F03 — Variations composées et indices

### P1 — Trois évolutions successives

Les facteurs multiplicatifs sont 1,05, 1,05 et 0,92. Le facteur global vaut :
\[
1,05\times1,05\times0,92=1,0143.
\]
Le taux global est donc 1,0143−1=0,0143, soit **+1,43 %**.

La somme arithmétique des taux (+5 %+5 %−8 %=+2 %) est incorrecte pour calculer l'évolution composée.

### P2 — Rebasage d'un indice

L'indice vaut 96 en t=1 et 120 en t=3. La valeur en t=3 exprimée en base 100 en t=1 est :
\[
100\times\frac{120}{96}=125.
\]
La série a donc progressé de 25 % entre t=1 et t=3. Le rebasage ne change pas le rapport entre les deux niveaux ; il change le point de référence.

### P3 — Points et variation relative

Le taux passe de 4 % à 5 %.

- Écart absolu de taux : 5 %−4 %=**1 point de pourcentage**.
- Variation relative : (5−4)/4=0,25, soit **+25 %**.

Dire « hausse de 1 % » serait ambigu et généralement faux : le taux augmente d'un point, ce qui représente une hausse relative de 25 %.

---

## F04 — Exponentielle et logarithme

### P1 — Équation exponentielle

\[
5^{2x-1}=13.
\]
Comme 5>0 et 5≠1, on peut prendre le logarithme :
\[
(2x-1)\ln5=\ln13.
\]
Donc :
\[
x=\frac12\left(1+\frac{\ln13}{\ln5}\right)\approx1,297.
\]

La transformation est réversible, car le logarithme est défini pour 13>0 et la fonction exponentielle de base 5 est injective.

### P2 — Nombre d'années entières

On cherche le plus petit entier n tel que :
\[
1,025^n\geq1,30.
\]
En prenant les logarithmes :
\[
n\geq\frac{\ln(1,30)}{\ln(1,025)}\approx10,62.
\]
Le plus petit entier qui satisfait l'inégalité est donc **11 ans**.

**Contrôle discret.** Le seuil réel est entre 10 et 11 ; on vérifie donc les valeurs entières voisines. 10 ans ne suffisent pas, 11 ans suffisent. Ne pas arrondir 10,62 à 10 : il s'agit d'un nombre minimal de périodes entières.

### P3 — Taux continu équivalent

Le facteur annuel effectif est 1,045. Le taux continu équivalent δ vérifie e^δ=1,045 :
\[
\delta=\ln(1,045)\approx0,0440169.
\]
Soit environ **4,402 % en taux continu**. Il est inférieur au taux effectif de 4,5 %, car ln(1+r)<r pour r>0.

---

## F05 — Algèbre, factorisation et domaines

### P1 — Développement et contrôle numérique

\[
(2x-3)^2=(2x)^2-2(2x)(3)+3^2
=4x^2-12x+9.
\]
Pour x=2, l'expression initiale vaut (4−3)²=1. L'expression développée donne 4×4−24+9=16−24+9=1.

Le contrôle numérique détecte certaines erreurs, mais ne remplace pas la preuve algébrique générale.

### P2 — Simplification rationnelle

\[
\frac{x^2-9}{x^2-3x}
=\frac{(x-3)(x+3)}{x(x-3)}.
\]
Le dénominateur initial impose x≠0 et x≠3. Pour ces valeurs seulement, on simplifie par x−3 :
\[
\frac{x+3}{x},\qquad x\in\mathbb R\setminus\{0,3\}.
\]

**Point essentiel.** La formule simplifiée est définie en x=3, mais la fonction initiale ne l'est pas. L'exclusion x=3 doit donc être conservée.

### P3 — Factorisation et signe

\[
P(x)=x^2-7x+12=(x-3)(x-4).
\]
Les racines sont 3 et 4. Le coefficient dominant est positif ; le trinôme est positif à l'extérieur des racines et négatif entre elles :
- P(x)>0 si x<3 ou x>4 ;
- P(x)=0 si x=3 ou x=4 ;
- P(x)<0 si 3<x<4.

On peut confirmer le signe en testant un point de chaque intervalle, par exemple 0, 3,5 et 5.

---

## F06 — Équations, inéquations et systèmes

### P1 — Équation du premier degré

\[
3x-7=11.
\]
Ajouter 7 aux deux membres donne 3x=18. Diviser par 3, non nul, donne x=6. Vérification : 3×6−7=11. Chaque opération est réversible ; la solution est unique.

### P2 — Équation avec racine

\[
\sqrt{x+2}=x.
\]
La racine impose x+2≥0, mais l'égalité impose aussi x≥0 puisque le membre de gauche est non négatif. On travaille donc sur [0,+∞[.

En élevant au carré :
\[
x+2=x^2\iff x^2-x-2=0\iff(x-2)(x+1)=0.
\]
Les candidats sont 2 et −1. Le candidat −1 est hors du domaine x≥0. Vérification de x=2 :
\[
\sqrt{2+2}=2.
\]
La solution est **x=2**. Le contrôle dans l'équation initiale est indispensable après élévation au carré.

### P3 — Système linéaire

\[
\begin{cases}
x+2y=11,\\
3x-y=5.
\end{cases}
\]
De la première équation, x=11−2y. Substitution dans la seconde :
\[
3(11-2y)-y=5
\iff33-7y=5
\iff y=4.
\]
Donc x=11−8=3.

Vérification : 3+2×4=11 et 3×3−4=5. La solution unique est (x,y)=(3,4). Le déterminant de la matrice [[1,2],[3,−1]] vaut −1−6=−7, non nul, ce qui confirme l'unicité.

---

## F07 — Fonctions et transformations

### P1 — Domaine et image d'une racine

\[
f(x)=\sqrt{x-3}.
\]
Pour que la racine carrée réelle existe, il faut x−3≥0, donc le domaine est [3,+∞[. La racine carrée prend des valeurs positives ou nulles. Toute valeur y≥0 est atteinte en choisissant x=y²+3. L'image est donc [0,+∞[.

Cette dernière justification prouve à la fois que l'image est incluse dans [0,+∞[ et qu'elle contient toutes les valeurs de cet intervalle.

### P2 — Injectivité et réciproque

f(x)=3x−5 sur R. Supposons f(x₁)=f(x₂) :
\[
3x_1-5=3x_2-5\implies3x_1=3x_2\implies x_1=x_2.
\]
La fonction est injective. Pour déterminer la réciproque, poser y=3x−5 et isoler x :
\[
x=\frac{y+5}{3}.
\]
Ainsi f⁻¹(y)=(y+5)/3. Comme la fonction affine de pente non nulle prend toutes les valeurs réelles, elle est aussi surjective de R vers R et donc bijective.

### P3 — Ordre des transformations

Multiplier par 1,2 puis ajouter 7 donne :
\[
g(f(x))=1,2x+7.
\]
Ajouter 7 puis multiplier par 1,2 donne :
\[
f(g(x))=1,2(x+7)=1,2x+8,4.
\]
La différence est 8,4−7=1,4. La composition n'est pas commutative. Pour x=0, les résultats sont déjà distincts : 7 contre 8,4.

---

## F08 — Repères, unités et représentation

### P1 — Pente et interprétation

\[
m=\frac{24-18}{400-300}=\frac6{100}=0,06\text{ litre/km}.
\]
Sur l'intervalle observé, la consommation augmente en moyenne de 0,06 litre par kilomètre supplémentaire. Cette pente décrit la variation entre les deux points ; elle ne prouve pas que la relation est linéaire pour toutes les distances.

### P2 — Conversion de vitesse

\[
90\frac{km}{h}\times\frac{1000\ m}{1\ km}
\times\frac{1\ h}{3600\ s}
=25\frac{m}{s}.
\]
Les kilomètres et les heures se simplifient ; il reste des mètres par seconde. Le contrôle dimensionnel permet de vérifier l'unité finale.

### P3 — Comparaison des échelles

Première série : 40 à 80, variation absolue +40 et facteur 80/40=2, donc +100 %. Deuxième série : 400 à 800, variation absolue +400 et facteur 800/400=2, donc également +100 %.

Les variations absolues diffèrent d'un facteur 10, mais les variations relatives sont identiques. Une échelle logarithmique représente les rapports : un doublement correspond au même écart vertical sur les deux séries. Elle exige des valeurs strictement positives et doit être clairement signalée.

---

## Auto-évaluation

Après correction, reprendre sans notes les problèmes qui ont révélé :
- une confusion entre unité et valeur numérique ;
- une confusion entre variation en points et variation relative ;
- une transformation non équivalente non contrôlée ;
- une perte du domaine initial après simplification ;
- une interprétation excessive d'un résultat descriptif ;
- une confusion entre pente, taux et variation totale.

Le but n'est pas de mémoriser les résultats, mais de pouvoir reconstruire le raisonnement.
