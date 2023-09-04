from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q

from accounts.models import Member


@admin.register(Member)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email',]
    fieldsets = [
        (None, {'fields': ("username", "email", "first_name", "last_name")}),
        ("permissions", {'fields': ("is_staff", "user_permissions")}),
    ]
