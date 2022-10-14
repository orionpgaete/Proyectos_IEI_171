from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    fono = models.CharField(max_length=15)