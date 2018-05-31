from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^filter$', views.filter, name='detail'),
    url(r'^(?P<tweetID>[0-9]+)$', views.details, name='detail'),
]