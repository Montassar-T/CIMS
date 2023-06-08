from django.urls import path
from . import views 

urlpatterns =[
    path('', views.home, name='home'),
    path('stage/', views.stage, name='stage'),
    path('contact/', views.contact, name='contact'),
    path('formation/applicative/', views.appli, name='applicative'),
    path('formation/bureautique/', views.bureau, name='bureau'),
    path('formation/platforme', views.elearning, name='elearning')
]