from django import forms
from django.forms import ValidationError

class contacto_form(forms.Form):
    nombre = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class': 'contacto-campo', 'placeholder': 'ingrese su nombre'}))
    mail = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'contacto-campo','placeholder': 'ingrese su email'}))
    mensaje = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'contacto-campo contacto-area', 'placeholder': 'ingrese un mensaje', "rows": "5"}))

