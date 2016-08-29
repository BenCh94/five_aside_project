from __future__ import unicode_literals

from django.db import models
from five_aside_project import settings


# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
