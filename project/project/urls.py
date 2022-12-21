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
from ejemplo.views import index, monstrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar
#-----------------------Clase 23-------------------------
#from ejemplo_dos.views import index, PostList, PostCrear, PostBorrar, PostActualizar
#-----------------------Clase 24-------------------------
from ejemplo_dos.views import (index, PostDetalle, PostList, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout )
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    #-----------------------Clase 18-------------------------
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
    #-----------------------Clase 19-------------------------
    path('mi-familia/', monstrar_familiares), # nueva vista
    #-----------------------Clase 20-------------------------
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    #-----------------------Clase 21-------------------------
    path('mi-familia/alta', AltaFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    #-----------------------Clase 21 Parte1-------------------------
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    #-----------------------Clase 22-------------------------
    path('panel-familia/', FamiliarList.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/crear', FamiliarCrear.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/borrar', FamiliarBorrar.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/actualizar', FamiliarActualizar.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    #-----------------------Clase 23-------------------------
    path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    path('ejemplo-dos/listar/', PostList.as_view(), name="ejemplo-dos-listar"),
    #path('ejemplo-dos/crear/', PostCrear.as_view(), name="ejemplo-dos-crear"),
    # Despues de clase 23
    #path('ejemplo-dos/<int:pk>/borrar/', PostBorrar.as_view(), name="ejemplo-dos-borrar"),
    #path('ejemplo-dos/<int:pk>/actualizar/', PostActualizar.as_view(), name="ejemplo-dos-actualizar"),
    #-----------------------Clase 24-------------------------
    path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('ejemplo-dos/crear/', staff_member_required(PostCrear.as_view()), name="ejemplo-dos-crear"),
    path('ejemplo-dos/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="ejemplo-dos-borrar"),
    path('ejemplo-dos/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="ejemplo-dos-actualizar"),
    path('ejemplo-dos/signup/', UserSignUp.as_view(), name ="ejemplo-dos-signup"),
    path('ejemplo-dos/login/', UserLogin.as_view(), name= "ejemplo-dos-login"),
    path('ejemplo-dos/logout/', UserLogout.as_view(), name="ejemplo-dos-logout"),
]
