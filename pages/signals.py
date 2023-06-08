from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
import random
from django.contrib.auth.models import User
from django.contrib.auth import get_user



@receiver(post_save, sender=DemandeAcces)
def send_email_to_employee(sender, instance, **kwargs):
    if instance.etat == 1 :
        send_mail(
            'Demande d\'accès',
            'Félicitation votre compte  a été créé. Voici les paramètres : \n\nNomUtilisateur: " '+instance.NomUtilisateur+' " \n\nMotdePasse: " '+instance.MotPasse+' "',      
            'tayarimonta@gmail.com',
            [instance.id_employee.email],
            fail_silently=True,
        )
    

@receiver(post_save, sender=DemandeStage)
def send_email_to_student(sender, instance, **kwargs):
    if instance.etat == 1 :
        send_mail(
            'Demande de stage',
            'Bonjour,\n\nVotre demande de stage a été acceptée \nMerci de nous contacter.',
            'tayarimonta@gmail.com',
            [instance.id_etudiant.email],
            fail_silently=True,
        )
    
   
@receiver(post_save, sender=Applicative)
def send_email_to_student(sender, instance, **kwargs):
    if instance.etat == 1 :
        send_mail(
            'Demande de formation',
            'Bonjour,\n\nVotre demande de stage a été acceptée \nMerci de faire une demande d\'aacès au plateforme E-learning.',
            'tayarimonta@gmail.com',
            [instance.id_employee.email],
            fail_silently=True,
        )
@receiver(post_save, sender=Bureautique)
def send_email_to_student(sender, instance, **kwargs):
    if instance.etat == 1 :
        send_mail(
            'Demande de formation',
            'Bonjour,\n\nVotre demande a été acceptée\nMerci de faire une demande d\'aacès au plateforme E-learning.',
            'tayarimonta@gmail.com',
            [instance.id_employee.email],
            fail_silently=True,
        )
