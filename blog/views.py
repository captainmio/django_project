from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Rustum Jordan',
        'title': 'Blog post 1',
        'content': 'This is a post',
        'date_posted': 'August 20, 2020'
    },
    {
        'author': 'Jimmy Doe',
        'title': 'Blog post 2',
        'content': 'Hey guys',
        'date_posted': 'August 12, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })
    # return HttpResponse('<h1>About Us</h1>')
BDO = 51,000
bpi = 52,557