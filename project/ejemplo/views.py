from django.shortcuts import render

#-----------------------Clase 18-------------------------
def index(request):
    return render(request, "ejemplo/saludar.html")

#-----------------------Clase 19-------------------------
from ejemplo.models import Familiar

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

#-----------------------Clase 20-------------------------
from ejemplo.forms import Buscar # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})