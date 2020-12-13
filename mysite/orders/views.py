from django.shortcuts import render
from .models import Order, OrderItem
from carts.models import ShoppingCart, CartItem
# Create your views here.


def add_order(request, shopping_cart):
    shopping_cart = ShoppingCart.objects.get(pk=shopping_cart)
    order = Order(user=shopping_cart.user, price=shopping_cart.price)
    order.save()
    cart_item = CartItem.objects.filter(shopping_cart=shopping_cart)
    for item in cart_item:
        OrderItem(order=order, product=item.product).save()
        item.product.is_sold = True
        item.product.save()
    shopping_cart.delete()
    return render(request, 'thrifts/home.html')
