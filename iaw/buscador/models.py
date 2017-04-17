from django.db import models
#import uuid
#from cassandra.cqlengine import columns
#from django_cassandra_engine.models import DjangoCassandraModel

# Create your models here.

class Categoria (models.Model):
	nombre = models.CharField(max_length=50)

class Periodico (models.Model):
	nombre = models.CharField(max_length=50)
	url =  models.URLField(max_length=200)

class Articulo (models.Model):
	titulo = models.CharField(max_length=50)
	url =  models.URLField(max_length=200)
	descripcion = models.URLField()
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	visitas = models.PositiveIntegerField()
	periodico = models.ForeignKey(Periodico)
	categoria = models.ManyToManyField(Categoria)
	author = models.CharField(max_length=50)


#class ExampleModel(DjangoCassandraModel):
#    example_id    = columns.UUID(primary_key=True, default=uuid.uuid4)
#    example_type  = columns.Integer(index=True)
#    created_at    = columns.DateTime()
#    description   = columns.Text(required=False)
