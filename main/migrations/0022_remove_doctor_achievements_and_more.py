# Generated by Django 5.0 on 2024-04-07 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_reception_fullname_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='achievements',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='certificates',
        ),
    ]
