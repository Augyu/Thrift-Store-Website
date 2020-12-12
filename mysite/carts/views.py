from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ShoppingCart, CartItem
from thrifts.models import Product

# add item to the shopping cart
# 1. check if there is a shopping cart for the current user,
#    if not create a new cart
# 2. check if the item has already in the cart,
#    if not, add item into the shopping cart


def add_to_cart(request):
    if is_ajax and request.method == 'POST':
        username = request.session.get('username')
        user = User.objects.get(username=username)
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        try:
            shopping_cart = ShoppingCart.objects.get(user=user)
        except:
            shopping_cart = ShoppingCart(user=user, price=0)
            shopping_cart.save()
        # add item to cart
        try:
            cart_item = CartItem(shopping_cart=shopping_cart, product=product)
            cart_item.save()
            shopping_cart.price = shopping_cart.price + product.price
            shopping_cart.save()
        except:
            return JsonResponse({'success': 'The item has already in the cart.'}, status=200)

        return JsonResponse({'success': 'You have succesfully added to cart!'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def cart(request):
    if request.method == 'GET':
        username = request.session.get('username')
        user = User.objects.get(username=username)
        try:
            shopping_cart = ShoppingCart.objects.get(user=user)
            cart_item = CartItem.objects.filter(shopping_cart=shopping_cart)
            return render(request, 'carts/home.html', {'cart_item': cart_item})

        except:
            return render(request, 'carts/home.html')

    return render(request, 'carts/home.html')


def delete_from_cart(request, shopping_cart, product):
    shopping_cart = ShoppingCart.objects.get(id=shopping_cart)
    delete_item = CartItem.objects.get(
        shopping_cart=shopping_cart, product=product)
    shopping_cart.price = shopping_cart.price - delete_item.product.price
    shopping_cart.save()
    delete_item.delete()

    cart_item = CartItem.objects.filter(shopping_cart=shopping_cart)
    if not cart_item:
        shopping_cart.delete()

    return render(request, 'carts/home.html', {'cart_item': cart_item})


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
