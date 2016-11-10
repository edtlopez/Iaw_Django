from django import forms
from buscador.models import Fecha, Portada

class search_noticia(forms.ModelForm):
	Año = forms.CharField(label='Año', max_length=4)
	Mes = forms.CharField(label='Mes', max_length=2)
	Dia = forms.CharField(label='Dia', max_length=2)
	
	class Meta:
		model = Fecha
		fields = ['Dia', 'Mes', 'Año']	
