"""
Autor: Luis Ramos (@luisAngelDev)
GitHub: https://github.com/luisAngelDev
Descripción: Definición del modelo Servicio utilizado para la pagina web personal.
"""
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=100, help_text="Ej: bi bi-code, fa fa-paint-brush (Bootstrap o FontAwesome)")

    def __str__(self):
        return self.titulo
