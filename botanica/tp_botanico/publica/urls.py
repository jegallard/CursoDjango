from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('productos', views.productos, name='productos'),
    path('club', views.club, name='club'),
]
