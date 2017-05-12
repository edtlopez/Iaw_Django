from django.conf.urls import url, include
from buscador.views import *

urlpatterns = [
		url(r'^articulo/(?P<id>[0-9]+)/$', ArticleDetailView.as_view(), name='article-detail'),
		url(r'^articulo/edit/(?P<id>[0-9]+)/$',AuthorUpdate.as_view(),name="artedit"),
		url(r'^articulo/del/(?P<id>[0-9]+)/$',ArticuloDelete.as_view(),name="artdel"),
		url('^', include('django.contrib.auth.urls')),
        url(r'^$', Articulolist.as_view(),name='home'), 


]

