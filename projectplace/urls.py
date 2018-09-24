from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.Title, name='Title'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]