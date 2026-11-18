# Démonstration — Moyenne ou médiane : quelle mesure résume vraiment un groupe ?

> Exemple fictif et original ; résultats vérifiés arithmétiquement.

## Question
Dans une équipe de sept personnes, les rémunérations mensuelles (en milliers d'euros) sont : 2,0 ; 2,1 ; 2,2 ; 2,3 ; 2,4 ; 2,5 ; 12,0. Quelle mesure décrit le mieux le salaire « typique » ?

## Objectifs
Calculer moyenne et médiane pour effectifs pairs/impairs ; expliquer la sensibilité de la moyenne ; savoir quand la moyenne répond à une question de total ; savoir quand la médiane décrit mieux le centre d'une distribution asymétrique ; vérifier les résultats avec Excel, Python et R ; automatiser si nécessaire avec VBA.

## Intuition
Si l'on verse tous les salaires dans une cagnotte puis qu'on répartit le total à parts égales, la part individuelle est la moyenne. Elle répond à « quel montant chacun recevrait-il si le total était distribué équitablement ? »

La médiane répond à « quelle valeur partage les observations ordonnées en deux moitiés ? » Elle dépend du rang, pas de la taille des écarts.

## Formalisation
Pour x₁,…,xₙ, x̄ = (1/n) Σxᵢ. Si n est impair, médiane = observation de rang (n+1)/2 après tri. Si n est pair, convention usuelle numérique : moyenne des observations de rang n/2 et n/2+1.

Somme = 25,5 ; moyenne = 25,5/7 = 3,642857… k€ ; médiane = 2,3 k€. La moyenne ne signifie pas que la plupart gagnent près de 3 643 €. La médiane indique que la moitié des observations est inférieure ou égale à 2 300 € et au moins la moitié supérieure ou égale.

## Modifier une observation
Remplacer 12,0 par 30,0 : somme = 43,5 ; moyenne = 43,5/7 = 6,214285… ; médiane reste 2,3. Une observation modifiée change fortement la moyenne, mais pas la médiane tant qu'elle reste au-dessus du rang central.

La médiane n'est pas toujours meilleure : elle ne conserve pas l'information sur le total et peut être moins adaptée à un coût moyen, une consommation attendue ou un bilan.

## Effectif pair
2,0 ; 2,1 ; 2,2 ; 2,4 ; 2,5 ; 12,0. Médiane = (2,2+2,4)/2 = 2,3 ; moyenne = 23,2/6 = 3,866666… k€.

## Ateliers sur les mêmes données
Entrer en A2:A8 : 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 12.0 (k€).

### Excel
- `=AVERAGE(A2:A8)` / `=MOYENNE(A2:A8)`.
- `=MEDIAN(A2:A8)` / `=MEDIANE(A2:A8)`.
- Trier une copie, puis observer un point plot ou boxplot. Les noms et séparateurs varient selon langue/version.

### Excel VBA
```vb
Option Explicit

Sub ResumeSalaire()
    Dim ws As Worksheet
    Dim valeurs As Range
    Set ws = ThisWorkbook.Worksheets("Donnees")
    Set valeurs = ws.Range("A2:A8")

    If Application.WorksheetFunction.Count(valeurs) = 0 Then
        MsgBox "Aucune observation numérique.", vbExclamation
        Exit Sub
    End If

    ws.Range("D2").Value = "Moyenne (k€)"
    ws.Range("E2").Value = Application.WorksheetFunction.Average(valeurs)
    ws.Range("D3").Value = "Médiane (k€)"
    ws.Range("E3").Value = Application.WorksheetFunction.Median(valeurs)
End Sub
```
En production : contrôler cellules vides, erreurs, textes, unités, feuille absente et plage dynamique.

### Python
```python
from statistics import mean, median

salaires = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 12.0]
print(f"Moyenne : {mean(salaires):.3f} k€")
print(f"Médiane : {median(salaires):.3f} k€")
```

### R
```r
salaires <- c(2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 12.0)
mean(salaires)
median(salaires)
summary(salaires)
boxplot(salaires, horizontal=TRUE,
        xlab="Salaire mensuel (milliers d'euros)")
```

## Erreurs fréquentes
- Dire que la moyenne représente toujours une personne typique.
- Dire que la médiane est toujours préférable.
- Comparer salaires sans définir brut/net, temps plein/partiel, période et population.
- Supprimer une valeur extrême sans vérifier si elle est erronée.
- Confondre moyenne des salaires et ratio masse salariale/effectif si les définitions ou pondérations diffèrent.

## Exercices
A. 4, 4, 5, 7, 10 : moyenne 6, médiane 5.
B. Ajouter 100 : moyenne 130/6 = 21,6667 ; médiane (5+7)/2 = 6.
C. Pour partager un budget total identique, la moyenne répond à total/effectif ; la médiane décrit le centre en rang.
D. « Le salaire moyen est de 3 643 €, donc un employé gagne environ 3 643 €. » Critique : distribution, médiane, effectif, définition, période, valeurs extrêmes et population manquent.

## Synthèse
Moyenne : centre d'équilibre arithmétique, sensible aux valeurs extrêmes. Médiane : centre en rang, résistante à une observation extrême isolée. Mode : valeur/catégorie la plus fréquente. Aucune mesure n'est universellement supérieure : la question, la distribution et l'objectif déterminent le choix.

## Références
- OpenIntro Statistics : https://www.openintro.org/book/os/
- Penn State STAT 200 : https://online.stat.psu.edu/stat200/
- NIST/SEMATECH EDA : https://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm
- R manual : https://cran.r-project.org/doc/manuals/r-release/R-intro.html
- Python statistics : https://docs.python.org/3/library/statistics.html
- Microsoft Excel Support : https://support.microsoft.com/en-us/excel
- Excel VBA : https://learn.microsoft.com/en-us/office/vba/api/overview/excel

Les données sont fictives ; les références documentent les méthodes, pas les chiffres illustratifs.
