from django.db import models


# Create your models here.
class Catalogpokemon(models.Model):
    generacion = models.CharField(max_length=30)
    cantidad = models.IntegerField(default=0)
