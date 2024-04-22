from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rat

@receiver(post_save, sender=User)
def create_rat(sender, instance, created, **kwargs):
    if created:
        Rat.objects.create(user=instance, name=instance.username, email=instance.email)

@receiver(post_save, sender=User)
def save_rat(sender, instance, **kwargs):
    instance.rat.save()

