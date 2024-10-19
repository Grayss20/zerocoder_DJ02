from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'caption': 'Ferrets Django'})


def new(request):
    return render(request, 'main/new.html')


def data(request):
    return HttpResponse("<h1>Data text.</h1>")


def test(request):
    return HttpResponse("<h1>Test text.</h1>")