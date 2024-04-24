from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import BaseUserManager
from datetime import date

class CustomUserManager(BaseUserManager):
    """
    Пользовательский менеджер, где email является уникальным идентификатором
    для аутентификации вместо username.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Создание и сохранение пользователя с указанным email и паролем.
        """
        if not email:
            raise ValueError(_('Email должен быть установлен'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создание и сохранение суперпользователя с указанным email и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser должен иметь is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser должен иметь is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class UserProfile(AbstractUser):
    GENDER_CHOICES = [
        ('муж', 'Мужчина'),
        ('жен', 'Женщина'),
    ]
    username = None  # Убедитесь, что username полностью удалено
    full_name = models.CharField("ФИО", max_length=100)
    address = models.CharField("Адрес", max_length=200)
    email = models.EmailField("Электронная почта", unique=True)
    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=10, choices=GENDER_CHOICES, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    groups = models.ManyToManyField(Group, related_name='user_profiles_groups', blank=True,
                                    help_text='The groups this user belongs to.')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_profiles_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return f"{self.email} ({self.full_name})"

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None
    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

