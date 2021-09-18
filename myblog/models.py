from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):

    choices = (
        ('published', 'PUBLISHED'),
        ('draft', 'DRAFT')
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=choices,max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.title
