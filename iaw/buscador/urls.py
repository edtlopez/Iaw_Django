from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.IndexView.get_queryset),
#        url(r'^(?P<año>[0-9]{4})/(?P<mes>[0-9]{2})/(?P<dia>[0-9]{2})/$', views.buscador_noticias),

    ]
