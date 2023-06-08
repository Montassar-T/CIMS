
from django.shortcuts import *
from .models import *
from django.core.mail import send_mail
from .forms import*
from django.contrib import messages
import random



# Create your views here.

def home(request):
    return render(request,'pages/index.html')

def stage(request):
    
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        demande = DemandeStageForm(request.POST)
        etudiant = EtudiantForm(request.POST)
        if demande.is_valid() and etudiant.is_valid():
            demande = demande.save(commit=False)
            instance = etudiant.save()
            demande.id_etudiant = instance
            if request.user.is_authenticated:
                demande.id_admin = request.user
            else:
                demande.id_admin = User.objects.first()
            demande.save()
        else:
            nom= request.POST['nom']
            prenom= request.POST['prenom']
            date_naissance= request.POST['date_naissance']
            telephone= request.POST['telephone']
            email= request.POST['email']
            etablissement= request.POST['etablissement']
            classe=request.POST['classe']

            for field in etudiant:
                for error in field.errors:
                    messages.error(request, error)

            return render(request,'pages/demande.html', {'nom' : nom ,'prenom': prenom ,'email':email,'date_naissance': date_naissance ,'etablissement': etablissement,'classe':classe})
            
            
        return render(request,'pages/index.html',{'nom': nom , 'prenom':prenom})

    else:    
        return render(request,'pages/demande.html')



def contact(request):

    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email= request.POST['email']
        sujet= request.POST['sujet']
        message= request.POST['message']
        send_mail(
            sujet,
            message,
            email,
            #**************** Change the email later ***************
            ['montassartayari14@gmail.com'],
            fail_silently=True,

            )
       
        return render(request,'pages/contact.html',{'nom' :nom , 'prenom' : prenom })
    else:   
        return render(request,'pages/contact.html')



def appli(request):
    
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        employee= EmployeeForm(request.POST)
        demande= ApplicativeForm(request.POST)
        if employee.is_valid() and demande.is_valid():
            demande = demande.save(commit=False)
            insatnce = employee.save()
            demande.id_employee = insatnce
            demande.id_admin = User.objects.first()
            demande.save()
        else:
            nom= request.POST['nom']
            prenom= request.POST['prenom']
            cin= request.POST['cin']
            telephone= request.POST['telephone']
            email= request.POST['email']
            etablissement= request.POST['etablissement']
            grade=request.POST['grade']
           
            for field in employee:
                for error in field.errors:
                    messages.error(request, error)
            return render(request,'pages/appli.html', {'nom' : nom ,'prenom': prenom ,'cin': cin ,'email':email,'etablissement': etablissement,'grade':grade  })

        return render(request,'pages/index.html',{'nom' : nom , 'prenom': prenom})
    else:
        return render(request,'pages/appli.html')





    

def bureau(request):

    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        employee= EmployeeForm(request.POST)
        demande= BureautiqueForm(request.POST)
        if employee.is_valid() and demande.is_valid():
            demande = demande.save(commit=False)
            instance = employee.save()
            demande.id_employee = instance
         
            demande.id_admin = User.objects.first()

            demande.save()
        else:
            nom= request.POST['nom']
            prenom= request.POST['prenom']
            cin= request.POST['cin']
            telephone= request.POST['telephone']
            email= request.POST['email']
            etablissement= request.POST['etablissement']
            grade=request.POST['grade']
           
            for field in employee:
                for error in field.errors:
                    messages.error(request, error)
            return render(request,'pages/bureau.html', {'nom' : nom ,'prenom': prenom ,'cin': cin ,'email':email,'etablissement': etablissement,'grade':grade  })

        return render(request,'pages/index.html',{'nom' : nom , 'prenom': prenom})
    else:
        return render(request,'pages/bureau.html')







def elearning(request):
    
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        employee= EmployeeForm(request.POST)
        demande= DemandeAccesForm(request.POST)
        if employee.is_valid() and demande.is_valid():
    
            demande = demande.save(commit=False)
            instance = employee.save()
            demande.id_employee = instance
           
            demande.id_admin = User.objects.first()
            username= nom.lower()+'.'+prenom.lower()

            characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?"]

            password_length = 16
            password = "".join(random.sample(characters, password_length))
            demande.MotPasse= password
            demande.NomUtilisateur=username.replace(" ", "")
            demande.save()
            
        else:
            nom= request.POST['nom']
            prenom= request.POST['prenom']
            cin= request.POST['cin']
            telephone= request.POST['telephone']
            email= request.POST['email']
            etablissement= request.POST['etablissement']
            grade=request.POST['grade']
           
            for field in employee:
                for error in field.errors:
                    messages.error(request, error)
            return render(request,'pages/elearning.html', {'nom' : nom ,'prenom': prenom ,'cin': cin ,'etablissement': etablissement,'grade':grade  })

        return render(request,'pages/index.html',{'nom' : nom , 'prenom': prenom})
    else:
        return render(request,'pages/elearning.html')

















