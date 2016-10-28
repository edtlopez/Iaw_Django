from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,loader
from buscador.models import Portada, Fecha


def buscador_index(request):
	template = loader.get_template('buscador/index.html')
	return HttpResponse(template.render(request))



def buscador_noticias(request,año,mes,dia):
	template = loader.get_template('buscador/resultados.html')
	return HttpResponse(template.render(request))
