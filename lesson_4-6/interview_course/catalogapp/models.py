from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=64,
                                     verbose_name='category name')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = CurrentSiteManager('site')

    def __str__(self):
        return self.category_name


class ProductItem(models.Model):
    product_name = models.CharField(max_length=128,
                                    verbose_name='product name')
    product_category = models.ManyToManyField(ProductCategory)
    added = models.DateTimeField(auto_now_add=True, verbose_name='date added')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0,
                                verbose_name='price')
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name='product quantity')
    supplier_name = models.CharField(max_length=128,
                                     verbose_name='supplier name')
    site = models.ManyToManyField(Site)
    objects = CurrentSiteManager('site')
