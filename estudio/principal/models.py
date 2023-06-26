from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Galeria(models.Model):
    imagen = models.ImageField(upload_to='principal/img')
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.get_nombre_completo()


    def get_nombre_completo(self):
        return self.nombre

    def get_autor_personalizado(self):
        return self.autor