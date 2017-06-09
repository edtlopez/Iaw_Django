#! /usr/bin/python
# -*- coding: utf8 -*-

import feedparser
from datetime import *
import time
from django.core.management.base import BaseCommand, CommandError
import sys
from buscador.models import *

class Command (BaseCommand):
	def handle (self, *args, **options):
		for p in Periodico.objects.all().values('url'):
			url = p['url']
			articulos = feedparser.parse(url)
			for articulo in articulos['items']:		
				try:
					aid = Articulo.objects.get(url=articulo['id'])
				except : 
					aid = Articulo(url = articulo['id'])		
				
				if not 'published_parsed' in articulo.keys():	
					fecha = datetime.fromtimestamp(time.mktime(articulo['published_parsed']))
				else:
					fecha = datetime.fromtimestamp(time.mktime(time.localtime()))	
				categorias=[]
				if 'tags' in articulo.keys() :
					for tags in articulo['tags']:
						try:
							a = Categoria(nombre=tags['term'])
							a.save()
						except:
							a = Categoria.objects.get(nombre=tags['term'])
						categorias.append(a)
				
				aid.titulo = articulo['title']
				aid.descripcion = articulo['summary']
				aid.author = articulo['author']
				aid.fecha = fecha
				aid.periodico_id = Periodico.objects.filter(url=url).values('id')[0]['id']
				aid.save()
					
				if 'tags' in articulo.keys() :
					try:
						aid.categoria.set(categorias)
					except:
						pass
					print ('OK')


	def Periodicosact () :
		pass
