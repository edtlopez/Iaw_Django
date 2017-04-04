#! /usr/bin/python
# -*- coding: utf8 -*-

import feedparser
from buscador.models import Articulo, Periodico, Categoria
from datetime import datetime
import time

RSS = {

    'elmundo' : 'http://estaticos.elmundo.es/elmundo/rss/portada.xml',
    'elpais' : 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
    'abc' : 'http://www.abc.es/rss/feeds/abcPortada.xml',

}


def categoria_act(RSS):
	for DIARIO in RSS :
		scraping = feedparser.parse(RSS[DIARIO])
		for NOTICIAS in scraping["items"] :
			if "tags" in NOTICIAS.keys():
				for tags in NOTICIAS["tags"] :
					categoria = tags["term"]
					db_categorias = Categoria.objects.filter(nombre=categoria).values('nombre')
					if len(db_categorias) < 1 :
						insert = Categoria(nombre=categoria)
						insert.save()
						print ("Nueva catagoria encontrada " )
						print (categoria)
					print ("La categoria ya existe")
				print ("No existe categorias para esta noticia")

def periodicos_act(RSS) :
	for peri in RSS :
		db_periodicos = Periodico.objects.filter(nombre=peri).values('nombre')
		if len(db_periodicos) < 1 :
			insert = Periodico(nombre=peri)
			insert.save()
			print ("Entrada Periodicos Añadida")


def articulos_act(RSS):
	for DIARIO in RSS:
		scraping = feedparser.parse(RSS[DIARIO])
		for NOTICIAS in scraping['items']:
			if 'tags' in NOTICIAS.keys() :
				FECHA = datetime.fromtimestamp(time.mktime(NOTICIAS['published_parsed']))
				Arti_Search = Articulo.objects.filter(url=NOTICIAS['id'],fecha=FECHA).values('url')
				if len(Arti_Search) < 1 :
					insert = Articulo (url = NOTICIAS['id'], titulo =NOTICIAS['title'],descripcion = NOTICIAS['summary'], author = NOTICIAS['author'], fecha=FECHA)
					insert.Periodicos_id = (Periodico.objects.filter(nombre=DIARIO).values('id')[0]['id'])
					for tags in NOTICIAS['tags']:
						ca = Categoria.objects.filter(nombre=tags['term']).values('nombre')
						insert.categoria.add(ca)
					insert.save()
					print ("categoria Añadida")
					
					


periodicos_act(RSS)
categoria_act(RSS)
articulos_act(RSS)
