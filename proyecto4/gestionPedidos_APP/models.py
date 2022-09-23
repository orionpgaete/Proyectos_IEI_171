from django.db import models

# Create your models here.
# Crear 3 tablas Clientes, Productos, Pedidos

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)



# python manage.py makemigrations (migra BBDD)

#python manage.py sqlmigrate gestionPedidos_APP 0001

#python manage.py migrate (crea tablas en DB)