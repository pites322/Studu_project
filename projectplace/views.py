from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
#
def Title(request):
    return render(request, 'projectplace/Title.html', {})

def post_new(request):
    def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'projectplace/post_edit.html', {'form': form})

    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('post_detail', pk=post.pk)
    # else:
    #     form = PostForm()
    # return render(request, 'blog/post_edit.html', {'form': form})