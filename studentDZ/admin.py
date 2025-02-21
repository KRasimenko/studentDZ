from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taskmanager_reg.models import CustomUser, Group

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'full_name', 'role', 'group', 'is_approved')
    list_filter = ('role', 'is_approved', 'group')
    actions = ['approve_users']
    
    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)
    approve_users.short_description = "Подтвердить выбранных пользователей"

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Group)