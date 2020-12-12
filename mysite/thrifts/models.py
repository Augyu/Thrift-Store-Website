from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    img = models.ImageField(upload_to='image/')
    description = models.TextField(blank=True)
    seller = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField()

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('thrifts:detail', args=[self.id])
