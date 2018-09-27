from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.title, name='Title'),
    url(r'^post/new/$', views.PostNew, name='post_new'),
]