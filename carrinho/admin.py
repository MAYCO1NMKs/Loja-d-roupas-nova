from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'endereco')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefone', 'endereco')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
