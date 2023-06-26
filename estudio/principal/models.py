from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Galeria(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='principal/img')
    valor = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.nombre
