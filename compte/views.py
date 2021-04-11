from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Creeruser
from django.contrib.auth import authenticate, login


# Create your views here.
def inscriptionPage(request):
    form = Creeruser()
    if request.method=='POST':
        form = Creeruser(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'compte créé'+user)
            return redirect('acces')
    context={'form':form}
    return render(request, 'app/inscription.html', context)

def Acces(request):
    context = {}
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('acceuil')
        else:
            messages.info(request, "il y a une erreur nom utilisateur ou mot de passe incorrect")

    return render(request, 'app/login_2.html', context)


def logout(request):
    logout(request)
    return redirect('acces')

