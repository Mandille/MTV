from django.db import models

class familiar(models.model):
    nombre= models.CharField(max_lenght=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    nacimiento= models.DateField()