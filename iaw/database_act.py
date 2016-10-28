#! /usr/bin/python2.7
import feedparser
from buscador.models import Portada, Fecha
import iaw/settings.py
import datetime

#from django.core.management.base import BaseCommand, CommandError
#from django.db import models
#import models.py

class Act_Database :
	def __init__ (self) :
		pass
		

	def __Exist_fecha (self,datetime):
		salida = False
		if count(Fecha.objects.filter(fecha=datetime)):
			salida = True
		return salida

	def __Exist_Noticia (self,iden):
		salida = False
		if count(Portada.objects.filter(ref=iden)):
			salida = True
		return salida

	def __ID_Fecha (self):
		

	def Update (self):
		
		for rss in RSS :
			A = feedparser.parse(RSS[rss])
			for Noticia in A['items']:
				iden = Noticia['id']
				dt = datetime.datetime(Noticia['published_parsed'][0],A['items'][0]['published_parsed'][1],A['items'][0]['published_parsed'][2],A['items'][0]['published_parsed'][3],A['items'][0]['published_parsed'][4],0)
				if not (__Exist_fecha(dt)) and not( __Exist_Noticia(iden)):
					
					Po = (

						ponom = str(Noticia['title']), 
						editorial = str(RSS[rss])
						url = str(Noticia['link'])
						ref = str(Noticia['id'])


					)


		
		for Noticias_Dia in A['items']:





	def search (self,url,edi):
		rss = feedparser.parse(url)
		for titular in rss['items']:
			DB = Portada( 
				ponom = str(titular['title']), 
				editorial = str(edi), 
				ref = str(titular['id']),
			)

			DB.save()

			print ("OK")


A = Act_Database()
for ele in RSS :
	A.search(RSS[ele],ele)