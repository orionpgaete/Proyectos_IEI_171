from pyexpat import model
from django.db import models

# Create your models here.
# Crear 3 tablas Clientes, Productos, Pedidos

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

# python manage.py makemigrations (migra BBDD)

#python manage.py sqlmigrate gestionPedidos_APP 0001

#python manage.py migrate (crea tablas en DB)

#python manage.py shell (inica consola)

# from gestionPedidos_APP.models import Productos
# pro = Productos(nombre = 'mesa', categoria='Muebles', precio = 5000)
# pro.save()
# pro = Productos.objects.get(id=2)  (traer producto)
# pro.precio=700 (modifica producto)
# pro = Productos.objects.get(id=3)  (trae producto)
# pro.delete()
# pro = Productos.objects.create(nombre = 'Sillon', categoria='Muebles', precio = 15000)