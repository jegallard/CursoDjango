from django import forms
from django.core import validators
from django.forms import ValidationError

def nombre_valido(value):
    if not value:
        raise ValidationError("El campo 'Nombre' es obligatotio",code="Nombre incompleto")
    else:
        if len(value.split(" ")) > 1:
            list_nombres = value.split(" ")
            for nombre in list_nombres:
                if not nombre.isalpha():
                    raise ValidationError("No intriducir números ni caracteres especiales", code="Nombre no alfanumerico")                    
        else:
            raise ValidationError("Introducir nombre y apellido", code="Nombre incompleto")

class contacto_form(forms.Form):
    nombre = forms.CharField(
        max_length=50, 
        label="", 
        validators=(nombre_valido,),
        widget=forms.TextInput(attrs={'class': 'contacto-campo', 'placeholder': 'Nombre y apellido'})        
        )
    mail = forms.EmailField(
        label="", 
        widget=forms.EmailInput(attrs={'class': 'contacto-campo','placeholder': 'E-mail'})
        )
    asunto = forms.CharField(
        max_length=40, label="", 
        widget=forms.TextInput(attrs={'class': 'contacto-campo', 'placeholder': 'Asunto'})
        )
    mensaje = forms.CharField(
        label="", 
        widget=forms.Textarea(attrs={'class': 'contacto-campo contacto-area', 'placeholder': 'Ingrese su mensaje', "rows": "5"})
        )

