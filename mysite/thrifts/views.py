from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import products
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


def list(request):
    template = loader.get_template('thrifts/list.html')
    context = {'products': products}
    print(products)
    return render(request, 'thrifts/list.html', context)

def detail(request):
    template = loader.get_template('thrifts/detail.html')
    return HttpResponse(template.render())
