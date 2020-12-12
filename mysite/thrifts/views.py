from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturaltime
from google.cloud import vision
from .models import Product
from comments.models import Comment
from feeds.models import Feed

GCP_RESULT = {'safe': 1, 'unsafe': 0, 'error': -1}


def home(request):
    selling_list = []
    if (request.session.get('role') == 'admin'):
        selling_list = Product.objects.all()

    elif (request.session.get('role') == 'regular'):
        selling_list = Product.objects.filter(
            seller=request.session['username'])

    feeds = Feed.objects.order_by('-created_time')[:10]
    context = {'selling_list': selling_list, "feeds": feeds}
    return render(request, 'thrifts/home.html', context)


def list(request):
    products = Product.objects.all()
    sorting_type = request.GET.get('sorting')
    category = request.GET.get('category')
    product = request.GET.get('product')

    if product:
        products = Product.objects.filter(name__icontains=product)
    if category:
        products = Product.objects.filter(category=category)
    if sorting_type:
        products = products.order_by(sorting_type)
    return render(request, 'thrifts/list.html', {'sorting': sorting_type, 'name': product, 'products': products})


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    comments = Comment.objects.filter(seller_username=product.seller)
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
            user = User.objects.get(username=request.session.get('username'))
            if image:
                is_safe = image_safe_search(image)
                if is_safe == GCP_RESULT['safe']:
                    product.img = image
                elif is_safe == GCP_RESULT['unsafe']:
                    messages.warning(
                        request, 'You picture might be appropriate, please upload another one.')
                    return render(request, 'thrifts/edit.html', context)
                elif is_safe == GCP_RESULT['error']:
                    messages.warning(
                        request, 'The image detector is not working right now, please try again later.')
                    return render(request, 'thrifts/edit.html', context)
            product.save()
            messages.info(request, 'You successfully edited %s' % name)
            feed = Feed(user=user, verb='update a new product.',
                        target=product)
            feed.save()
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

# this is the add item page


def sell(request):
    if request.method == "POST":
        name = request.POST.get('product_name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        seller = request.session['username']
        user = User.objects.get(username=request.session.get('username'))
        is_safe = image_safe_search(image)
        if is_safe == GCP_RESULT['safe']:
            product = Product(name=name, price=price, img=image,
                              description=description, category=category, seller=seller, user=user)
            product.save()
            messages.success(request, 'You successfully added %s' % name)
            # log the feed
            feed = Feed(user=user, verb='created a new product.',
                        target=product)
            feed.save()
            return redirect('thrifts:detail', product.id)
        elif is_safe == GCP_RESULT['unsafe']:
            messages.warning(
                request, 'You picture might be appropriate, please upload another one.')
            return render(request, 'thrifts/add.html')
        elif is_safe == GCP_RESULT['error']:
            messages.warning(
                request, 'The image detector is not working right now, please try again later.')
            return render(request, 'thrifts/add.html')

    return render(request, 'thrifts/add.html')


def seller(request, seller):
    comments = []
    # comments = Comment.objects.filter(seller_username=seller)
    return render(request, 'thrifts/seller.html', {'comments': comments, 'name': seller})


def image_safe_search(image):
    client = vision.ImageAnnotatorClient()
    gcp_image = vision.Image(content=image.read())
    response = client.safe_search_detection(image=gcp_image)

    safe = response.safe_search_annotation

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    if response.error.message:
        return -1

    if likelihood_name[safe.adult] == 'LIKELY' or likelihood_name[safe.adult] == 'VERY_LIKELY' or\
            likelihood_name[safe.medical] == 'LIKELY' or likelihood_name[safe.medical] == 'VERY_LIKELY' or\
            likelihood_name[safe.spoof] == 'LIKELY' or likelihood_name[safe.spoof] == 'VERY_LIKELY' or\
            likelihood_name[safe.violence] == 'LIKELY' or likelihood_name[safe.violence] == 'VERY_LIKELY' or\
            likelihood_name[safe.racy] == 'LIKELY' or likelihood_name[safe.racy] == 'VERY_LIKELY':
        return 0
    else:
        return 1


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
