from django.contrib.auth.models import BaseUserManager


class NewProfile(BaseUserManager):
    stripe_publock_key = models.CharField(max_length=255, unique=True, default="None")
    stripe_sickret_key = models.CharField(max_length=255, unique=True, default="None")