from django.db import models


# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField(default=0)
    pais = models.CharField(max_length=25, default='')
    dni = models.CharField(max_length=8, default='00000000')
    vigente = models.BooleanField(default=True)

    def __str__(self):
        return "{} de {}".format(self.nombre, self.pais)
