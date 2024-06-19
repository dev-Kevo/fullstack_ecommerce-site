from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'modified_at']
    list_filter = ['name', 'created_at', 'modified_at']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created_at', 'modified_at']
    list_filter = ['name', 'category', 'price', 'created_at', 'modified_at']
    search_fields = ['name', 'category']
    list_per_page = 20
    