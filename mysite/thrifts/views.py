from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import products, fakeuser, fake_selling_list, fakeadmin
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def home(request):
    context = {'selling_list': fake_selling_list}
    print(context)
    return render(request, 'thrifts/home.html', context)

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    if username == fakeuser['username'] and password == fakeuser['password']:
        request.session['username'] = username
        request.session['role'] = 'regular'
    elif username == fakeadmin['username'] and password == fakeadmin['password']:
        request.session['username'] = username
        request.session['role'] = 'admin'
    return redirect('thrifts:home')

def logout(request):
    try:
        del request.session['username']
        del request.session['role']
    except KeyError:
        pass   
    return redirect('thrifts:home')

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

def sell(request):
    return render(request, 'thrifts/add.html')