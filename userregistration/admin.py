from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'name', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'phone', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name', 'phone')
    ordering = ('email',)

admin.site.register(CustomUser, UserAdmin)
