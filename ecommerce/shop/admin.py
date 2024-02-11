from django.contrib import admin

# Register your models here.
from django.contrib import admin

from shop.models import category,product

# Register your models here.
admin.site.register(category)
admin.site.register(product)
