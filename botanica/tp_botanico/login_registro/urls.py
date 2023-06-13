from . import views
from django.urls import path
from .views import Registro
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.mi_login, name='login'),
    path('registro', Registro.as_view(), name='registro'), 
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),          
]
