from django.shortcuts import render
from .models import Post
#
def Title(request):
    return render(request, 'projectplace/Title.html', {})
# Create your views here.
