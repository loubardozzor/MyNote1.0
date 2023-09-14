from django.shortcuts import render, redirect
from django.http import  HttpResponse
from appunti.models import Studente
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from MyNotes import settings
from django.core.mail import send_mail # la funzione che manda in modo automatico una mail
# Create your views here.
def acceuil(request):
    return render(request, "autenticazione/index.html")

def register(request):
    if request.method == 'POST': #l'user invia il form compilato per la registrazione
        nome = request.POST['nome']
        cognome = request.POST['cognome']
        dataNascita = request.POST['dataNascita']
        email = request.POST['email']
        password = request.POST['password']
        passwordconfirm = request.POST['passwordConfirm']
        username = request.POST['username']

        """ controllo degli input di creazione 
        dell'account dell'utente lato server
            """
        if User.objects.filter(username=username):# se c'è  un account che ha gia chesto nome come user dobbiamo impedire
            messages.error(request, 'questo username è gia usato in altro account ')
            return redirect('register')
        if User.objects.filter(email = email):
            messages.error(request, 'questo email è gia usato da un altro account')
            return redirect('register')
        if password != passwordconfirm:
            messages.error(request, 'i passwords non coincidono')
            return redirect('register')

        if not username.isalnum():
            messages.error(request, 'lo username deve essere alfanumerico')
            return redirect('register')
        # quindi l'oggetto messages è accessibile diretamente dai template senza avere bisogno di passarli


        # nuovo studente che si registra sull'applicazione
        oggetto_con_max_id = Studente.objects.latest('id')
        max_id = oggetto_con_max_id.id
        nuovo_studente = Studente(max_id+1, nome, cognome, dataNascita, username, password, email)
        nuovo_studente.save() # registramo il nuovo utente come studente
        mio_user = User.objects.create_user(username, email, password)
        mio_user.first_name = nome
        mio_user.last_name = cognome
        mio_user.save() # registrare il nuovo utente come user dell'applicazione
        messages.success(request, 'la creazione del tuo account è andato a buon fine')

        """ quando una persona crea un account l'inviamo direttamento un email di benvenuto"""

        subject = "Benvenuto su MyNotes" # titolo del messaggio di benvenuto
        message = "Benvenuto "+mio_user.first_name + " " + mio_user.last_name + "\n Siamo felici di averti con noi ! \n\n\n Grazie \n\n MyNotes" #messaggio di benvenuto
        from_email = settings.EMAIL_HOST_USER # sender dell'email
        to_list = [mio_user] # receivers dell'email
        send_mail(subject, message, from_email, to_list, fail_silently=False) # invio dell'email con fail_silently=False mi notifica se è successo qualcosa nell'invio


        return redirect('login')
    else:
        pass

    return render(request, 'autenticazione/register.html')


def lOgin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password) # controllo se l'utente è registrato prima di effettuare il suo login
        if user is not None: # l'utente è autenticato
            login(request, user)
            nome = user.first_name
            cognome = user.last_name
            messages_benvenuto_utente = "ciao {0} {0} benvenuto su MyNotes".format(nome, cognome)
            context = {"nome": nome, "cognome": cognome}
            return render(request, 'appunti/home.html', context) # torno nella pagina principale per specificare che l'user si è logato disabilitando il bottone di login, registrati e facendo aapparire solo il bottone di lougout
        else:
            messages.error(request, "l'autenticazone è andata a storto")
            return redirect('login')
    return render(request, 'autenticazione/login.html') # quando l'user si è logato torniamo nell'app principale appunti

def lOgout(request):
    logout(request)
    messages.success(request, 'logout andato a buon fine!')
    return redirect('home')
    pass