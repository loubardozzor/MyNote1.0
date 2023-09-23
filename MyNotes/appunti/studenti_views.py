from django.shortcuts import render
from appunti.models import *
from django.http import FileResponse
from .forms import *
from django.shortcuts import   get_object_or_404
from django.utils import timezone
from datetime import datetime
from django.shortcuts import redirect  # ajoutez cet import
from django.http import  HttpResponse



def  studenti_list(request):
    studenti = Studente.objects.all()
    context = {'studenti': studenti}
    return render(request, "appunti/studenti_list.html", context)

def studente_detail(request, studente_id):
    appunti_studente = Appunto.objects.filter(studente_id = studente_id)
    context = {'appunti_studenti': appunti_studente}
    return  render(request, "appunti/studente_detail.html", context)

