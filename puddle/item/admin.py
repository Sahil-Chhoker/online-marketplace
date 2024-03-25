from django.contrib import admin

from .models import Category, Item

# Register your models here.

# To make the modes visible in admin tab
admin.site.register(Category)
admin.site.register(Item)