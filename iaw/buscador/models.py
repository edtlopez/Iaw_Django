from django.db import models

# Create your models here.

class Fecha (models.Model):
	fecha = models.DateTimeField()
	num_busquedas = models.IntegerField()

class Portada (models.Model):
	ponom = models.CharField(max_length=50)
	editorial = models.CharField(max_length=50)
	ref = models.CharField(max_length=60)
	url = models.CharField(max_length=50)
	fk_fecha = models.ForeignKey(Fecha,on_delete=models.CASCADE)
	

