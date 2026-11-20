Attribute VB_Name = "Bloc1Fondations"
Option Explicit

' F02 : rapport avec contrôle du dénominateur.
Public Function Ratio(ByVal Numerateur As Double, ByVal Denominateur As Double) As Variant
    If Denominateur = 0 Then
        Ratio = CVErr(xlErrDiv0)
    Else
        Ratio = Numerateur / Denominateur
    End If
End Function

' F03 : variation relative ; valeur initiale nulle = cas non défini.
Public Function VariationRelative(ByVal Initial As Double, ByVal Final As Double) As Variant
    If Initial = 0 Then
        VariationRelative = CVErr(xlErrNum)
    Else
        VariationRelative = Final / Initial - 1
    End If
End Function

' F03 : composition de deux taux décimaux signés.
Public Function VariationComposee(ByVal Taux1 As Double, ByVal Taux2 As Double) As Variant
    If Taux1 <= -1 Or Taux2 <= -1 Then
        VariationComposee = CVErr(xlErrNum)
    Else
        VariationComposee = (1 + Taux1) * (1 + Taux2) - 1
    End If
End Function

' F02 : partage proportionnel d'un montant selon un poids.
Public Function PartPonderee(ByVal Total As Double, ByVal Poids As Double, _
                             ByVal SommePoids As Double) As Variant
    If Poids < 0 Or SommePoids <= 0 Then
        PartPonderee = CVErr(xlErrNum)
    Else
        PartPonderee = Total * Poids / SommePoids
    End If
End Function

' F06 : résolution de ax+b=0. Renvoie une erreur si a=0.
Public Function SolutionLineaire(ByVal A As Double, ByVal B As Double) As Variant
    If A = 0 Then
        SolutionLineaire = CVErr(xlErrDiv0)
    Else
        SolutionLineaire = -B / A
    End If
End Function
