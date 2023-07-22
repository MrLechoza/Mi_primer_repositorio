from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libro = Libro.objects.all()
    paginator = Paginator(Libro.objects.all(), 5)
    pagina = request.GET.get("page", 1)
    posts = paginator.get_page(pagina)
    current_page = int(pagina)
    paginas = range(1, posts.paginator.num_pages + 1)
    return render(request, 'paginas/libros/index.html', {'posts': posts, 'paginas': paginas, 'current_page': current_page})

def crear_libro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'paginas/libros/crear.html', {'formulario': formulario})

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'paginas/libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')