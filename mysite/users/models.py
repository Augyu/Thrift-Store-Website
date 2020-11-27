from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(default='regular', max_length=50)


@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        Details.objects.create(user=instance)
    else:
        instance.details.save()


# @receiver(post_save, sender=User)
# def save_user_details(sender, instance, **kwargs):
#     instance.details.save()
