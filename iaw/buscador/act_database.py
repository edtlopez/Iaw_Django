import datetime
import feedparser

RSS = {

    'elmundo' : 'http://estaticos.elmundo.es/elmundo/rss/portada.xml',
    'elpais' : 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
    'abc' : 'http://www.abc.es/rss/feeds/abcPortada.xml',

}


class act_database():
	def __init__ (self,RSS) :
		for DIARIO in RSS :
			scraping = feedparser.parse(RSS[DIARIO])
			for NOTICIAS in scraping['items'] :
				print (NOTICIAS['title'])
				print (NOTICIAS['description'])
				print (NOTICIAS['link'])
				print (NOTICIAS['id'])
		


act_database(RSS)
