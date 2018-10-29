from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ("film", "Film"),
    ("art", "Art"),
    ("design", "Design&Tech"),
    ('game', "Games"),
    ("music", "Music"),
    ("other", "Other")
)


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True, default="None")
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default="Other")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(decimal_places=2, max_digits=30, default=0)
    image = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=100, default='Def_img.png')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class UserConnect(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_account = models.CharField(max_length=100, default='None_imput')