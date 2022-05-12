# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User, Department

@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info',), {'fields': ('email',)}),
        (_('Permissions',), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Password',), {'fields': ('password_changed', 'password_changed_date',)}),
        (_('Important Dates',), {'fields': ('last_login', 'date_joined',)}),
    )

    list_display = ('username', 'email', 'full_name', 'is_active', 'is_staff')
    search_fields = ('username', 'full_name', 'email')
    filter_horizontal = ('groups', 'user_permissions', 'departments')

