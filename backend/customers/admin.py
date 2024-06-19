from django.contrib import admin
from . models import Customer, Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'state', 'country', 'zip_code', 'created_at', 'modified_at']
    list_filter = ['address', 'city', 'state', 'country', 'zip_code', 'created_at', 'modified_at']
    search_fields = ['address', 'city', 'state', 'country', 'zip_code']
    list_per_page = 10


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'modified_at']
    list_filter = ['name', 'email', 'created_at', 'modified_at']
    search_fields = ['name', 'email']
    list_per_page = 10