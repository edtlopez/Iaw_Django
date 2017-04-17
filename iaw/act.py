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
	
	
def articulos_act(url):
	articulos = feedparser.parse(url)
	for articulo in articulos['items']:
		if 'tags' in articulo.keys() :
			if articulo['published_parsed'] != None :
				fecha = datetime.fromtimestamp(time.mktime(articulo['published_parsed']))
			else:
				fecha = datetime.fromtimestamp(time.mktime(time.localtime()))
				if Articulo.objects.filter(url=articulo['id']).values('url').count() < 1 :
					categorias=[]
					for tags in articulo['tags']:
						a = Categoria(nombre=tags['term'])
						a.save()
						categorias.append(a)
					insert = Articulo (visitas=0, url = articulo['id'], titulo = articulo['title'],descripcion = articulo['summary'], author = articulo['author'], fecha=fecha)
					insert.periodico_id = Periodico.objects.filter(url=url).values('id')[0]['id']
					insert.save()
					insert.categoria.set(categorias)
					print (articulo['id'])
					print ('Articulo añadido')
				else :
					print (articulo['id'])
					print ('El articulo ya existe')
			
				


for P in Periodico.objects.values():
	articulos_act(P['url'])
	

