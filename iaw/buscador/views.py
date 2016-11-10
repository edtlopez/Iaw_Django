from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from buscador.models import Fecha, Portada
from buscador.forms import search_noticia


class IndexView(generic.ListView):

	def Buscador(request):
		if request.method == "POST":
			form = search_noticia(request.POST)
			if form.is_valid():
				Año = form.cleaned_data['año']
				Mes = form.cleaned_data['mes']
				Dia = form.cleaned_data['dia']
				return HttpResponseRedirect('/resultado/')	
		else:
			form = search_noticia()
		return render(request, 'buscador/formulario.html', {'form': form})

	def Resultado_Busqueda(request):
		
		return render(request, 'buscador/resultado.html', {'form': form})
