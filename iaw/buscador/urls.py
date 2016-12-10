from django.conf.urls import url
from . import views
from buscador.views import IndexView

urlpatterns = [
        url(r'^$', IndexView.Buscador, name="Buscador"),
        url(r'^resultado/$', IndexView.Resultado),        
]
