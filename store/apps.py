from __future__ import unicode_literals

from django.apps import AppConfig
from django.contrib import admin
from models import Product


class StoreConfig(AppConfig):
    name = 'store'


admin.site.register(Product)
