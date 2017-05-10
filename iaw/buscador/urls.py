from django.conf.urls import url, include
from buscador.views import *

urlpatterns = [
		url(r'^articulo/(?P<id>[0-9]+)/$', ArticleDetailView.as_view(), name='article-detail'),
		url('^', include('django.contrib.auth.urls')),
        url(r'^$', Articulolist.as_view(),name='home'),   

]

