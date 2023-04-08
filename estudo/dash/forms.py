from django import forms
from .models import Matéria, Assunto

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Matéria
        fields = ['nome', 'descrição']

class AssuntoForm(forms.ModelForm):
    class Meta:
        model = Assunto
        fields = ['nome', 'descrição', 'matéria']
