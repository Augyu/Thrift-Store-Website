from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from thrifts.models import Product
# Create your models here.


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    date_created = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('shopping_cart', 'product')
