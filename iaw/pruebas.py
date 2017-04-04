import feedparser
from buscador.models import Articulo, Periodico, Categoria
import datetime
import time


RSS = {

    'elmundo' : 'http://estaticos.elmundo.es/elmundo/rss/portada.xml',
    'elpais' : 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
    'abc' : 'http://www.abc.es/rss/feeds/abcPortada.xml',

}

def articulos_act (RSS) :
	for DIARIO in RSS :
		scraping = feedparser.parse(RSS[DIARIO])
		for NOTICIAS in scraping['items'] :
			print (NOTICIAS['author'])
			print ('--------')

articulos_act(RSS)


#				FECHA = datetime.fromtimestamp(time.mktime(NOTICIAS['published_parsed']))
#				search_link = Articulo.objects.filter(url=str(NOTICIAS['link'],fecha=FECHA)
				

#	def articulos_act (RSS) :
#		for DIARIO in RSS :
#			scraping = feedparser.parse(RSS[DIARIO])
#			for NOTICIAS in scraping['items'] :
#				FECHA = datetime.fromtimestamp(time.mktime(NOTICIAS['published_parsed']))
#				search_link = Articulo.objects.filter(url=str(NOTICIAS['link'],fecha=FECHA).values('link')
#				if len(search_link) < 1 :
#					print ("menor")


#def articulos_act (RSS) :
#	for DIARIO in RSS :
#		scraping = feedparser.parse(RSS[DIARIO])
#		for NOTICIAS in scraping['items'] :
#			FECHA = datetime.fromtimestamp(time.mktime(NOTICIAS['published_parsed']))
#			search_link = Articulo.objects.filter(url=str(NOTICIAS['link'],fecha=FECHA)
#			if len(search_link.values("url")) < 1 :
#				print(NOTICIAS["published"])



#class CateArti (models.Model):
#	categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
#	articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE) through='CateArti',through_fields=('articulo', 'categoria'))