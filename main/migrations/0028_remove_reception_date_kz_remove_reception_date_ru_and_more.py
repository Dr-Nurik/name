# Generated by Django 5.0 on 2024-04-08 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_service_image_kz_service_image_ru_service_price_kz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reception',
            name='date_kz',
        ),
        migrations.RemoveField(
            model_name='reception',
            name='date_ru',
        ),
        migrations.RemoveField(
            model_name='reception',
            name='time_kz',
        ),
        migrations.RemoveField(
            model_name='reception',
            name='time_ru',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image_kz',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image_ru',
        ),
    ]
