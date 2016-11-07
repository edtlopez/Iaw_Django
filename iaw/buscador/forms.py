from django import forms
from .models import Fecha, Portada

class search_noticia(forms.ModelForm):
	

	class Meta:
		pass
		model = Fecha
		fields = ('fecha',)
		
	

