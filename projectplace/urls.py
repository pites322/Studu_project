from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.Title.as_view(), name='Title'),
#    url(r'^$', views.HomeView.as_view(), name='Title'),
#    url(r'^$', views.title, name='title'),
    url(r'^post/new/$', views.PostNew, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostNew, name='post_edit'),
    url(r'^art/$', views.Art.as_view(), name='Art'),
    url(r'^design&tech/$', views.Design.as_view(), name='Design'),
    url(r'^games/$', views.Games.as_view(), name='Games'),
    url(r'^music/$', views.Music.as_view(), name='Music'),
    url(r'^other/$', views.Other.as_view(), name='Other'),
]

