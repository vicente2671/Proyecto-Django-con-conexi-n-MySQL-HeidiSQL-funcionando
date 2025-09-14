from django.db import models

# Modelo de empleados
class Employee(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
