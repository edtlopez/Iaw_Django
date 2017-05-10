from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render

#@login_required(login_url='/login/')
class Articulolist(ListView):
	model = Articulo
	template_name = "principal.html"


class ArticleDetailView(DetailView):
	model = Articulo
	template_name="article_detail.html"
	slug_url_kwarg = "id"
	slug_field = 'id'
	