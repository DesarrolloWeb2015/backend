from django.db import models
from clients.models import Clients


# Create your models here.
class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    slogan = models.CharField(max_length=128)
    tiny_description = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey(Clients)

    class Meta:
        ordering = ('created', )


class Gallery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32)
    project = models.ForeignKey(Project)


class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32)
    url_file = models.URLField()
    gallery = models.ForeignKey(Gallery)