from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView #Antes TemplateView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy

# Clase 23

def index(request):
    return render(request, "ejemplo_dos/index.html", {})

class PostList(ListView): #TemplateView antes
    model = Post 
    #template_name = "ejemplo_dos/post_list.html", ya no hace falta

#class PostCrear(CreateView):
#    model = Post
#    success_url = "/ejemplo-dos/listar/" #Despues que creamos que nos lleve de nuevo a lista
#    fields = "__all__"

class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = '__all__'

#Fuera de clase

class PostBorrar(DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")

class PostActualizar(UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = "__all__"


