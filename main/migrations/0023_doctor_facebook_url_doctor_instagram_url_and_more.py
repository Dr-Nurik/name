# Generated by Django 5.0 on 2024-04-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_doctor_achievements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='facebook_url',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook URL'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram URL'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='telegram_url',
            field=models.URLField(blank=True, null=True, verbose_name='Telegram URL'),
        ),
    ]
