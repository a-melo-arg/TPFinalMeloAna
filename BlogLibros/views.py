from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro, Autor, Lectores
# from .forms import LibroFormulario, BusquedaFormulario, AutorFormulario, LectorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 

def inicio(request):
    return render(request, "BlogLibros/inicio.html")

# vistas basadas en funciones
""" def cargar_libro(request):
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST) # Aqui me llega la informacion del html
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            libro = Libro(titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"])
            libro.save()
            return render(request, "BlogLibros/inicio.html")  # vuelvo a inicio
    else:
        miFormulario = LibroFormulario()  # formulario vacio para construir el html
    return render(request, "BlogLibros/cargarlibro.html", {"miFormulario": miFormulario}) """

def busquedaLibro(request):
    return render(request, "BlogLibros/buscarlibro.html")

def buscar_libro(request):   #busca en la BD
    if request.GET ["librobuscado"]:
        librobusco = request.GET ["librobuscado"]
        libros = Libro.objects.filter(titulo__icontains=librobusco)
            
        return render(request, "BlogLibros/mostrarlibros.html", {"titulo":librobusco, "libros":libros})  
    else:
        respuesta = "ERROR, por favor ingrese el nombre del libro"
        return HttpResponse(respuesta)


""" def cargar_autor(request):
    if request.method == "POST":
        miFormulario = AutorFormulario(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            autor = Autor(nombre=informacion["nombre"], apellido=informacion["apellido"],)
            autor.save()
            return render(request, "BlogLibros/inicio.html")  
    else:
        miFormulario = AutorFormulario()  
    return render(request, "BlogLibros/cargarautor.html", {"miFormulario": miFormulario}) """

""" def cargar_lector(request):
    if request.method == "POST":
        miFormulario = LectorFormulario(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            lector = Lectores(nombre=informacion["nombre"], apellido=informacion["apellido"], pais=informacion["pais"])
            lector.save()
            return render(request, "BlogLibros/inicio.html")  
    else:
        miFormulario = LectorFormulario()  
    return render(request, "BlogLibros/cargarlector.html", {"miFormulario": miFormulario})
 """

# vistas basadas en clases - LIBROS
class LibroListView(ListView):
    model = Libro 
    context_object_name = "libros"
    template_name = "BlogLibros/libro_lista.html"
    
class LibroDetailView(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = "BlogLibros/libro_detalle.html"
    
class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = "BlogLibros/libro_crear.html"
    success_url = reverse_lazy('ListaLibros')
    fields = ['titulo', 'autor', 'genero']
    
class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "BlogLibros/libro_editar.html"
    success_url = reverse_lazy('ListaLibros')
    fields = ['titulo', 'autor', 'genero']
    
class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "BlogLibros/libro_borrar.html"
    success_url = reverse_lazy('ListaLibros')
    

# vistas basadas en clases - AUTORES
class AutorListView(LoginRequiredMixin, ListView):
    model = Autor 
    context_object_name = "autores"
    template_name = "BlogLibros/autor_lista.html"
    
class AutorDetailView(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "BlogLibros/autor_detalle.html"
    
class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    template_name = "BlogLibros/autor_crear.html"
    success_url = reverse_lazy('ListaAutor')
    fields = ['nombre', 'apellido']
    
class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    template_name = "BlogLibros/autor_editar.html"
    success_url = reverse_lazy('ListaAutor')
    fields = ['nombre', 'apellido']
    
class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = "BlogLibros/autor_borrar.html"
    success_url = reverse_lazy('ListaAutor')
    
    
# vistas basadas en clases - LECTORES
class LectorListView(LoginRequiredMixin, ListView):
    model = Lectores 
    context_object_name = "lectores"
    template_name = "BlogLibros/lector_lista.html"
    
class LectorDetailView(LoginRequiredMixin, DetailView):
    model = Lectores
    template_name = "BlogLibros/lector_detalle.html"
    
class LectorCreateView(LoginRequiredMixin, CreateView):
    model = Lectores
    template_name = "BlogLibros/lector_crear.html"
    success_url = reverse_lazy('ListaLector')
    fields = ['nombre', 'apellido', 'pais']
    
class LectorUpdateView(LoginRequiredMixin, UpdateView):
    model = Lectores
    template_name = "BlogLibros/lector_editar.html"
    success_url = reverse_lazy('ListaLector')
    fields = ['nombre', 'apellido', 'pais']
    
class LectorDeleteView(LoginRequiredMixin, DeleteView):
    model = Lectores
    template_name = "BlogLibros/lector_borrar.html"
    success_url = reverse_lazy('ListaLector')
    
def about(request):
    return render(request, "BlogLibros/about.html")