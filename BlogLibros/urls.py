from django.urls import path
from BlogLibros import views

urlpatterns = [    
    path('', views.inicio, name = "Inicio"),
    path('buscar_libro', views.buscar_libro),
    path('busquedaLibro', views.busquedaLibro, name = "BucarLibro"),
    path('about', views.about, name = "About"),            
]

# LIBROS
urlpatterns += [    
    path('libros/lista', views.LibroListView.as_view(), name = "ListaLibros"),
    path('libros/nuevo', views.LibroCreateView.as_view(), name = "NuevoLibro"),
    path('libros/<pk>', views.LibroDetailView.as_view(), name = "DetalleLibro"),
    path('libros/<pk>/editar', views.LibroUpdateView.as_view(), name = "EditarLibro"),
    path('libros/<pk>/borrar', views.LibroDeleteView.as_view(), name = "BorrarLibro"),        
]

# AUTORES
urlpatterns += [    
    path('autores/lista', views.AutorListView.as_view(), name = "ListaAutor"),
    path('autores/nuevo', views.AutorCreateView.as_view(), name = "NuevoAutor"),
    path('autores/<pk>', views.AutorDetailView.as_view(), name = "DetalleAutor"),
    path('autores/<pk>/editar', views.AutorUpdateView.as_view(), name = "EditarAutor"),
    path('autores/<pk>/borrar', views.AutorDeleteView.as_view(), name = "BorrarAutor"),        
]

# LECTORES
urlpatterns += [    
    path('lectores/lista', views.LectorListView.as_view(), name = "ListaLector"),
    path('lectores/nuevo', views.LectorCreateView.as_view(), name = "NuevoLector"),
    path('lectores/<pk>', views.LectorDetailView.as_view(), name = "DetalleLector"),
    path('lectores/<pk>/editar', views.LectorUpdateView.as_view(), name = "EditarLector"),
    path('lectores/<pk>/borrar', views.LectorDeleteView.as_view(), name = "BorrarLector"),        
]