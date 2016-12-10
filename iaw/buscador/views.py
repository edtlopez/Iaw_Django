from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from buscador.models import Portada
from buscador.forms import search_noticia_form
import datetime

def search (busqueda):
	salida = {}
	for Editorial in ("Elmundo","ABC"):
		a = Portada(fecha=busqueda ,editorial=Editorial)
		salida[Editorial]=a
	return salida	
	

class IndexView(generic.ListView):

	def Buscador(request):
		form = search_noticia_form()
		return render(request, 'buscador/formulario.html', {'form': form})

	def Resultado(request):
		if request.method == "POST":
			form = search_noticia_form(request.POST)
			if form.is_valid():
				Año = int(request.POST["Año"])
				Mes = int(request.POST["Mes"])
				Dia = int(request.POST["Dia"])
				date = datetime.datetime(Año,Mes,Dia,0,0,0,0)
				busqueda = search(date)			
			return 	render(request, 'buscador/resultado.html', busqueda)	
		else:
			form = search_noticia_form()
			return HttpResponseRedirect('/', {'form': form})		
				
		
		
