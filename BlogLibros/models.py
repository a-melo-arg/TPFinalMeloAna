from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=40)
    genero = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Título: {self.titulo}"
        
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
        
    def __str__(self):
        return f"Apellido: {self.apellido}, Nombre: {self.nombre}"
    
class Lectores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
