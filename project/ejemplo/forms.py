#----------------------------Clase 20--------------------------
from django import forms

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

#----------------------------Clase 21--------------------------
from ejemplo.models import Familiar

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']