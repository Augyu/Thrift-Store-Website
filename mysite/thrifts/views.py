from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import products, fakeuser, fake_selling_list, fakeadmin, Product, Comment
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


def home(request):
    selling_list = []
    if (request.session.get('role') == 'admin'):
        selling_list = Product.objects.all()

    elif (request.session.get('role') == 'regular'):
        selling_list = Product.objects.filter(
            seller=request.session['username'])

    context = {'selling_list': selling_list}
    print(selling_list)

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
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'thrifts/list.html', context)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    comments = Comment.objects.filter(seller=product.seller)
    context = {'product': product, 'comments': comments}
    return render(request, 'thrifts/detail.html', context)


def edit(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'thrifts/edit.html', context)


def delete(request, product_id):
    Product.objects.filter(pk=product_id).delete()
    return render(request, 'thrifts/home.html')


def sell(request):
    if request.method == "POST":
        name = request.POST.get('product_name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        seller = request.session['username']
        product = Product(name=name, price=price, img=image,
                          description=description, category=category, seller=seller)
        product.save()
        return redirect('thrifts:home')

    return render(request, 'thrifts/add.html')
