from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import products
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def list(request):
    context = {'products': products}
    for product in products:
        print(product.img[0])
    return render(request, 'thrifts/list.html', context)

def detail(request, product_id):
    context = {}
    for product in products:
        if product.getProductById(product_id):
            context = {'product': product}
            break
    return render(request, 'thrifts/detail.html', context)