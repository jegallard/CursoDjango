from django import forms
from .models import Planta, Categoria

class PlantaForm(forms.ModelForm):

    nombre=forms.CharField(
            label='Nombre', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    
    imagen = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
    )
    class Meta:
      model = Planta
      fields = ['nombre', 'descripcion', 'imagen']




