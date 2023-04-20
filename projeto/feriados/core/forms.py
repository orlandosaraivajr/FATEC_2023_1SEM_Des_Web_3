from django import forms


class FeriadoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    dia = forms.IntegerField()
    mes = forms.IntegerField()
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()
    

from core.models import FeriadoModel
from django.forms import ModelForm


class FeriadoModelForm(ModelForm):
    class Meta:
        model = FeriadoModel
        fields = ['nome', 'dia', 'mes']
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()
