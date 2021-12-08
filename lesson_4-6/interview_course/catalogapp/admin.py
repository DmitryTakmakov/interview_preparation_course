from django.contrib import admin

# Register your models here.
from catalogapp.models import ProductItem, ProductCategory

admin.site.register((ProductItem, ProductCategory,))
