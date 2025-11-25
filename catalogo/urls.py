from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
  path('', views.index, name='agregar'),
  path('perfumes/', views.listar_perfumes, name='perfumes'),
  path('actualizarPerfume/<int:id>/', views.editar_perfume, name='editar'),
  path('eliminarPerfume/<int:id>/', views.eliminar_perfume, name='eliminar'),

  path('api/perfumes/', views.api_perfumes),
  path('api/perfumes/<int:pk>/', views.api_perfume_detalle)
]