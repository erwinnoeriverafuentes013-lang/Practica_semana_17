from django import forms
from .models import Categoria, Marca, Instrumento


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion", "activa"]


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["nombre", "pais_origen", "sitio_web"]


class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ["modelo", "categoria", "marca", "precio", "stock"]