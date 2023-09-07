from django import  forms
from .models import Appunto

class CaricamentoAppuntoForm(forms.ModelForm):
    class Meta:
        model = Appunto
        fields = ['nome_appunto', 'pdf_appunto']
