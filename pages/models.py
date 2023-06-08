from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    date_naissance = models.DateField()
    telephone = models.IntegerField(unique=True, error_messages={"unique":"Le numéro est déja utilisé"})
    email = models.EmailField() 
    etablissement = models.CharField(max_length=100)
    classe = models.CharField(max_length=20)
    def __str__(self):    
        return self.nom.lower() + ' '+ self.prenom.lower()
            


class DemandeStage(models.Model):
    id_etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    type_stage= models.CharField(max_length=20)
    etat= models.IntegerField(default=0)
    id_admin=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        if self.etat == 1 :
            return self.type_stage+': ' + self.id_etudiant.nom.lower() +' '+self.id_etudiant.prenom.lower()+'(Accepté)'

        elif self.etat == -1:
            return self.type_stage+': ' + self.id_etudiant.nom.lower() +' '+self.id_etudiant.prenom.lower()+'(Refusé)'

        else:
            return self.type_stage+': ' + self.id_etudiant.nom.lower() +' '+self.id_etudiant.prenom.lower()





class Employee(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    telephone = models.IntegerField()
    cin = models.IntegerField(unique=True, error_messages={"unique":"Le numéro de cin est déja utilisé"})
    etablissement = models.CharField(max_length=100) 
    grade = models.CharField(max_length=100) 
    def __str__(self):
        return self.nom.lower() + ' '+ self.prenom.lower()


class DemandeAcces(models.Model):
    id_employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    MotPasse =models.CharField(max_length=16, null=True)
    NomUtilisateur =models.CharField(max_length=100, null=True)
    etat= models.IntegerField(default=0)
    id_admin=models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        if self.etat == 1 :
            return self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()+'(Accepté)'
        elif self.etat == -1:   
            return self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()+'(Refusé)'
        else:
            return self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()
  

class Bureautique(models.Model):
    id_employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    theme = models.CharField(max_length=100) 
    niveau = models.CharField(max_length=100) 
    etat= models.IntegerField(default=0)
    id_admin=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        if self.etat == 1 :
            return self.theme+' niveau '+self.niveau  +': ' + self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()+'(Accepté)'
        elif self.etat == -1:   
            return self.theme+' niveau '+self.niveau  +': ' + self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()+'(Refusé)'
        else:
            return self.theme+' niveau '+self.niveau  +': ' + self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()


class Applicative(models.Model):
    id_employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    theme = models.CharField(max_length=100) 
    etat= models.IntegerField(default=0)
    id_admin=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        if self.etat == 1 :
            return self.theme+': ' + self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()+'(Accepté)'
        elif self.etat == -1:   
            return self.theme+': ' + self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()+'(Refusé)'
        else:
            return self.theme+': ' + self.id_employee.nom.lower() +' '+self.id_employee.prenom.lower()



