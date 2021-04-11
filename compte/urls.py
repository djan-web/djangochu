from django.urls import path
from . import views

urlpatterns = [
    path('inscription', views.inscriptionPage, name="Inscription"),
    path('acces', views.Acces, name="acces"),
    path('quitter', views.logout, name="quitter")
]