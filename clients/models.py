from django.db import models
# Create your models here.


class Clients(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=256)

    class Meta:
        ordering = ('created', )
