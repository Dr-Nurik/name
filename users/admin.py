from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileAdmin(UserAdmin):
    # Укажите поля, которые хотите отобразить
    list_display = ('email', 'full_name', 'is_staff')

    # Настройка полей для формы редактирования
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),  # Изменено здесь
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Настройка полей для формы создания пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'full_name',)
    ordering = ('email',)
    filter_horizontal = ()

# Регистрация модели пользователя с указанным классом администратора
admin.site.register(UserProfile, UserProfileAdmin)
