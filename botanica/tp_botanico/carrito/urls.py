from . import views
from django.urls import path

urlpatterns = [
    path('tienda', views.tienda, name='tienda'),
]
