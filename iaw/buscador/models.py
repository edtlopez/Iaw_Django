from django.db import models
# Create your models here.

class Categoria (models.Model):
	nombre = models.CharField(max_length=50)

class Periodico (models.Model):
	nombre = models.CharField(max_length=50)

class Articulo (models.Model):
	titulo = models.CharField(max_length=50)
	url =  models.URLField(max_length=200)
	descripcion = models.URLField()
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	visitas = models.PositiveIntegerField()
	periodico = models.ForeignKey(Periodico)
	categoria = models.ManyToManyField(Categoria)
	author = models.CharField(max_length=50)





















