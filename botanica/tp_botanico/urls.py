from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('productos',views.productos, name='productos'),
    path('plantin' , views.plantin, name='plantin'),
    path('planton',  views.planton,name='planton'),
    path('nuevo',  views.nuevo,name='nuevo'),
#    path('plantas',  views.plantas_index,name='plantas'),
    #path('plantas/nuevo/', views.plantas_nuevo,name='plantas_nuevo'),
    #path('plantas/editar/<int:id_curso>', views.plantas_editar,name='plantas_editar'),


]
