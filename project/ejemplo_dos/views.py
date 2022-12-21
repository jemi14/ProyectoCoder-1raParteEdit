from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView #Antes TemplateView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy

# Clase 24
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from ejemplo_dos.forms import UsuarioForm

# Clase 23
def index(request):
    return render(request, "ejemplo_dos/index.html", {})

# Clase 24
from django.views.generic import DetailView

class PostDetalle(DetailView):
    model = Post

# Clase 23
class PostList(ListView): #TemplateView antes
    model = Post 
    #template_name = "ejemplo_dos/post_list.html", ya no hace falta

#Clase 24
class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = '__all__'

#Clase 24
class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")

#Clase 24
class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('ejemplo-dos-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('ejemplo-dos-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('ejemplo-dos-listar')
