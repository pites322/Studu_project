from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView, ListView
from .forms import AddPostForm
from .models import Post
from django.conf import settings
from django.utils import timezone
#


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

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


class Title(ListView):
    template_name = 'projectplace/Title.html'
    model = Post


class Art(ListView):
    template_name = 'projectplace/Art.html'
    model = Post


class Design(ListView):
    template_name = 'projectplace/Design&Tech.html'
    model = Post


class Games(ListView):
    template_name = 'projectplace/Games.html'
    model = Post


class Music(ListView):
    template_name = 'projectplace/Music.html'
    model = Post


class Other(ListView):
    template_name = 'projectplace/Other.html'
    model = Post


class HomeView(TemplateView):
    template_name = 'projectplace/Title.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        post = Post.objects.values().order_by('-created_at').first()
#        context['posts'] = Post.objects.get_home_posts()

        # if 'view_count' not in self.request.session:
        #     self.request.session['view_count'] = 0
        # self.request.session['view_count'] += 1
        # self.request.session.save()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['some'] = 'value'
        return self.render_to_response(context)



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

