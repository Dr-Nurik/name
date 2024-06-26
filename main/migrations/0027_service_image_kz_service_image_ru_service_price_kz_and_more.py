# Generated by Django 5.0 on 2024-04-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_specializationcategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image_kz',
            field=models.ImageField(default='', null=True, upload_to='service_images/', verbose_name='Фотография услуг'),
        ),
        migrations.AddField(
            model_name='service',
            name='image_ru',
            field=models.ImageField(default='', null=True, upload_to='service_images/', verbose_name='Фотография услуг'),
        ),
        migrations.AddField(
            model_name='service',
            name='price_kz',
            field=models.CharField(default='Уточняйте у администратора', max_length=100, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='service',
            name='price_ru',
            field=models.CharField(default='Уточняйте у администратора', max_length=100, null=True, verbose_name='Цена'),
        ),
    ]
