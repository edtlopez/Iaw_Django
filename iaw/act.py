#! /usr/bin/python
# -*- coding: utf8 -*-

import feedparser
from buscador.models import Articulo, Periodico, Categoria
from datetime import *
import time


		
RSS = {'elmundo' : 'http://estaticos.elmundo.es/elmundo/rss/portada.xml',
'elpais' : 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
'abc' : 'http://www.abc.es/rss/feeds/abcPortada.xml'


}

		
def periodicos_act(RSS) :
	for peri in RSS :
		db_periodicos = Periodico.objects.filter(nombre=peri).values('nombre')
		if len(db_periodicos) < 1 :
			insert = Periodico(nombre=peri,url=RSS[peri])
			insert.save()
			print ("Entrada Periodicos Añadida")
	
def act (url):
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
		
		aid.visitas=0
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

for p in Periodico.objects.all().values('url'):
	act(p['url'])
	

