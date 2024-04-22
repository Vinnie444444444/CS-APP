# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Workout, Rat, Exercise

# Define your custom UserAdmin class
class CustomUserAdmin(BaseUserAdmin):
    # Your customizations here
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined")

# Unregister the default UserAdmin
admin.site.unregister(User)

# Register User with the customized UserAdmin
admin.site.register(User, CustomUserAdmin)

# Register other models
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Rat)
