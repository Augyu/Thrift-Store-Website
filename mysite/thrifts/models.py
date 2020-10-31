from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    img = models.ImageField(upload_to='image/')
    description = models.TextField(blank=True)
    seller = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
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


# comment1 = Comment('David cleaned the product before he sold it.',
#                    'Jenny',
#                    'David',
#                    datetime(2020, 9, 10))
# comment2 = Comment('I would loved to buy things from David again.',
#                    'Frank',
#                    'David',
#                    datetime(2020, 4, 5))
# comment3 = Comment('David cleaned the product before he sold it.',
#                    'Sharon',
#                    'David',
#                    datetime(2019, 3, 2))
# comment4 = Comment('Really cheap things!',
#                    'Tim',
#                    'David',
#                    datetime(2016, 12, 24))

fakeuser = {'username': "David", 'password': "password"}
fakeadmin = {'username': "admin", 'password': "password"}
