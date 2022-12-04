"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import index, monstrar_familiares, BuscarFamiliar, AltaFamiliar

urlpatterns = [
    path('admin/', admin.site.urls),
    #-----------------------Clase 18-------------------------
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
    #-----------------------Clase 19-------------------------
    path('mi-familia/', monstrar_familiares), # nueva vista
    #-----------------------Clase 20-------------------------
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    #-----------------------Clase 21-------------------------
    path('mi-familia/alta', AltaFamiliar.as_view()) # NUEVA RUTA PARA BUSCAR FAMILIAR
]