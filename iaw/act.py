import feedparser
from buscador.models import Articulo, Periodico, Categoria
from datetime import datetime
import time 
 
RSS = {

#   'elmundo' : 'http://estaticos.elmundo.es/elmundo/rss/portada.xml',
    'elpais' : 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
    'abc' : 'http://www.abc.es/rss/feeds/abcPortada.xml',

}

try:
	
	def categoria_act (RSS):
		for DIARIO in RSS :
			scraping = feedparser.parse(RSS[DIARIO])
			for NOTICIAS in scraping['items'] :
				for tags in NOTICIAS["tags"] :
					categoria = str(tags['term'])
					db_categorias = Categoria.objects.filter(nombre=categoria).values('nombre')
					if len(db_categorias) < 1 :
						insert = Categoria(nombre=str(categoria))
						insert.save()
						print ("Nueva catagoria encontrada " )
						print (categoria)
					print ("La categoria ya existe")
					

	def periodicos_act (RSS) :
		for peri in RSS :
			db_periodicos = Periodico.objects.filter(nombre=peri).values('nombre')
			if len(db_periodicos) < 1 :
				insert = Periodico(nombre=peri)
				insert.save()
				print ('Entrada Periodicos Añadida')

except KeyError: 
		pass






#def articulos_act (RSS) :
#	for DIARIO in RSS :
#		scraping = feedparser.parse(RSS[DIARIO])
#		for NOTICIAS in scraping['items'] :
#			FECHA = datetime.fromtimestamp(time.mktime(NOTICIAS['published_parsed']))
#			search_link = Articulo.objects.filter(url=str(NOTICIAS['link'],fecha=FECHA)
#			if len(search_link.values("url")) < 1 :
#				print(NOTICIAS["published"])


categoria_act(RSS)
periodicos_act(RSS)

