from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from buscador.models import Portada
from buscador.forms import search_noticia
import datetime


class IndexView(generic.ListView):

	def Buscador(request):
		if request.method == "POST":
			form = search_noticia(request.POST)
			if form.is_valid():
				Año = request.POST["Año"]
				Mes = request.POST["Mes"]
				Dia = request.POST["Dia"]
				
				
			return 	render('buscador/resultado.html')
		else:
			form = search_noticia()
		return render(request, 'buscador/formulario.html', {'form': form})

