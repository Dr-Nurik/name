from django.core.exceptions import ValidationError
from datetime import date

def validate_date(value):
    if value < date.today():
        raise ValidationError("Дата не может быть в прошлом")

def validate_time(value):
    # Здесь ваша логика для проверки времени
    pass
