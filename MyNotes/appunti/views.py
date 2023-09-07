from django.shortcuts import render
from appunti.models import *
from django.http import FileResponse
from django.shortcuts import   get_object_or_404

from django.shortcuts import redirect  # ajoutez cet import

from django.http import  HttpResponse
# Create your views here.

""" la views che ritorna la home page"""
def home(request):
    return render(request, 'appunti/home.html')

""" la views che ritorna la lista delle materie"""
def materie_list(request):
    materie = Materia.objects.all()
    context = {"materie": materie}
    return render(request, 'appunti/materie_list.html', context)

""" la via che ritorna una singola materia con la lista degli appunti essa associata"""
def materia_detail(request, materia_id):
    materia = Materia.objects.get(id=materia_id)
    appunti_materia_curr = Appunto.objects.filter(materia_id = materia)
    context = {"materia": materia, "appunti_materia_curr": appunti_materia_curr}
    return render(request, 'appunti/materia_detail.html', context)


def upload_appunto(request, materia_id):
    return HttpResponse('<h1> Pagina di upload dell appunto <h2>')

def appunto_detail(request, materia_id,appunto_id):
    appunto = Appunto.objects.get(id=appunto_id)
    recenzioni= Recenzione.objects.filter(appunto_recenzionato = appunto_id)
    context = {'appunto': appunto, 'recenzioni': recenzioni, 'materia_id': materia_id}
    return render(request, 'appunti/appunto_detail.html', context)

def appunto_detail_download(request,materia_id, appunto_id):
    appunto = get_object_or_404(Appunto, id=appunto_id) # per recuperare l'appunto di cui so l'id
    file_path = appunto.pdf_appunto.path # recupero il camino del doc pdf dell'appunto
    response = FileResponse(open(file_path, 'rb')) # apro il file pdf il modelita lettura binaria
    return response

def appunto_detail_recenzionare(request,materia_id, appunto_id):

    return HttpResponse('<h1> Pagina di recenzione <h1>')


def appunto_detail_votare(request):
    return HttpResponse('Votare appunto')