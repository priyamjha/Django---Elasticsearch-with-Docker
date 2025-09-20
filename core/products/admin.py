from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_brand', 'product_price']