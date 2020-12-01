from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    comment = models.TextField(blank=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='seller')
    seller_username = models.CharField(max_length=200)
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='buyer')
    buyer_username = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']
