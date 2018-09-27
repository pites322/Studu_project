from django import forms
from .models import Post
from django.db import models
from django.db.models.signals import post_save

class PostForm(forms.ModelForm):

    model = Post
    title = models.CharField(max_length=255)
    body = models.TextField()
#    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body')
