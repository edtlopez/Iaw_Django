from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import admin


#import uuid
#from cassandra.cqlengine import columns
#from django_cassandra_engine.models import DjangoCassandraModel

# Create your models here.
#@admin.register(Categoria)
class Categoria (models.Model):
	nombre = models.CharField(max_length=50,unique=True)

#@admin.register(Periodico)
class Periodico (models.Model):
	nombre = models.CharField(max_length=50)
	url =  models.URLField(max_length=200)

#@admin.register(Articulo)
class Articulo (models.Model):
	titulo = models.CharField(max_length=100)
	url =  models.URLField(max_length=200,unique=True)
	descripcion = models.CharField(max_length=1000)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	periodico = models.ForeignKey(Periodico)
	categoria = models.ManyToManyField(Categoria)
	author = models.CharField(max_length=100)

class userextension (models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fecha_nacimiento = models.DateTimeField(auto_now_add=True, blank=True)
	pregunta_secreta =  models.CharField(max_length=100)
	respueste_secreta =  models.CharField(max_length=100)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class ArticuloAdmin(admin.ModelAdmin):
    pass

@admin.register(Periodico)
class ArticuloAdmin(admin.ModelAdmin):
    pass

#class Comentario (DjangoCassandraModel):
#	id = columns.UUID(primary_key=True, default=uuid.uuid4)
#	usuario_id = 
#	articulo_id =
#	comentario =
	

#class ExampleModel(DjangoCassandraModel):
#    example_id    = columns.UUID(primary_key=True, default=uuid.uuid4)
#    example_type  = columns.Integer(index=True)
#    created_at    = columns.DateTime()
#    description   = columns.Text(required=False)
