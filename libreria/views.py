from msilib.schema import ListView
from django.shortcuts import render
from django.http import HttpResponse

from .models import Libro
from django.views.generic import ListView

# Create your views here.
#Acceso del sitio
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

#Acceso a los libros
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    return render(request, 'libros/crear.html')

def editar(request):
    return render(request, 'libros/editar.html')

# class indexLibreria(ListView):
#     template_name = 'libros/index.html'
#     context_object_name = 'listar_libro'
    
#     def get_queryset(self):
#         return Libro.objects.all()
