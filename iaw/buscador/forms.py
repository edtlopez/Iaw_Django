from django import forms
from buscador.models import  Portada

class search_noticia_form(forms.ModelForm):
	Año = forms.CharField(label='Año', max_length=4)
	Mes = forms.CharField(label='Mes', max_length=2)
	Dia = forms.CharField(label='Dia', max_length=2)
	
	class Meta:
		model = Portada
		fields = ['Dia', 'Mes', 'Año']	
