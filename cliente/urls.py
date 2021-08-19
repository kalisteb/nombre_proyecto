from django.urls import path, include
from . import views


# todas las rutas de la app
# '' me redirige el view  al metodo o funcion agregar
urlpatterns = [
    #path('/inicio', views.inicio),
    path('', views.inicio),
    path('inicio', views.inicio),
    path('agregar', views.agregar),
    path('leer', views.leer),
    path('actualizar', views.actualizar),
    path('eliminar', views.eliminar),
]