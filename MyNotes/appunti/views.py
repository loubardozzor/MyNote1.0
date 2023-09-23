from django.shortcuts import render
from appunti.models import *
from django.http import FileResponse
from .forms import *
from django.shortcuts import   get_object_or_404
from django.utils import timezone
from datetime import datetime
from django.shortcuts import redirect  # ajoutez cet import
from django.http import  HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from .forms import RecenzioneForm
""" la views che ritorna la home page"""

def home(request):
    return render(request, 'appunti/home.html')

""" la views che ritorna la lista delle materie"""
def materie_list(request):
    percorso = [{'nome': 'Materie Disponibili', 'url': 'materie/'}]
    materie = Materia.objects.all()
    context = {"materie": materie, 'percorso': percorso}
    return render(request, 'appunti/materie_list.html', context)

""" la via che ritorna una singola materia con la lista degli appunti essa associata"""
def materia_detail(request, materia_id):
    materia = Materia.objects.get(id=materia_id)
    appunti_materia_curr = Appunto.objects.filter(materia_id = materia)
    url_corrente = "materie/{0}".format(materia_id)
    elemento_corrente = {"nome": materia.nome, 'url': url_corrente}
    percorso = [{"nome": "Materie Disponibili", "url":"materie/"},]

    percorso.append(elemento_corrente)

    context = {"materia": materia, "appunti_materia_curr": appunti_materia_curr, "percorso": percorso}
    return render(request, 'appunti/materia_detail.html', context)

""" la view che ritorna la pagina di successo caricamento"""
def pagina_di_successo_caricamento(request):
    return render(request, 'appunti/pagina_di_successo_caricamento.html')


""" la view che ritorna la pagina di insuccesso caricamento """
def pagina_di_insuccesso_caricamento(request):
    return render(request, 'appunti/pagina_di_insuccesso_caricamento.html')



""" la view che gestisce il caricamento di un appunto """

def upload_appunto(request, materia_id):
    if request.method == 'POST': # se la richiesta è post quindi l'utente manda il modulo compilato
        form = CaricamentoAppuntoForm(request.POST, request.FILES)
        if form.is_valid():
            # salviamo il documento nel database che contiene dati sul documento
            data_ora_attuale = timezone.now()
            nome_appunto = form.cleaned_data['nome_appunto']
            pdf_appunto = form.cleaned_data['pdf_appunto']
            oggetto_con_max_id = Appunto.objects.latest('id')
            max_id = oggetto_con_max_id.id

            #recuperiamo il riferimento nella tabella studente dell'user corrente che carica il documento
            username_userCurr = request.user #username dell'utente attualmente autenticato
            user_curr = Studente.objects.get(Username = username_userCurr)

            nuovo_appunto = Appunto(max_id + 1, nome_appunto, pdf_appunto, 0, 0, user_curr.id, materia_id, data_ora_attuale)
            nuovo_appunto.save()
            return redirect('materia-detail', materia_id) # ridirezione dgli appunti per la materia corrente
        else:
            return redirect('pagina_di_incuccesso_caricamento') # ridirezione alla pagina di insuccesso
    else: # l'utente richiede il modulo per compilare dobbiamo verificare se l'utente è autenticato
        if request.user.is_authenticated: # se l'utente è autenticato gli faccio accedere alla pagina di download degli appunti
            form = CaricamentoAppuntoForm()
            materia = Materia.objects.get(id=materia_id)
            appunti_materia_curr = Appunto.objects.filter(materia_id=materia)
            url_corrente = 'materie/{0}'.format(materia_id)
            materia_elemento = {"nome": materia.nome, 'url': url_corrente}
            percorso = [{"nome": "Materie Disponibile", 'url': "materie/"}, ]
            url_appunto_upload = url_corrente+'/upload-appunto'
            upload_appunto={"nome": 'upload_appunto', 'url': url_appunto_upload}
            percorso.append(materia_elemento)
            percorso.append(upload_appunto)

            context = {'form':form, 'materia': materia, "percorso": percorso}
            return render(request, 'appunti/upload_appunto.html', context)
        else: # lo mandiamo nella pagina di login
            return redirect('login')


def delete_appunto(request, materia_id , appunto_id):
    appunto = Appunto.objects.get(id=appunto_id)
    if request.method == 'POST':  # se mando il comando per cancellare
        appunto.delete()
        return redirect('materia-detail', materia_id)
    context = {'appunto': appunto}
    return render(request,
                  'appunti/delete_appunto.html', context)


def update_appunto(request, materia_id, appunto_id): # implementazione futuro
    context = {'materia_id': materia_id, 'appunto_id': appunto_id}
    return render(request, 'appunti/update_appunto.html', context)


