from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from .models import Fecha, Portada
from .forms import search_noticia


class IndexView(generic.ListView):
	template_name = 'buscador/base.html'

	def Buscador(self):
		 template = loader.get_template('buscador/formulario.html')
		 return HttpResponse(template.render())

	def search(request):
		form = search_noticia.buscar_noticias(año,mes,dia)
		
		
		return render(request, 'buscador/search_resultados.html', {'form': form})
