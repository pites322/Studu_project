from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.conf import settings

if settings.DEBUG:
    urlpatterns = [
        url(r'^$', views.HomeView.as_view(), name='Title'),
        url(r'^post/new/$', views.PostNew, name='post_new'),
        url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
        url(r'^post/(?P<pk>\d+)/edit/$', views.PostNew, name='post_edit'),
    ]


