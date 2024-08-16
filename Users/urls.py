from django.urls import path
from Users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [    
    path('', views.inicio),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='Users/logout.html'), name = 'Logout'),
    path('editarperfil', views.editarperfil, name = 'EditarPerfil'),
    path('cambiarcontrasenia', views.CambiarContrasenia.as_view(), name = 'CambiarContrasenia'),
]