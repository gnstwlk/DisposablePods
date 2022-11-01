from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# class Dudelki(models.Model):
#     NameProduct = models.CharField(max_length=255)
#     Description = models.CharField(max_length=255)


class Availability(models.Model):
    NameProduct = models.CharField(max_length=255)
    Amount = models.IntegerField()
    WholesalePrice = models.DecimalField(max_digits=6, decimal_places=2)
    RetailPrice = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.NameProduct

class Sales(models.Model):
    Product = models.ForeignKey(Availability, on_delete=models.CASCADE)
    DateOfSale = models.DateField()
    def __str__(self):
        return self.Product.NameProduct

