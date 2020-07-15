from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })
    # return HttpResponse('<h1>About Us</h1>')