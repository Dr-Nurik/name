# Generated by Django 5.0 on 2024-03-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_userprofile_auth_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegram ID'),
        ),
    ]