from django.contrib import admin
from .models import Perfume

# Register your models here.
@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'marca', 'tamano_ml', 'precio', 'stock', 'anio_lanzamiento')
  search_fields = ('nombre', 'marca')
  list_filter = ('marca', 'anio_lanzamiento')
  ordering = ('nombre',)