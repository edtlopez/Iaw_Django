from django import forms
from .models import  *

class articulo_update_form (forms.Form):
	titulo = forms.CharField(label="Titulo",max_length=100)
	url =  forms.URLField(label="url",max_length=200)
	descripcion = forms.CharField(label="Descripcion",max_length=1000)
	author = forms.CharField(label="Author",max_length=100)



	



