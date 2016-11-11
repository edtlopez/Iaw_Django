from django.db import models
# Create your models here.


class Portada (models.Model):
	ponom = models.CharField(max_length=50)
	editorial = models.CharField(max_length=50)
	ref = models.CharField(max_length=60)
	url = models.CharField(max_length=50)
	fecha = models.DateTimeField()
	


