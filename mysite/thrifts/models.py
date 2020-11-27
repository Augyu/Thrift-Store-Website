from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    img = models.ImageField(upload_to='image/')
    description = models.TextField(blank=True)
    seller = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.name


class Comment(models.Model):
    buyer = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    comment = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['-date_posted']


fakeuser = {'username': "David", 'password': "password"}
fakeadmin = {'username': "admin", 'password': "password"}
