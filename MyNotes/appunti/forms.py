from django import  forms
from .models import Appunto
from .models import  Recenzione

class CaricamentoAppuntoForm(forms.ModelForm):
    class Meta:
        model = Appunto
        fields = ['nome_appunto', 'pdf_appunto']


class RecenzioneForm(forms.ModelForm):
    class Meta:
        model = Recenzione
        fields = ['testo_recenzione']

