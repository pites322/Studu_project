from django.db import models
from django.utils import timezone

CATEGORY_CHOICES = (
    ("film", "Film"),
    ("art", "Art"),
    ("design", "Design&Tech"),
    ('game', "Games"),
    ("music", "Music"),
    ("other", "Other")
)


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True, default="None")
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default="Other")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(decimal_places=2, max_digits=30, default=0)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='Def_img.png')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# class PostForm(forms.ModelForm):
#
#     model = Post
#     title = models.CharField(max_length=255)
#     category = models.ForeignKey("Film", "Art", "Design&Tech", "Games", "Music", "Other")
#     body = models.TextField(help_text="Enter a brief description of the post")
#     author = models.ForeignKey(User)
#     value = models.DecimalField()
#     image = models.ImageField()
#
#
#     created_at = models.DateTimeField(auto_now_add=True)