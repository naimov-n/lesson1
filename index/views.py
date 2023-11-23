from django.http import  HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    menu = [{'title': 'Home'},{'title': 'News'},{'title': 'About'}]

    return render(request, 'index/index.html', {'title': "Home page", 'menu': menu})


def create(request):

    return render(request, 'index/create.html', {'title': "News page"})


def news(request):
    return render(request, 'index/news.html', {'title': "News page"})


def newsInner(request, id):
    return HttpResponse(f"<h1>News Page</h1> <br/> parametr: {id}")


def about(request):
    if request.GET:
        return HttpResponse(f"<h1>News Page</h1> {request.GET['name']}")
    else:
        return redirect('/')
