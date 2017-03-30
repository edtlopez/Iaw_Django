from django import forms
from buscador.models import  Periodico, Articulo


class busqueda_avanzada (forms.ModelForm):
	
	Fecha = forms.DateTimeField()
	Periodico = forms.CharField(label='Periodico', max_length=2)
	Categoria = forms.CharField(label='Categoria', max_length=2)
	Titulo = forms.CharField(label='Titulo', max_length=2)	
	
	class Meta:
		model = Articulo
		fields = ['Fecha','Periodico','Categoria','Titulo']	
	