from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls.static import static
from buscador.views import *
from django.conf.urls.static import static

urlpatterns = [
        url('',include('social.apps.django_app.urls', namespace='social')),
		url(r'^articulo/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='article-detail'),
		url(r'^articulo/edit/(?P<pk>[0-9]+)/$',login_required(AuthorUpdate.as_view(),login_url="/login/"),name="artedit"),
		url(r'^articulo/del/(?P<pk>[0-9]+)/$',login_required(permission_required(ArticuloDelete.as_view(), 'articulo_del', raise_exception=True),login_url="/login/"),name="artdel"),
		url('^', include('django.contrib.auth.urls')),
        url(r'^$', Articulolist.as_view(),name='home'),


         
  		



]

