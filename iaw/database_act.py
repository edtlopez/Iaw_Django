#! /usr/bin/python2.7
import feedparser
from buscador.models import Portada, Fecha
#from django.core.management.base import BaseCommand, CommandError
#from django.db import models
#import models.py

RSS = {

    'elmundo' : 'http://estaticos.elmundo.es/elmundo/rss/portada.xml',
    'elpais' : 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
    'abc' : 'http://www.abc.es/rss/feeds/abcPortada.xml',

}

class Act_Database :
	def __init__ (self) :
		pass
	def search (self,url,edi):
		rss = feedparser.parse(url)
		for titular in rss['items']:
			DB = Portada( 
				ponom = str(titular['title']), 
#				pofecha = titular['published_parsed'], 
				editorial = str(edi), 
				ref = str(titular['id']),
			)

			DB.save()

			print ("OK")


A = Act_Database()
for ele in RSS :
	A.search(RSS[ele],ele)