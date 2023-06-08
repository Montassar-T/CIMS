from django import forms
from .models  import *

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ["nom","prenom","date_naissance","telephone","email","etablissement","classe"]

class DemandeStageForm(forms.ModelForm):
    class Meta:
        model = DemandeStage   
        fields=["type_stage"]


class EmployeeForm(forms.ModelForm):
     class Meta:
        model = Employee
        fields = ["nom","prenom","cin","telephone","email","etablissement","grade"]

class ApplicativeForm(forms.ModelForm):
    class Meta:
        model = Applicative
        fields= ["theme"]

class BureautiqueForm(forms.ModelForm):
    class Meta:
        model = Bureautique
        fields= ["theme","niveau"]


class DemandeAccesForm(forms.ModelForm):
    class Meta:
        model = DemandeAcces
        fields= []
