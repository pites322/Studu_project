from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from projectplace.forms import AddPostForm
#

def title(request):
    return render(request, 'projectplace/Title.html', {})


class PostNew(FormView):
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
        # return render(request, 'projectplace/post_edit.html', {'form': form})

        template_name = 'projectplace/post_edit.html'
        form_class = AddPostForm
        success_url = '/'

        def get_form_kwargs(self):
            form_kwargs = super(PostNew, self).get_form_kwargs()
            if 'pk' in self.kwargs:
                form_kwargs['instance'] = Post.objects.get(id=self.kwargs['pk'])
            return form_kwargs

        def form_valid(self, form):
            post = form.save(commit=False)
            post.owner = self.request.user
            if post.is_published:
                post.published_at = timezone.now()
            post.save()
            return super(PostNew, self).form_valid(form)

