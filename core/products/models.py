from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_brand = models.CharField(max_length=100)
    product_price = models.FloatField()