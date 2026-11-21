# Exercices corrigés — dérivée et techniques de dérivation

**Programme B · Bloc 1 · Calcul différentiel introductif**  
20 exercices progressifs, avec calculs, preuves, domaines, interprétations et questions de transfert.

## Énoncés

### A. Définition et sens de la dérivée

**1. Définition.** À partir du quotient différentiel, calculer la dérivée de \(f(x)=3x+2\).

**2. Définition.** À partir du quotient différentiel, calculer la dérivée de \(f(x)=x^2-4x\).

**3. Continuité et dérivabilité.** Montrer que \(f(x)=|x|\) est continue en zéro mais non dérivable en zéro.

**4. Tangente.** Déterminer l'équation de la tangente à \(f(x)=x^2+1\) au point d'abscisse 2.

### B. Règles de dérivation

**5. Polynôme.** Calculer \(f'(x)\) pour \(f(x)=4x^5-3x^3+2x-7\).

**6. Produit.** Dériver \(f(x)=(x^2+1)e^x\).

**7. Quotient.** Dériver \(f(x)=(2x+1)/(x-3)\), en précisant le domaine.

**8. Chaîne.** Dériver \(f(x)=(5x^2-2x+1)^4\).

**9. Exponentielle composée.** Dériver \(f(x)=e^{3x^2-1}\).

**10. Logarithme composé.** Déterminer le domaine puis dériver \(f(x)=\ln(x^2+1)\).

**11. Trigonométrie composée.** Dériver \(f(x)=\sin(4x^3)\).

**12. Puissance réelle.** Dériver \(f(x)=x^{3/2}\) sur son domaine réel de dérivabilité.

### C. Inverse et implicite

**13. Fonction réciproque.** Retrouver la dérivée de \(\ln x\) à partir de la dérivée de l'exponentielle et de la formule de dérivation d'une réciproque.

**14. Dérivation implicite.** Pour \(x^2+xy+y^2=7\), déterminer \(dy/dx\) lorsque la relation définit localement \(y\) comme fonction de \(x\).

### D. Dérivées d'ordre supérieur et interprétation

**15. Dérivée seconde.** Pour \(f(x)=x^4-2x^3+x\), calculer \(f'\) et \(f''\).

**16. Sensibilité.** Un indicateur vaut \(R(\theta)=100e^{0,02\theta}\). Calculer \(R'(\theta)\), puis interpréter \(R'(0)\).

**17. Vitesse.** La position d'un mobile est \(s(t)=t^3-6t^2+9t\), en mètres, \(t\) en secondes. Calculer vitesse et accélération, puis la vitesse à \(t=2\).

### E. Raisonnement et contrôle

**18. Faux raisonnement.** Un étudiant affirme : « \(f'(a)=0\), donc \(f\) a un maximum en \(a\). » Donner un contre-exemple et expliquer.

**19. Différences finies.** Pour \(f(x)=x^2\), calculer l'approximation avant \([f(2+h)-f(2)]/h\), puis la différence centrée \([f(2+h)-f(2-h)]/(2h)\). Comparer à la dérivée exacte.

**20. Domaine et dérivabilité.** Étudier le domaine et la dérivabilité de \(f(x)=\sqrt{x^2-1}\). Identifier les points où la formule de la dérivée ne s'applique pas.

---

## Corrigés détaillés

### 1. Fonction affine

\[
\frac{f(x+h)-f(x)}h
=\frac{3(x+h)+2-(3x+2)}h=3.
\]
La limite vaut 3, donc \(\boxed{f'(x)=3}\).

### 2. Polynôme quadratique par définition

\[
\frac{f(x+h)-f(x)}h
=\frac{(x+h)^2-4(x+h)-x^2+4x}{h}
=2x+h-4.
\]
Lorsque \(h\to0\), la limite vaut \(2x-4\). Donc \(\boxed{f'(x)=2x-4}\).

### 3. Valeur absolue

La continuité en zéro découle de \(|f(x)-f(0)|=|x|\to0\). Pour la dérivée :
\[
\frac{|h|-0}{h}=
\begin{cases}1,&h>0,\\-1,&h<0.\end{cases}
\]
Les limites latérales diffèrent. La dérivée bilatérale n'existe pas.

### 4. Tangente

\(f'(x)=2x\), donc \(f'(2)=4\) et \(f(2)=5\). L'équation est
\[
y-5=4(x-2),\quad\boxed{y=4x-3}.
\]

### 5. Polynôme

\[
\boxed{f'(x)=20x^4-9x^2+2}.
\]
La dérivée d'une constante est nulle.

### 6. Produit

\[
f'(x)=2xe^x+(x^2+1)e^x
=\boxed{e^x(x^2+2x+1)=e^x(x+1)^2}.
\]

### 7. Quotient

Domaine : \(\mathbb R\setminus\{3\}\). Par la règle du quotient :
\[
f'(x)=\frac{2(x-3)-(2x+1)}{(x-3)^2}
=\boxed{-7/(x-3)^2}.
\]

### 8. Chaîne

\[
f'(x)=4(5x^2-2x+1)^3(10x-2)
=\boxed{(40x-8)(5x^2-2x+1)^3}.
\]

### 9. Exponentielle composée

La dérivée de l'exposant \(3x^2-1\) est \(6x\). Ainsi
\[
\boxed{f'(x)=6xe^{3x^2-1}}.
\]

### 10. Logarithme composé

Comme \(x^2+1>0\) pour tout réel, le domaine est \(\mathbb R\). Par composition :
\[
\boxed{f'(x)=\frac{2x}{x^2+1}}.
\]

### 11. Trigonométrie composée

La dérivée de \(4x^3\) vaut \(12x^2\), donc
\[
\boxed{f'(x)=12x^2\cos(4x^3)}.
\]

### 12. Puissance réelle

La fonction \(x^{3/2}\) est réelle pour \(x\ge0\). Pour \(x>0\),
\[
\boxed{f'(x)=\frac32x^{1/2}}.
\]
Au point zéro, la dérivée à droite vaut
\[
\lim_{h\to0^+}\frac{h^{3/2}-0}{h}
=\lim_{h\to0^+}\sqrt h=0.
\]
Elle admet donc une dérivée à droite nulle au bord du domaine ; la dérivée bilatérale usuelle sur un ouvert de \(\mathbb R\) n'est pas définie en zéro.

### 13. Dérivée de ln par réciproque

Soit \(f(x)=e^x\). Sa dérivée est \(e^x\), jamais nulle, et sa réciproque est \(f^{-1}(y)=\ln y\), pour \(y>0\). La formule donne
\[
(f^{-1})'(y)=\frac{1}{f'(\ln y)}
=\frac{1}{e^{\ln y}}=\boxed{1/y}.
\]

### 14. Dérivation implicite

En dérivant :
\[
2x+(y+xy')+2yy'=0.
\]
On regroupe :
\[
(x+2y)y'=-(2x+y).
\]
Donc, lorsque \(x+2y\ne0\),
\[
\boxed{y'=-\frac{2x+y}{x+2y}}.
\]
Le dénominateur non nul correspond à la condition locale qui permet de résoudre la relation pour une pente finie.

### 15. Dérivées successives

\[
f'(x)=4x^3-6x^2+1,\qquad
\boxed{f''(x)=12x^2-12x}.
\]

### 16. Sensibilité

\[
R'(\theta)=100(0,02)e^{0,02\theta}
=\boxed{2e^{0,02\theta}}.
\]
À \(\theta=0\), \(R'(0)=2\). L'indicateur vaut alors 100 et sa pente locale est 2 unités d'indicateur par unité de \(\theta\). Cette interprétation suppose que l'échelle et l'unité de \(\theta\) sont définies par le modèle.

### 17. Vitesse et accélération

\[
v(t)=s'(t)=3t^2-12t+9,
\quad a(t)=v'(t)=6t-12.
\]
À \(t=2\), \(v(2)=12-24+9=\boxed{-3\text{ m/s}}\). Le signe négatif indique un mouvement dans le sens négatif de l'axe choisi. \(a(2)=0\text{ m/s}^2\).

### 18. Un point stationnaire n'est pas nécessairement un extremum

Prenons \(f(x)=x^3\). Alors \(f'(x)=3x^2\), donc \(f'(0)=0\), mais la fonction est strictement croissante de part et d'autre de zéro. Aucun maximum ni minimum local n'y est atteint. La condition \(f'(a)=0\) est seulement une condition nécessaire pour un extremum local intérieur lorsque la dérivée existe, pas une condition suffisante.

### 19. Différences finies

Pour \(f(x)=x^2\),
\[
\frac{f(2+h)-f(2)}h
=\frac{(2+h)^2-4}{h}=4+h.
\]
L'erreur par rapport à \(f'(2)=4\) est \(h\).

La différence centrée vaut
\[
\frac{(2+h)^2-(2-h)^2}{2h}
=\frac{8h}{2h}=4.
\]
Elle est exacte ici pour tout \(h\ne0\), car la fonction est quadratique. Cette exactitude particulière ne doit pas être généralisée à toutes les fonctions.

### 20. Racine et domaine

Il faut \(x^2-1\ge0\), donc
\[
D=(-\infty,-1]\cup[1,+\infty).
\]
Pour \(|x|>1\),
\[
f'(x)=\frac{2x}{2\sqrt{x^2-1}}
=\boxed{\frac{x}{\sqrt{x^2-1}}}.
\]
Aux points \(x=\pm1\), le dénominateur est nul et la formule n'est pas applicable. Les dérivées unilatérales dans le domaine deviennent non bornées en valeur absolue ; il n'existe pas de dérivée finie au sens usuel à ces extrémités.

## Barème indicatif

| Compétence | Exercices | Points |
|---|---:|---:|
| Définition, continuité, tangente | 1–4 | 20 |
| Règles de dérivation | 5–12 | 35 |
| Réciproque et implicite | 13–14 | 15 |
| Dérivées d'ordre supérieur et applications | 15–17 | 15 |
| Critique et numérique | 18–20 | 15 |
| **Total** | **20** | **100** |

Seuil pédagogique suggéré : 80/100, avec reprise obligatoire des erreurs de règle de chaîne, de domaine et d'interprétation de \(f'(a)=0\). Ce seuil est une convention interne, pas une norme académique universelle.

## Questions de défense orale

1. Pourquoi la dérivée est-elle une limite et non une pente sécante ?
2. Pourquoi la dérivabilité implique-t-elle la continuité ?
3. Pourquoi la continuité n'implique-t-elle pas la dérivabilité ?
4. D'où vient le facteur intérieur dans la règle de chaîne ?
5. Pourquoi les angles doivent-ils être exprimés en radians dans les formules usuelles ?
6. Pourquoi une dérivée nulle n'assure-t-elle pas un extremum ?
7. Que signifie l'unité de \(f'(x)\) dans un modèle ?
8. Pourquoi une différence finie n'est-elle pas une preuve de dérivabilité ?

## Références

- MIT OpenCourseWare, [18.01 Single Variable Calculus — notes de cours](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2005/pages/lecture-notes/).
- OpenStax, [Calculus Volume 1 — définition de la dérivée](https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative) et [règles de dérivation](https://openstax.org/books/calculus-volume-1/pages/3-3-differentiation-rules).
- MIT OpenCourseWare, [18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/).

