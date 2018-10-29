from django import forms
from .models import Post, UserConnect
from django.contrib.auth.models import User
from django.db import models


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', "category", 'body', "value", "image")


class AddUserStripe(forms.ModelForm):

    class Meta:
        model = UserConnect
        fields = ('stripe_account',)


class AddUserExtradata(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')