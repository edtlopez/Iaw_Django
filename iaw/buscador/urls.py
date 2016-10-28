from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.buscador_index),
        url(r'^(?P<año>[0-9]{4})/(?P<mes>[0-9]{2})/(?P<dia>[0-9]{2})/$', views.buscador_noticias),

    ]