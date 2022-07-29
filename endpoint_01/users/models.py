from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    key = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
