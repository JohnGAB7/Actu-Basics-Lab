# Bloc 1 — Corrigés des problèmes avancés

## 1. Décimaux et rationnels
\(17/600\) est irréductible et \(600=2^3\cdot3\cdot5^2\) contient un facteur 3 : pas de décimal fini. \(21/140=3/20\), dénominateur composé de 2 et 5 : décimal fini, \(0,15\). \(29/125\), avec \(125=5^3\), est fini : \(0,232\).

## 2. Tolérance numérique
On peut accepter \(|x-y|\leq\varepsilon_{abs}+\varepsilon_{rel}|y|\). La tolérance absolue protège les valeurs proches de zéro ; la relative adapte l'erreur à l'échelle. Les seuils doivent être définis selon les unités, les conséquences métier et la précision des données. Il n'existe pas de seuil universel.

## 3. Fréquence ajustée
A : \(54/900=0,06\), soit 6 sinistres pour 100 années-contrats. B : \(42/600=0,07\), soit 7 pour 100. Pour 1 000 années-contrats, les valeurs attendues sous stabilité sont 60 et 70. Il s'agit d'extrapolations de taux observés, pas de prédictions certaines.

## 4. Modèle de coût
\(C(q)=15+0,80q\). Le quotient \(C(q)/q=15/q+0,80\) varie avec \(q\) : pas de proportionnalité stricte. En soustrayant le coût fixe, \(C(q)-15=0,80q\), on isole une relation proportionnelle pour la partie variable.

## 5. Évolution composée
Facteur global : \(1,08\times0,95\times1,02=1,04652\), soit une hausse de 4,652 %. Le facteur annuel moyen est \(1,04652^{1/3}\), donc le taux moyen est environ 1,527 % par période.

## 6. Rebasage
Nouvel indice année 0 : \(100\times100/108\approx92,593\). Année 1 : 100. Année 2 : \(100\times117,72/108=109\). L'indice indique une hausse de 9 % entre années 1 et 2.

## 7. Temps de doublement
Chercher \(1,04^n>2\), donc \(n>\ln(2)/\ln(1,04)\approx17,67\). Le premier entier est 18. Vérifier que \(1,04^{17}<2\) et \(1,04^{18}>2\).

## 8. Croissance continue
Le taux continu \(r\) vérifie \(e^r=1,06\), donc \(r=\ln(1,06)\approx0,05827\), soit environ 5,827 % en convention continue. Le taux effectif de 6 % est le facteur annuel observé ; le taux continu est le logarithme de ce facteur.

## 9. Domaine après simplification
\(f(x)=((x-2)(x+2))/(x(x-2))\). Le domaine initial exclut 0 et 2. Pour \(x\ne0,2\), \(f(x)=(x+2)/x\). La valeur 2 reste exclue même si le facteur s'est simplifié.

## 10. Modèle de seuil
\(R(q)=-2(q^2-40q+250)\). Les racines sont \(q=20\pm5\sqrt{6}\), environ 7,753 et 32,247. Comme le coefficient dominant est négatif, \(R(q)>0\) entre les deux racines. Si \(q\) est une quantité non négative, cet intervalle est économiquement admissible ; l'interprétation dépend toutefois du domaine réel du modèle.

## 11. Système de tarification
\(3A+2B=190\), \(2A+5B=260\). Multiplier la première équation par 5 et la seconde par 2 : \(15A+10B=950\), \(4A+10B=520\). Soustraction : \(11A=430\), donc \(A=430/11\approx39,09\). Puis \(B=(190-3A)/2=\,?\) En remplaçant exactement : \(B= (190-1290/11)/2=400/11\approx36,36\). Vérification : \(3(430/11)+2(400/11)=2090/11=190\) et \(2(430/11)+5(400/11)=2860/11=260\).

## 12. Équation avec racine
Domaine : \(2x+3\geq0\) et le membre de gauche étant non négatif, l'égalité impose \(x\geq0\). En élevant au carré : \(2x+3=x^2\), soit \(x^2-2x-3=0=(x-3)(x+1)\). Les candidats sont 3 et -1 ; seul 3 respecte \(x\geq0\). Vérification : \(\sqrt9=3\).

## 13. Composition
\(c(k(m))=4+0,35(1,609m)=4+0,56315m\). Le coût fixe est 4 unités monétaires et la pente vaut 0,56315 unité monétaire par mile.

## 14. Injectivité et restriction
Sur \(\mathbb R\), non injective car \(f(0)=f(2)=1\). Sur \([1,+\infty[\), elle est strictement croissante et injective. Son image est \([0,+\infty[\) et sa réciproque est \(f^{-1}(y)=1+\sqrt y\).

## 15. Unités et pente
Pente : \(3/75=0,04\) litre/km. Avec une droite passant par l'origine, à 500 km la consommation estimée est \(0,04\times500=20\) litres. L'extrapolation suppose que le taux moyen reste constant.

## 16. Lecture critique
Série 1 : hausse absolue de 10 et relative de 10 %. Série 2 : hausse absolue de 2 et relative de 20 %. La première contribue davantage en valeur absolue ; la seconde progresse davantage proportionnellement. Une échelle linéaire met en évidence les écarts absolus, tandis qu'une comparaison de variations relatives peut être présentée en pourcentage ou sur une échelle logarithmique.
