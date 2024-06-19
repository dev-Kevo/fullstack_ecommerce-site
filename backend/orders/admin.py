from django.contrib import admin
from . models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order_number', 'product', 'status', 'created_at']
    list_filter = ['customer', 'order_number', 'product', 'status', 'created_at']
    search_fields = ['customer', 'order_number', 'product', 'status', 'created_at']
    list_per_page = 20
