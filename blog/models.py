from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # a short url that identifies the post
    handle = models.CharField(max_length=30, blank=True)

    title = models.CharField(max_length=40, blank=True)

    # a short description of a post
    abstract = models.TextField(default="")

    # the body of a post
    text = models.TextField(blank=True)
    
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.handle
