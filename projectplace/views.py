from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, FormView, ListView
from .forms import AddPostForm, AddUserStripe, AddUserExtradata
from .models import Post, UserConnect
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from functools import wraps
import json


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        if request.method == "POST":
            form = AddPostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.created_at = timezone.now()
                post.save()
                return redirect('/accounts/profile/', pk=post.pk)
        else:
            form = AddPostForm(instance=post)
        return render(request, 'projectplace/post_edit.html', {'form': form})
    else:
        def posts(self, request):
            import stripe
            stripe.api_key = "sk_test_KoPBXsif8wO9pa9GPKU9qsz6"
            stripe.Charge.create(
                amount=10000,
                currency="usd",
                source=request.POST['stripeToken'],  # obtained with Stripe.js
                description="Test payment",
                application_fee=100,
                capture=False
            )
        return render(request, 'projectplace/post_detail.html', {'post': post})


class HomeView(TemplateView):
    template_name = 'projectplace/Title.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['Posts'] = Post.objects.order_by('-created_at')
        # context['Art'] = Post.objects.filter(category="art").order_by('-created_at')
        # context['Design'] = Post.objects.filter(category="design").order_by('-created_at')
        # context['Games'] = Post.objects.filter(category="games").order_by('-created_at')
        # context['Music'] = Post.objects.filter(category="music").order_by('-created_at')
        # context['Other'] = Post.objects.filter(category="other").order_by('-created_at')
        return context


def PostNew(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = AddPostForm()
    return render(request, 'projectplace/post_edit.html', {'form': form})


class Profile(TemplateView):
    template_name = 'projectplace/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        user_posts = Post.objects.filter(
            author=self.request.user
        )
        user_stripe = UserConnect.objects.filter(user_id=self.request.user.pk)
        name_first_last = User.objects.filter(username=self.request.user)
        context['posts'] = user_posts
        context['stripe'] = user_stripe
        context['extradata'] = name_first_last
        return context


def user_mod(request,  *args, **kwargs):
    user_stripe = get_object_or_404(UserConnect, user_id=request.user.pk)
    user_first_sec_name = get_object_or_404(User, username=request.user)
    name_first_last = User.objects.filter(username=request.user)
    if request.method == "POST":
        # body_unicode = response.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # print(body)
        form1 = AddUserStripe(request.POST, instance=user_stripe)
        form2 = AddUserExtradata(request.POST, instance=user_first_sec_name)
        if form1.is_valid() and form2.is_valid():
            user_id = request.user.pk
            sripe = form1.save(commit=False)
            first_last_name = form2.save(commit=False)
            sripe.save()
            first_last_name.save()
            return redirect('/accounts/profile/')
    else:
        form1 = AddUserStripe(request.POST, instance=user_stripe)
        form2 = AddUserExtradata(request.POST, instance=user_first_sec_name)
        user_id = request.user.pk
    return render(request, 'projectplace/account_extradata.html', {'form1': form1, 'form2': form2, 'stripe': user_stripe, "user": name_first_last})


# def json_reader(request):
#     response = request.get("https://dashboard.stripe.com/oauth/authorize?response_type=code&client_id=ca_DhClBiSS69lYQZkAo1yevWDDjWOYhjYB&scope=read_write")
#     json_data = json.loads(response.text)
#     print(json_data)

