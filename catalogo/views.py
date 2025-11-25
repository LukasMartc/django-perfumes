from django.shortcuts import render, redirect
from .models import Perfume
from .forms import PerfumeForm

# Create your views here.
def index(request):
  form = PerfumeForm()
  if request.method == 'POST':
    form = PerfumeForm(request.POST)
    if form.is_valid():
      print('Formulario OK')
      print('Nombre: ', form.cleaned_data['nombre'])
      form.save()
      return listar_perfumes(request)
  data = {'form': form}
  return render(request, 'catalogo/index.html', data)

def listar_perfumes(request):
  perfumes = Perfume.objects.all()
  data = {'perfumes': perfumes}
  return render(request, 'catalogo/perfumes.html', data)

def editar_perfume(request, id):
  perfume = Perfume.objects.get(id=id)
  form = PerfumeForm(instance=perfume)
  if request.method == 'POST':
    form = PerfumeForm(request.POST, instance=perfume)
    if form.is_valid():
      form.save()
      return listar_perfumes(request)
  data = {'form': form}
  return render(request, 'catalogo/index.html', data)

def eliminar_perfume(request, id):
  perfume = Perfume.objects.get(id=id)
  perfume.delete()
  return redirect('catalogo:perfumes')


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import PerfumeSerializer
from .models import Perfume

# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def api_perfumes(request):
  if request.method == 'GET':
    perfumes = Perfume.objects.all()
    serializer = PerfumeSerializer(perfumes, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = PerfumeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET', 'PUT', 'DELETE'])
def api_perfume_detalle(request, pk):
  try:
    perfume = Perfume.objects.get(pk=pk)
  except Perfume.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = PerfumeSerializer(perfume)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    serializer = PerfumeSerializer(perfume, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  if request.method == 'DELETE':
    perfume.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)