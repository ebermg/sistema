from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Libro
from .forms import LibroForm

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

#éste está mal 
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html')

#este tambien esta mal :(
def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST: #otra forma de usar el post es ---->  request.method == 'POST'
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

# class indexLibreria(ListView):
#     template_name = 'libros/index.html'
#     context_object_name = 'listar_libro'
    
#     def get_queryset(self):
#         return Libro.objects.all()
