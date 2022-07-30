from django.db import models


class Issue(models.Model):
    summary = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=500, blank=True)
    issuetype = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100)
