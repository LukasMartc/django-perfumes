from django import forms
from django.core import validators
import datetime
from .models import Perfume

class PerfumeForm(forms.ModelForm):
  class Meta:
    model = Perfume
    fields = ['nombre', 'marca', 'descripcion', 'precio', 'stock', 'tamano_ml', 'anio_lanzamiento']
    widgets = {
      'nombre': forms.TextInput(attrs={'class': 'form-control'}),
      'marca': forms.TextInput(attrs={'class': 'form-control'}),
      'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
      'precio': forms.NumberInput(attrs={'class': 'form-control'}),
      'stock': forms.NumberInput(attrs={'class': 'form-control'}),
      'tamano_ml': forms.NumberInput(attrs={'class': 'form-control'}),
      'anio_lanzamiento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 2020'}),
    }

  nombre = forms.CharField(
    min_length=3,
    max_length=50,
    validators=[
      validators.MinLengthValidator(3),
      validators.MaxLengthValidator(50)
    ],
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )

  def clean_nombre(self):
    inputNombre = self.cleaned_data['nombre']
    if any(char.isdigit() for char in inputNombre):
      raise forms.ValidationError('El nombre del perfume no debe contener números')
    return inputNombre
  
  def clean_tamano_ml(self):
    tamano = self.cleaned_data['tamano_ml']
    if tamano <= 0:
        raise forms.ValidationError('El tamaño debe ser mayor a 0 ml')
    return tamano
  
  def clean_anio_lanzamiento(self):
    anio = self.cleaned_data.get('anio_lanzamiento')
    if anio:
      current_year = datetime.date.today().year
      if anio < 1900 or anio > current_year:
        raise forms.ValidationError(f'Ingrese un año válido entre 1900 y {current_year}')
    return anio
    