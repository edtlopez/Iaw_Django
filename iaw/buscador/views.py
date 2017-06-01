from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .forms import *
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

class Articulolist(ListView):
	model = Articulo
	template_name = "principal.html"

class ArticuloDelete (DeleteView):
	model = Articulo
	template_name="articulo_del.html"
	success_url = reverse_lazy('home')

class AuthorUpdate(UpdateView):
	model = Articulo
	from_class = articulo_update_form
	template_name="articulo_update_form.html"
	fields = ['titulo','url','descripcion','author']	
	success_url = reverse_lazy('home')

class ArticleDetailView(DetailView):
	model = Articulo
	template_name="article_detail.html"