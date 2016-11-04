from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from .models import Fecha, Portada


class IndexView(generic.ListView):
	template_name = 'buscador/base.html'

	def get_queryset(self):
		 template = loader.get_template('buscador/base.html')
		 return HttpResponse(template.render())
