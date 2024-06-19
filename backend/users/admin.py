from django.contrib import admin
from . models import CustomUser, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    list_display = ['email', 'is_staff', 'is_active', 'is_superuser']
    list_filter = ['email', 'is_staff', 'is_active', 'is_superuser']
    search_fields = ['email']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']
    list_filter = ['user', 'first_name', 'last_name']
    search_fields = ['user', 'first_name', 'last_name']
    list_per_page = 20

    
