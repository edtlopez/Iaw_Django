from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from buscador.models import Portada
from buscador.forms import search_noticia


class IndexView(generic.ListView):

	def Buscador(request):
		if request.method == "POST":
			form = search_noticia(request.POST)
			print (request.POST)
			return redirect(Resultado_Busqueda(Año,Mes,Dia))	
		else:
			form = search_noticia()
		return render(request, 'buscador/formulario.html', {'form': form})

	def Resultado_Busqueda(request):		
		return render(request, 'buscador/resultado.html')
