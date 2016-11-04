from django import forms
from .models import Fecha, Portada

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('fecha')
