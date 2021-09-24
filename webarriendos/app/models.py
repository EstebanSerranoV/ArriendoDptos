from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100, default=None)
    precio = models.IntegerField(default="")
    descripcion = models.TextField(default="")
    nuevo = models.BooleanField(default="")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, default="")
    fecha_fabricacion = models.DateField(default="")
    imagen = models.ImageField(upload_to="Productos", null=True, default="")
    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "consulta"],
     [1, "reclamo"],
      [2, "sugerencia"],
       [3, "felicitaciones"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=30, default=None)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensajes = models.TextField(max_length=500, default=None)
    avisos = models.BooleanField(default=None)

    def __str__(self):
        return self.nombre
