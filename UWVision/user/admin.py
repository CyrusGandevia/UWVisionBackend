from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = [
        'username',
        'email',
        'image',
        'is_active',
        'is_staff',
        'is_superuser'
    ]

admin.site.register(User, CustomUserAdmin)