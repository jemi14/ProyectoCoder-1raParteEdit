from django.shortcuts import render

#-----------------------Clase 18-------------------------
def index(request):
    return render(request, "ejemplo/saludar.html")

#-----------------------Clase 19-------------------------
from ejemplo.models import Familiar

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})