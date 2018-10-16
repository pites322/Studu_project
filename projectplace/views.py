from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, FormView, ListView
from .forms import AddPostForm
from .models import Post
from django.conf import settings
from django.utils import timezone


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
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
        context['posts'] = user_posts
        return context


    # def stripe_connect(self, **kwargs):
    #     profile = get_object_or_404(Profile, pk=pk)
    #     import stripe
    #     stripe.api_key = "sk_test_KoPBXsif8wO9pa9GPKU9qsz6"
    #
    #     acct = stripe.Account.create(
    #         country="US",
    #         type="custom"
    #     )
    #     return render(request, 'projectplace/post_detail.html', {'post': post})

