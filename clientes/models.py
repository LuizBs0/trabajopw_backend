from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.usuario

class Categoria_Res(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Restaurante(models.Model):
    nombre = models.CharField(max_length=25)
    categoria = models.ForeignKey(Categoria_Res, on_delete=models.CASCADE)
    horario = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria_Pla(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=25)
    categoria = models.ForeignKey(Categoria_Pla, on_delete=models.CASCADE)
    restaurante_id = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre