import feedparser
from buscador.models import Articulo, Periodico, Categoria
from datetime import datetime
import time

RSS = {

    'elmundo' : 'http://estaticos.elmundo.es/elmundo/rss/portada.xml',
    'elpais' : 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
    'abc' : 'http://www.abc.es/rss/feeds/abcPortada.xml',

}

for DIARIO in RSS :
		scraping = feedparser.parse(RSS[DIARIO])
		for NOTICIAS in scraping['items'] :
            print (NOTICIAS)