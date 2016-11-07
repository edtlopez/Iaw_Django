from django.conf.urls import url
from .views import IndexView

urlpatterns = [
        url(r'^$', IndexView.Buscador),
        url(r'^(?P<año>[0-9]{4})/(?P<mes>[0-9]{2})/(?P<dia>[0-9]{2})/$', IndexView.search),

    ]
