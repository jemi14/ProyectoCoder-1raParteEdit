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

#-----------------------Clase 21-------------------------
from ejemplo.forms import FamiliarForm #<--- NUEVO IMPORT

class AltaFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}" #Acomoda la info que te llega como un diccionario
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

#-----------------------Clase 21 parte 1-------------------------
from django.shortcuts import get_object_or_404 # <----- Nuevo import

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actulizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 'familiar': familiar,'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

#-----------------------Clase 22 -------------------------
from django.views.generic import ListView # <----- NUEVO IMPORT

class FamiliarList(ListView):
  model = Familiar

from django.views.generic import CreateView # <----- NUEVO IMPORT

class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]

from django.views.generic import DeleteView # <----- NUEVO IMPORT

class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"

from django.views.generic import UpdateView # <----- NUEVO IMPORT

class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]


