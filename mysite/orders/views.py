from django.shortcuts import render, redirect
from .models import Order, OrderItem
from carts.models import ShoppingCart, CartItem
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def add_order(request, shopping_cart):
    shopping_cart = ShoppingCart.objects.get(pk=shopping_cart)
    user = shopping_cart.user
    order = Order(user=shopping_cart.user, price=shopping_cart.price)
    order.save()
    cart_item = CartItem.objects.filter(shopping_cart=shopping_cart)
    for item in cart_item:
        OrderItem(order=order, product=item.product).save()
        item.product.is_sold = True
        item.product.save()
    shopping_cart.delete()
    messages.success(request, 'You successfully created an order!')
    return redirect('orders:home', user.username)


def home(request, username):
    user = User.objects.get(username=username)
    orders = Order.objects.filter(user=user)
    data = []
    for order in orders:
        items = OrderItem.objects.filter(order=order).select_related('product')
        temp = []
        for item in items:
            temp.append(item.product)
        data.append(
            {'order_id': order.id, 'price': order.price, 'items': temp})
    return render(request, 'orders/home.html', {'orders': data})
