from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth import get_user_model

@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance, *args, **kwargs):
    instance.userprofile.save()