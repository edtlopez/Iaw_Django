from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic.edit import UpdateView
from .forms import *
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class Articulolist(ListView):
	model = Articulo
	template_name = "principal.html"


class ArticleDetailView(DetailView):
	model = Articulo
	template_name="article_detail.html"
	slug_url_kwarg = "id"
	slug_field = 'id'


class AuthorUpdate(UpdateView):
	model = Articulo
	from_class = articulo_update_form
	template_name="articulo_update_form.html"
	fields = ['titulo','url','descripcion','author']	
	slug_url_kwarg = "id"
	slug_field = 'id'
	success_url = reverse_lazy('home')



class ArticuloDelete (DeleteView):
	model = Articulo
	success_url = reverse_lazy('home')
	template_name="articulo_del.html"
	success_url = reverse_lazy('home')
	slug_url_kwarg = "id"
	slug_field = 'id'

