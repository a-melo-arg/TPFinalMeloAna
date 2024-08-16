from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from Users.forms import UserRegisterForm, UserEditForm
from django.urls import reverse_lazy


def inicio(request):
    return render(request, "BlogLibros/inicio.html")

# funcion para iniciar sesion
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "BlogLibros/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "BlogLibros/inicio.html", {"mensaje":"Datos incorrectos"})
            
        else:
            return render(request, "BlogLibros/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Users/login.html", {"form": form})

# funcion para registrar un nuevo usuario
def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            return render(request,"BlogLibros/inicio.html" , {"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()     

    return render(request,"Users/registro.html" , {"form":form})

#funcion para editar el perfil, necesito estar logeado para acceder aca
@login_required
def editarperfil(request):
    usuario = request.user
    if request.method == "POST":
        mi_form = UserEditForm(request.POST, request.FILES, instance=usuario)
        
        if mi_form.is_valid():
            if mi_form.cleaned_data.get('imagen'):
                usuario.avatar.imagen = mi_form.cleaned_data.get('imagen')
                usuario.avatar.save()
            mi_form.save()
            return render(request, "BlogLibros/inicio.html")
    else: 
        mi_form = UserEditForm(instance=request.user)
        
    return render(request, "Users/editarperfil.html", {"mi_form":mi_form})


class CambiarContrasenia(PasswordChangeView):
    template_name = "Users/cambiarcontrasenia.html"
    success_url = reverse_lazy('EditarPerfil')
    