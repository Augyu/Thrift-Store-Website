from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from .models import products, fakeuser, fake_selling_list, fakeadmin, Product, Comment
# Create your views here.


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
    sorting_type = request.GET.get('sorting')
    if sorting_type:
        products = Product.objects.all().order_by(sorting_type)
    else:
        products = Product.objects.all()
    return render(request, 'thrifts/list.html', {'products': products})


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    comments = Comment.objects.filter(seller=product.seller)
    context = {'product': product, 'comments': comments}
    return render(request, 'thrifts/detail.html', context)


def edit(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        context = {'product': product}

        if request.method == "POST":
            name = request.POST.get('product_name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            category = request.POST.get('category')
            image = request.FILES.get('image')
            product.name = name
            product.price = price
            product.description = description
            product.category = category
            if image:
                product.img = image
            product.save()
            messages.info(request, 'You successfully edited %s' % name)
            return redirect('thrifts:home')

        return render(request, 'thrifts/edit.html', context)
    except Product.DoesNotExist:
        return render(request, 'thrifts/home.html')


def delete(request, product_id):
    if is_ajax(request) and request.method == 'POST':
        try:
            Product.objects.get(pk=product_id).delete()
            messages.warning(request, 'You successfully deleted the product.')
            return JsonResponse({'success': 'success'}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'No product found'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)

#  add view


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
        messages.success(request, 'You successfully added %s' % name)
        return redirect('thrifts:detail', product.id)

    return render(request, 'thrifts/add.html')


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
