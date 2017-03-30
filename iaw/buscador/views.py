from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from buscador.models import Articulo, Periodico
from buscador.forms import busqueda_avanzada
import datetime

def search (busqueda):
	salida = {}
	for Editorial in ("Elmundo","ABC"):
		a = Portada(fecha=busqueda ,editorial=Editorial)
		salida[Editorial]=a
	return salida	
	

class IndexView(generic.ListView):
	  def get_queryset(self):
		  pass
	

		