def update_appunto_name(request, materia_id, appunto_id):
    if request.method == 'POST': #
        form = ModificaNomeAppuntoForm(request.POST)
        if form.is_valid():
            # salviamo il documento nel database che contiene dati sul documento
            data_ora_attuale = timezone.now()
            nuovo_nome_appunto = form.cleaned_data['nome_appunto']
            # recuperiamo nella database gli appunti di cui dobbiamo modificare il nome
            appunto = Appunto.objects.get(id=appunto_id)
            appunto.nome_appunto = nuovo_nome_appunto
            appunto.save()
            return redirect('materia-detail', materia_id) # ridirezione dgli appunti per la materia corrente
        else:
            return redirect('pagina_di_incuccesso_caricamento') # ridirezione alla pagina di insuccesso
    else:
        appunto = Appunto.objects.get(id=appunto_id)
        form = ModificaNomeAppuntoForm()
        context = {'form': form, 'appunto': appunto}
        return render(request, 'appunti/update_appunto_element.html', context)


def update_appunto_pdf(request, materia_id, appunto_id):
    if request.method == 'POST': #
        form = ModificapdfAppuntoForm(request.POST)
        if form.is_valid():
            # salviamo il documento nel database che contiene dati sul documento
            data_ora_attuale = timezone.now()
            nuovo_pdf_appunto = form.cleaned_data['pdf_appunto']
            # recuperiamo nella database gli appunti di cui dobbiamo modificare il nome
            appunto = Appunto.objects.get(id=appunto_id)
            appunto.pdf_appunto = nuovo_pdf_appunto
            appunto.save()
            return redirect('materia-detail', materia_id) # ridirezione dgli appunti per la materia corrente
        else:
            return redirect('pagina_di_incuccesso_caricamento') # ridirezione alla pagina di insuccesso
    else:
        appunto = Appunto.objects.get(id=appunto_id)
        form = ModificapdfAppuntoForm(request.POST)
        context = {'form': form, 'appunto': appunto}
        return render(request, 'appunti/update_appunto_element.html', context)



def update_appunto_namePdf(request, materia_id, appunto_id):
    if request.method == 'POST': #
        form = ModificaNomePdfAppuntoForm(request.POST)
        if form.is_valid():
            # salviamo il documento nel database che contiene dati sul documento
            data_ora_attuale = timezone.now()
            nuovo_pdf_appunto = form.cleaned_data['pdf_appunto']
            nuovo_nome_appunto = form.cleaned_data['nome_appunto']          # recuperiamo nella database gli appunti di cui dobbiamo modificare il nome
            appunto = Appunto.objects.get(id=appunto_id)
            appunto.pdf_appunto = nuovo_pdf_appunto
            appunto.nome_appunto = nuovo_nome_appunto
            appunto.save()
            return redirect('materia-detail', materia_id) # ridirezione dgli appunti per la materia corrente
        else:
            return redirect('pagina_di_incuccesso_caricamento') # ridirezione alla pagina di insuccesso
    else:
        appunto = Appunto.objects.get(id=appunto_id)
        form = ModificaNomePdfAppuntoForm(request.POST)
        context = {'form': form, 'appunto': appunto}
        return render(request, 'appunti/update_appunto_element.html', context)




def appunto_detail(request, materia_id,appunto_id):
    appunto = Appunto.objects.get(id=appunto_id)
    materia = Materia.objects.get(id=materia_id)
    recenzioni= Recenzione.objects.filter(appunto_recenzionato = appunto_id)


    url_materia_curr = 'materie/{0}/'.format(materia_id)
    materia_elemento = {"nome": materia.nome, 'url': url_materia_curr}
    percorso = [{"nome": "Materie Disponibile", 'url': "materie/"}, ]
    percorso.append(materia_elemento)
    url_appunto_curr = url_materia_curr + '/{0}/'.format(appunto.id)
    appunto_elemento = {"nome": appunto.nome_appunto, "url": url_appunto_curr}
    percorso.append(appunto_elemento)
    context = {'appunto': appunto, 'recenzioni': recenzioni, 'materia_id': materia_id, "percorso": percorso}
    return render(request, 'appunti/appunto_detail.html', context)

def appunto_detail_download(request,materia_id, appunto_id):
    appunto = get_object_or_404(Appunto, id=appunto_id) # per recuperare l'appunto di cui so l'id
    num_scaricamento = appunto.Num_scaricamento;
    num_scaricamento += 1
    file_path = appunto.pdf_appunto.path # recupero il camino del doc pdf dell'appunto
    response = FileResponse(open(file_path, 'rb')) # apro il file pdf il modalita lettura binaria
    appunto.Num_scaricamento = num_scaricamento
    appunto.save() # per apportare le modifiche abbiamo fatto uno scaricamento
    return response





""" view che ritorna la pagina per recensire un appunto"""
def appunto_detail_recenzionare(request,materia_id, appunto_id):
    return HttpResponse('<h2>Recensire l''appunto<h2>')


def appunto_detail_votare(request):
    return HttpResponse('Votare appunto')