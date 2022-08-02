from django.db import models
from django.contrib.auth.models import AbstractUser

# Required modules for auto generating Tokens off User creation
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    image = models.CharField(max_length=255, blank=True, null=True)

# Signal -> triggers Token generation when a User is created
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)