from django.db import models

# Create your models here.
class Perfume(models.Model):
  nombre = models.CharField(max_length=100)
  marca = models.CharField(max_length=100)
  descripcion = models.TextField(blank=True)
  precio = models.DecimalField(max_digits=8, decimal_places=2)
  stock = models.PositiveIntegerField(default=0)
  tamano_ml = models.PositiveIntegerField(default=100)
  anio_lanzamiento = models.PositiveIntegerField(
    null=True, 
    blank=True,
    help_text='Ingrese solo el año de lanzamiento (ej: 2020)'
  )

  def __str__(self):
    return f'{self.nombre} - {self.marca} ({self.tamano_ml}ml)'