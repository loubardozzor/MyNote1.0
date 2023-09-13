from django.shortcuts import render, redirect
from django.http import  HttpResponse
from appunti.models import Studente
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def acceuil(request):
    return render(request, "autenticazione/index.html")

def register(request):
    if request.method == 'POST': #l'user invia il form compilato per la registrazione
        nome = request.POST['nome']
        cognome = request.POST['cognome']
        dataNascita = request.POST['dataNascita"']
        email = request.POST['email']
        password = request.POST['password']
        passwordconfirm = request.POST['passwordConfirm']
        username = request.POST['username']
        mio_user = Studente.objects.create()
        mio_user.nome = nome
        mio_user.cognome = cognome
        mio_user.Username = username
        mio_user.dataNascita = dataNascita
        mio_user.password = password
        mio_user.save() # registrare il nuovo user
        messages.success(request, 'la creazione del tuo account è andato a buon fine')
        return redirect('login')
    else:
        pass

    return render(request, 'autenticazione/register.html')


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password) # controllo se l'utente è registrato prima di effettuare il suo login
        if user is not None: # l'utente è autenticato
            login(request,user)
            nome = user.nome
            cognome = user.cognome
            context = {"nome": nome, "cognome": cognome}
            return render(request, 'autenticazione/login.html',context)

    return render(request, 'autenticazione/index.html') # quando l'user si è logato torniamo nell'app principale appunti

def logout(request):
    pass