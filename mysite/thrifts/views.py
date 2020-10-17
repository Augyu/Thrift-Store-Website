from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import products, fakeuser
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def user(request):
    return render(request, 'thrifts/user.html')

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == fakeuser['username'] and password == fakeuser['password']:
        request.session['username'] = username
        request.session['role'] = 'regular'
        return redirect('thrifts:list')
    else:
        return render(request, 'thrifts/user.html')

def logout(request):
    try:
        del request.session['username']
        del request.session['role']
    except KeyError:
        pass   
    return redirect('thrifts:user')

def list(request):
    context = {'products': products}
    return render(request, 'thrifts/list.html', context)

def detail(request, product_id):
    context = {}
    for product in products:
        if product.getProductById(product_id):
            context = {'product': product}
            break
    return render(request, 'thrifts/detail.html', context)
