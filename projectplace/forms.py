from django import forms
from .models import Post
from django.db import models


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', "category", 'body', "value", "image")


