from django.shortcuts import render
from appunti.models import *
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


def upload_appunto(request):
    return HttpResponse('<h1> Pagina di upload dell appunto <h2>')

def appunto_detail(request):
    return HttpResponse('<h1> i detagli del appunto si puo votare, fare il download, vedere le recenzione e votare, vedere il voto dell appunto')

def appunto_detail_download(request):
    return HttpResponse('fare il download dell apppunto ')

def appunto_detail_recenzionare(request):
    return HttpResponse('Recenzionare  appunto')

def appunto_detail_votare(request):
    return HttpResponse('Votare appunto')