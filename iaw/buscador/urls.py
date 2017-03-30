from django.conf.urls import url
from . import views
from buscador.views import IndexView

urlpatterns = [
        url(r'^$', IndexView.get_queryset, name="Buscador"),
        url(r'^resultado/$', IndexView.get_queryset),        
]
