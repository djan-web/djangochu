import serial

from django.shortcuts import render
from .models import Patient
from .form import PatientForm
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url="acces")
def index(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'app/index.html', context)


def pat(request):
    tab = Patient.objects.all()

    s={'tab': tab}
    return render(request,'app/tab.html',s)


def ard(request, pk):
    arduino = serial.Serial('COM4', 9600)
    query = "SELECT Status FROM formulaire_patient WHERE id = 'arduino'"
    tab = Patient.objects.raw(query)
    if arduino.read() == pk:
        if request.method == 'GET':
            form = PatientForm(request.GET)


def Dbord(request):
    patient = Patient.objects.all().count()
    cardio = Patient.objects.filter(services='cardiologie').count()
    maternité = Patient.objects.filter(services='maternité').count()
    Pédiatrie = Patient.objects.filter(services='Pédiatrie').count()
    traumatologie = Patient.objects.filter(services='traumatologie').count()
    pneumologie = Patient.objects.filter(services='pneumologie').count()
    immunologie = Patient.objects.filter(services='immunologie').count()


    context = {'patient':patient, 'cardio':cardio,'maternité':maternité,'Pédiatrie':Pédiatrie
               ,'traumatologie':traumatologie,'pneumologie':pneumologie,'immunologie':immunologie}

    return render(request,'app/Dbord.html',context)