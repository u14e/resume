from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'is_superuser', 'is_active', 'date_joined')
    filter_horizontal = ('groups', 'user_permissions')
